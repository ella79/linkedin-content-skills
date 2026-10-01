#!/usr/bin/env python3
"""
claims.py - the third gate: is any of this actually backed?

detect.py asks whether a draft reads as human. reach.py asks whether the feed
will carry it. Neither one cares whether a single word of it is true, and a
confident wrong number survives both.

This cannot verify the world. What it can do is refuse to let a factual claim
leave the draft unless the research you did actually contains it:

  - every number in the post must appear in the sources file
  - every named study, company or person must appear there too
  - a number in a sentence about yourself must come from the story bank,
    because invented personal metrics are the easiest thing to write and the
    hardest thing to walk back

Usage
  claims.py draft.txt --sources research.txt [--story ~/.claude/linkedin/story-bank.md]

Write the sources file while you research: paste the quotes and the URLs. It is
the evidence, so it has to exist before the draft, not after.
Exit code is 0 only when nothing is UNBACKED.
"""
import argparse, re, sys, os

# 41%, 1,080, 4.8 million, 2026, 15x, two thirds
NUM = re.compile(r'\b\d[\d,.]*\s*(?:%|percent|million|billion|k\b|x\b)?', re.I)
WORD_NUM = re.compile(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|'
                      r'eleven|twelve|thirteen|fourteen|fifteen|twenty|thirty|'
                      r'forty|fifty|hundred|thousand)\b', re.I)
# A capitalised run that is not at the start of a sentence: likely a name.
PROPER = re.compile(r'(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,})*)\b', re.M)
SELF = re.compile(r'\b(I|my|me|we|our)\b', re.I)

# Words that look like names but are ordinary sentence starters or common nouns.
IGNORE = {"The", "This", "That", "These", "Those", "It", "They", "There", "What",
          "When", "Where", "Which", "While", "And", "But", "So", "If", "Not",
          "Your", "You", "Their", "Here", "Now", "Both", "Each", "Every", "One",
          "Two", "Three", "Fourteen", "Fifteen", "Nothing", "Where", "Link",
          "Python", "English"}

def norm(s):
    s = s.lower().replace("percent", "%").replace("per cent", "%")
    return re.sub(r'[,\s]', '', s).rstrip('.')

def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

def check(draft, sources, story):
    src = sources.lower()
    src_nums = {norm(m.group()) for m in NUM.finditer(sources)}
    story_nums = {norm(m.group()) for m in NUM.finditer(story)} if story else set()
    rows, fails = [], 0

    for sent in sentences(draft):
        if sent.lstrip().startswith("#"):
            continue
        for m in list(NUM.finditer(sent)) + list(WORD_NUM.finditer(sent)):
            tok = m.group().strip()
            n = norm(tok)
            if not n or n in {"1", "2", "3", "4", "5"}:
                continue  # list counters and tiny ordinals are not claims
            # a number written as a word counts as backed when the word is in
            # the research, which is how people actually quote "five platforms"
            if WORD_NUM.fullmatch(tok) and tok.lower() in src:
                rows.append(("ok", tok, "in sources")); continue
            personal = bool(SELF.search(sent))
            if n in src_nums:
                rows.append(("ok", tok, "in sources"))
            elif n in story_nums:
                rows.append(("ok", tok, "in story bank"))
            elif personal:
                rows.append(("FAIL", tok, "a number about you, not in the story bank")); fails += 1
            else:
                rows.append(("FAIL", tok, "not in the sources file")); fails += 1

    seen = set()
    for name in PROPER.findall(draft):
        head = name.split()[0]
        if head in IGNORE or name in seen:
            continue
        seen.add(name)
        if name.lower() in src:
            rows.append(("ok", name, "in sources"))
        else:
            rows.append(("warn", name, "named but not in the sources file"))
    return rows, fails

def main():
    p = argparse.ArgumentParser()
    p.add_argument("draft")
    p.add_argument("--sources", required=True, help="the research you actually did")
    p.add_argument("--story", default=os.path.expanduser("~/.claude/linkedin/story-bank.md"))
    a = p.parse_args()
    draft = open(a.draft, encoding="utf-8").read()
    if not os.path.exists(a.sources):
        sys.exit(f"no sources file at {a.sources}. Research first, then draft.")
    sources = open(a.sources, encoding="utf-8").read()
    story = open(a.story, encoding="utf-8").read() if os.path.exists(a.story) else ""

    rows, fails = check(draft, sources, story)
    print("\n  CLAIMS CHECK\n  " + "=" * 58)
    if not rows:
        print("  no factual claims found. Nothing to back.")
    for state, tok, why in rows:
        mark = {"ok": "  ok  ", "warn": " warn ", "FAIL": " FAIL "}[state]
        print(f"  [{mark}] {tok[:28]:<30} {why}")
    print("  " + "-" * 58)
    print(f"  {'BACKED' if not fails else 'UNBACKED'}: {fails} claim(s) with nothing behind them\n")
    return 0 if not fails else 1

if __name__ == "__main__":
    sys.exit(main())
