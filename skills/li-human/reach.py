#!/usr/bin/env python3
"""
reach.py - check a LinkedIn draft against the distribution mechanics that decide
how many people ever see it. This is not about whether the writing is good.
detect.py asks "does it read as human". This asks "will the feed carry it".

Every rule here comes from documented 2026 feed behaviour, not taste:
  - a post with an external link in the body reaches 50-70% fewer people
  - the first ~140 chars (mobile) / ~210 (desktop) are all that show before "see more"
  - dwell time is the heaviest ranking signal; 150-300 words earns the click
  - hashtags test identical at 0-2 and 5+, so a wall buys nothing
  - under 2s on a post is a scroll-past and scores nothing; 8s+ is a strong signal
  - comments longer than four words count for more than generic ones
Exit code is 0 only when nothing FAILS, so it can gate a pipeline.
"""
import re, sys

URL = re.compile(r'(https?://|www\.|\b[\w-]+\.(com|io|dev|ai|org|net|me|co)\b)', re.I)

def check(text):
    out, fails = [], 0
    lines = [l for l in text.strip().splitlines() if l.strip()]
    hook = lines[0] if lines else ""
    body = "\n".join(lines)
    tags = re.findall(r'(?<!\w)#\w+', body)
    # body words, hashtags excluded
    words = len(re.sub(r'(?<!\w)#\w+', '', body).split())

    def rule(ok, warn, name, detail):
        nonlocal fails
        state = "PASS" if ok else ("WARN" if warn else "FAIL")
        if state == "FAIL": fails += 1
        out.append((state, name, detail))

    rule(len(hook) <= 140, len(hook) <= 210, "HOOK LENGTH",
         f"{len(hook)} chars. Mobile cuts at ~140, desktop at ~210.")
    rule(hook.count(".") + hook.count("?") + hook.count("!") <= 2, True, "HOOK FOCUS",
         "Line 1 should carry one idea, not three sentences.")
    body_no_tags = re.sub(r'(?<!\w)#\w+', '', body)
    links = URL.findall(body_no_tags)
    rule(not links, False, "NO LINK IN BODY",
         f"{len(links)} link-like token(s). Links in the body cost 50-70% of reach. Move to the first comment."
         if links else "No external link in the body.")
    rule(150 <= words <= 300, 120 <= words <= 350, "LENGTH FOR DWELL",
         f"{words} words. Target 150-300, the dwell window.")
    rule(len(tags) <= 2, len(tags) <= 3, "HASHTAGS",
         f"{len(tags)} hashtags. 0-2 performs the same as 5+, so extras are noise.")
    has_q = body.rstrip().endswith("?") or any(l.strip().endswith("?") for l in lines[-3:])
    rule(has_q, True, "CTA", "A question near the end invites the comments that drive phase 2.")

    # A yes/no question gets yes/no answers, and a comment under five words is
    # worth less to the ranker than a substantive one. Open questions earn length.
    qline = next((l.strip() for l in reversed(lines) if l.strip().endswith("?")), "")
    openers = ("what", "how", "why", "where", "which", "when", "who")
    closed = ("do ", "does ", "did ", "are ", "is ", "was ", "were ", "have ",
              "has ", "can ", "could ", "would ", "will ", "should ", "any ")
    first = qline.lower().lstrip("# ")
    ok_open = (not qline) or first.startswith(openers)
    rule(ok_open, not first.startswith(closed), "OPEN QUESTION",
         f'"{qline[:48]}" invites more than a yes.' if ok_open
         else f'"{qline[:48]}" can be answered with one word. Open it with what/how/why.')

    # Dwell is the heaviest signal. Under 2s scores nothing, 8s+ scores strongly,
    # and a post that takes ~20s to read has room to get there.
    secs = words / 3.5
    rule(secs >= 20, secs >= 12, "READ TIME",
         f"~{secs:.0f}s to read. Under 2s is a scroll-past, 8s+ is a strong signal.")
    return out, fails

def main():
    if len(sys.argv) < 2:
        print("usage: reach.py draft.txt"); return 2
    text = open(sys.argv[1], encoding="utf-8").read()
    out, fails = check(text)
    print("\n  REACH CHECK\n  " + "=" * 58)
    for state, name, detail in out:
        mark = {"PASS": "  ok  ", "WARN": " warn ", "FAIL": " FAIL "}[state]
        print(f"  [{mark}] {name:<18} {detail}")
    print("  " + "-" * 58)
    print(f"  {'CARRIES' if not fails else 'BLOCKED'}: {fails} rule(s) failed\n")
    return 0 if not fails else 1

if __name__ == "__main__":
    sys.exit(main())
