---
name: li-reply
description: Handle the thread under your own LinkedIn post. Sorts every comment into lead / substance / peer / support / noise, then writes replies in that order. Replies in the first hour drive reach. Reads voice.md.
---

# li-reply

The author pastes the comments under their post. You triage and reply in their
voice (`~/.claude/linkedin/voice.md`).

## Triage order (answer in this order)
1. **Lead** - a potential client, hire or collaborator. Answer first, move it
   forward (a question, an offer to talk).
2. **Substance** - a real technical point or counter-argument. Engage on merits.
3. **Peer** - a respected voice. Build the relationship, add something.
4. **Support** - genuine praise. A short, specific thank-you, not a like.
5. **Noise** - spam, pods, empty praise. Skip or a one-word acknowledgement.

## Rules
- The first 60 to 90 minutes decide more than the eventual total, and a reply
  from the author extends distribution on its own. Answer leads and substance in
  that window even if the reply is short.
- Write replies worth more than a nod. A comment over four words counts for more
  than a generic one, and that applies to yours as much as to theirs.
- Each reply earns its place: add, ask, or move it forward. No "Thanks!" alone.
- Keep the author's register. Run `li-human` on anything longer than a line.

## Output
A ranked list: each comment, its bucket, and the reply to paste.
