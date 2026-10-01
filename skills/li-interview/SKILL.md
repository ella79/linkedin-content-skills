---
name: li-interview
description: Interview the author and keep the answers in a Story Bank - real numbers, dated moments, scars, positions. Or ask five questions on one topic that end in a post spine. For when every draft comes back with {{your number}}.
---

# li-interview

Drafts come back with `{{your number}}` because the model has no real material.
This fixes the supply side: it interviews the author and banks what they say.

## Two modes

### 1. Fill the Story Bank
Ask focused questions, a few at a time, to fill `templates/story-bank.md`:
- Real numbers (dated, attributable, nothing rounded up or invented).
- Moments (small true scenes tellable in two lines).
- Scars (what went wrong, what changed).
- Positions (opinions the author will defend).
- Proof (links, repos, talks, shipped things).
Write the answers to `~/.claude/linkedin/story-bank.md`. Never put a number there
the author did not state.

### 2. Topic dig (ends in a post spine)
Ask five questions on one topic, then turn the answers into a **post spine**:
the hook candidate, the one idea, the anchor, the trade-off, the takeaway - ready
to hand to `li-post`.

## Rules
- Record only what the author actually says. No invented facts or numbers.
- Keep it private (the Story Bank is gitignored).

## Output
Mode 1: the questions, then the updated Story Bank section.
Mode 2: the five questions, then the filled post spine.

## Hands off to
-> `li-post`, carrying the post spine (hook candidate, one idea, anchor,
trade-off, takeaway) and any new story bank entries. The whole point of this
skill is that the next draft has real material, so do not stop at the answers.

## Preconditions
- Nothing. This skill exists precisely for when there is no material yet.

## Done when (verify, do not assume)
- Every line written to the story bank is something she actually said.
- No number appears that she did not state. Nothing inferred, nothing rounded up.
- In topic mode, the output is a usable post spine: hook candidate, one idea, anchor, trade-off, takeaway.
