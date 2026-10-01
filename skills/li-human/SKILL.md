---
name: li-human
description: Humanize a LinkedIn draft before anyone reads it. Runs two real scripts - humanize.py strips invisible characters, em-dashes and 100+ slop phrases, detect.py scores the draft on five human-vs-machine checks. Use on every post, comment or reply before showing it. Reads voice.md.
---

# li-human

The humanizer. Two scripts that actually run, in `tools/`. Run it, do not eyeball.

## Run it
From the kit root (or wherever you installed `tools/`):

```
python3 tools/humanize.py draft.txt --report
python3 tools/detect.py draft.txt
```

- `humanize.py` cleans zero-width/invisible characters, converts em-dashes and
  fancy typography, and removes the slop phrases listed in `tools/slop.json`.
  `--report` prints what changed.
- `detect.py` scores the draft 0-100 across five checks: burstiness (sentence
  length variation), specificity (concrete detail), slop density, typographic
  fingerprint, and voice. Higher is better. `detect.py before.txt after.txt`
  proves the delta.

## If Python is not available
Apply the same rules by hand: delete zero-width/invisible chars, turn every
em-dash into a comma or two sentences, strip the terms in `tools/slop.json`,
and raise burstiness and concreteness.

## Tune it to one person
`tools/slop.json` is editable. If it strips a word the author genuinely uses
(declared in `voice.md`), remove that word from `slop.json`. The voice file wins.

## Honest about limits
The scores are local heuristics, not GPTZero or Originality. They catch what
those tools key on; they do not promise their verdict. The point is a draft
that reads like a person wrote it, because one did.
