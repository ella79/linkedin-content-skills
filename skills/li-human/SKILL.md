---
name: li-human
description: Humanize a LinkedIn draft before anyone reads it. Runs two real scripts - humanize.py strips invisible characters, em-dashes and 100+ slop phrases, detect.py scores the draft on five human-vs-machine checks. Use on every post, comment or reply before showing it. Reads voice.md.
---

# li-human

The humanizer. Two scripts that actually run, and they live in this skill's own
folder so they travel with it on install. Run it, do not eyeball.

## Run it
The scripts sit next to this SKILL.md (e.g. `~/.claude/skills/li-human/` after a
global install, or `.claude/skills/li-human/` project-local):

```
python3 ~/.claude/skills/li-human/humanize.py draft.txt --report
python3 ~/.claude/skills/li-human/detect.py draft.txt
```

- `humanize.py` cleans zero-width/invisible characters, converts em-dashes and
  fancy typography, and removes the slop phrases listed in `li-human/slop.json`.
  `--report` prints what changed.
- `detect.py` scores the draft 0-100 across five checks: burstiness (sentence
  length variation), specificity (concrete detail), slop density, typographic
  fingerprint, and voice. Higher is better. `detect.py before.txt after.txt`
  proves the delta.

## What the score means (the bar for publishing)
`detect.py` returns one of three verdicts, and the rule is strict on purpose:

- **PASS** - overall >= 70 **and** every one of the five signals >= 55. Ship it.
- **REVIEW** - overall >= 50 but one signal is below 55. Fix that signal, not the average.
- **FLAGGED** - overall < 50. Rewrite.

The weakest signal drags the verdict, because a detector only needs one tell. An
overall of 67 with specificity at 48 still fails. The script exits non-zero unless
the verdict is PASS, so it can gate a pipeline.

The five signals: **burstiness** (sentence-length variation), **specificity**
(concrete, checkable detail), **slop density** (stock phrases), **fingerprint**
(invisible characters, em-dashes, curly quotes), **voice** (contractions, first
person). PASS means it reads as human. Whether the idea is worth posting is a
separate judgement, and that one is the author's.

## The second gate: reach.py
`detect.py` asks whether a draft reads as human. `reach.py` asks whether the feed
will carry it at all, which is the question that decides how many people ever see
the writing.

```
python3 ~/.claude/skills/li-human/reach.py draft.txt
```

It checks the mechanics, not the taste: hook length against the ~140 char mobile
cut, a link in the body (50-70% less reach), 150-300 words for dwell, 0-2
hashtags, a closing question, whether that question can be answered in one word,
and the rough read time. Under 2 seconds on a post is a scroll-past worth nothing,
8 seconds or more is a strong signal, so the aim is a post with room to get there. It exits non-zero while anything FAILS, so a
draft cannot quietly ship with a reach-killing mistake in it.

Run both. A post that passes `detect.py` and fails `reach.py` is well written and
will be seen by almost nobody.

## The third gate: claims.py
The first two gates do not care whether a word of the draft is true. A confident
wrong number passes both.

```
python3 ~/.claude/skills/li-human/claims.py draft.txt --sources research.txt
```

It cannot verify the world. It enforces something narrower and still useful: a
factual claim may not leave the draft unless the research actually contains it.
Every number in the post has to appear in the sources file, every named study or
company too, and **a number in a sentence about the author has to come from the
story bank**, because an invented personal metric is the easiest thing to write
and the hardest thing to take back.

This means the sources file exists **before** the draft. Paste the quotes and the
URLs while researching. If there is no sources file, the gate refuses to run,
which is the correct answer to drafting from memory.

## If Python is not available
Apply the same rules by hand: delete zero-width/invisible chars, turn every
em-dash into a comma or two sentences, strip the terms in `li-human/slop.json`,
and raise burstiness and concreteness.

## Tune it to one person
`li-human/slop.json` is editable. If it strips a word the author genuinely uses
(declared in `voice.md`), remove that word from `slop.json`. The voice file wins.

## Honest about limits
The scores are local heuristics, not GPTZero or Originality. They catch what
those tools key on; they do not promise their verdict. The point is a draft
that reads like a person wrote it, because one did.

## Preconditions
- A draft file exists. For `claims.py`, a sources file exists too.

## Done when (verify, do not assume)
- `detect.py` PASS: >=70 overall **and** no single signal under 55.
- `reach.py` CARRIES: zero FAIL rows.
- `claims.py` BACKED: zero unbacked claims.
- Any failure was fixed at the source and the gate re-run, not explained away in a caveat.
