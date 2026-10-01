---
name: li-router
description: The entry point. Reads a free-form request, works out which LinkedIn skill it is, checks that skill's preconditions are met, runs the chain in the right order, and refuses to report done until the gates pass. Use this when the request is not already a specific /li- command.
---

# li-router

Fifteen skills with nothing coordinating them is a pile, not a kit. This is the
layer that decides what to run, in what order, and whether it is actually
finished. Every other skill does one job and states what it needs; this one
routes and verifies.

## 1. Parse the intent
Map the request to a skill. When two fit, ask once rather than guessing.

| The request sounds like | Run |
|---|---|
| "write a post about X", an idea, a link to react to | `li-post` |
| "turn this into slides", a sequence, steps, a framework | `li-carousel` |
| "I have a video / article / transcript", one source, many posts | `li-repurpose` |
| "what do I reply to this post", someone else's post pasted | `li-comment` |
| "handle the comments on mine", a thread under her own post | `li-reply` |
| "reach out to", a connection request, outreach | `li-dm` |
| "sort my messages", an inbox dump | `li-inbox` |
| "look at my profile", headline, About, experience | `li-profile` |
| "what should I post this week", planning, calendar | `li-plan` |
| "why did that flop", analytics, what worked | `li-audit` |
| "I have nothing concrete to say", drafts full of placeholders | `li-interview` |
| "why did this post work", teardown of a winner | `li-hooks` |
| "who should I engage with" | `li-engagers` |
| "make the image", a card, a visual | `li-card` |
| "check this draft" | `li-human` |

## 2. Check preconditions before starting
Every skill declares what it needs. Do not start a skill whose preconditions
fail; say what is missing and fix that first.

- **`~/.claude/linkedin/voice.md` missing** - stop. Every writing skill reads it.
  Offer `templates/voice.md` or build it from three of her existing posts.
- **A writing task with no sources file** - research first. `claims.py` refuses
  to run without one, and that is the correct behaviour.
- **`li-audit` with no `log.md` and no analytics** - ask for the export or the
  numbers. Do not invent a post-mortem.
- **Drafts coming back with placeholders** - the story bank is empty. Route to
  `li-interview` before trying to write again.

## 3. Known chains
Some work is more than one skill, in a fixed order:

- **A post from scratch:** research -> `li-post` -> `li-card` -> three gates ->
  publish (her) -> log line -> `li-reply` during the first 60-90 minutes.
- **A post with no real material:** `li-interview` -> `li-post`.
- **A week:** `li-audit` -> `li-plan` -> `li-engagers` -> the post chain per slot.
- **A winner worth copying:** `li-hooks` -> `li-post` using the extracted template.
- **A long asset:** `li-repurpose` -> the post chain for each piece.

## 4. Verify before reporting done
A skill is finished when its own "Done when" block is satisfied, not when text
exists. For anything that produces a draft, that means all three gates:

```
python3 ~/.claude/skills/li-human/humanize.py draft.txt --report
python3 ~/.claude/skills/li-human/detect.py   draft.txt      # want PASS
python3 ~/.claude/skills/li-human/reach.py    draft.txt      # want CARRIES
python3 ~/.claude/skills/li-human/claims.py   draft.txt --sources research.txt
```

If any gate fails, fix the thing it names and run it again. Do not present a
draft and mention the failure as a caveat. A caveat is not a gate.

## 5. What this layer does not do
It does not write. It does not decide whether an idea is worth posting, and it
does not predict engagement. It routes, it checks, and it refuses to call
something finished when it is not.

## Hands off to
This layer starts the chain and stays out of the way. Hand the request to the
skill chosen in step 1, then follow that skill's own hand-off rather than
deciding again here.

## Preconditions
- The request has been read in full, including anything pasted with it.

## Done when (verify, do not assume)
- The chosen skill was named, and if two fit, she was asked rather than guessed for.
- Preconditions for that skill were checked, and anything missing was fixed first.
- The chain ran in order, and every skill's own "Done when" was satisfied.
- Nothing was reported finished on the strength of text existing.
