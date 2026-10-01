---
name: li-dm
description: Write a connection and outreach sequence that does not read as a pitch - the invite note, the first message, and two follow-ups. Reads voice.md. Drafts only; you send them yourself.
---

# li-dm

Outreach that sounds like a person who did their homework, not a template.

## Inputs
Who the author wants to reach and why (one real reason), plus anything they know
about the person (a post, a shared interest, a mutual).

## The sequence
1. **Invite note** (<=200 characters): one specific reason you are connecting.
   Reference something real (a post, a project). No pitch in the invite.
2. **First message** (after they accept): give before you ask. A useful thought,
   a relevant link, or a genuine question. Still no pitch.
3. **Follow-up 1** (if no reply, ~4-7 days): add value again, a different angle.
   Make it easy to say yes or no.
4. **Follow-up 2** (final): a graceful close that leaves the door open. Two
   follow-ups, then stop. No third.

## Rules
- Personal and specific; if you cannot name a real reason, do not send it.
- The author's voice (`~/.claude/linkedin/voice.md`). Run `li-human`.
- Drafts only. The author sends them.

## Output
The four messages, copy-ready, with the suggested spacing.

## Preconditions
- A real, specific reason to contact this person exists. Without one, stop.
- `voice.md` exists.

## Done when (verify, do not assume)
- Invite note is <=200 characters and references something real about them.
- First message gives before it asks. No pitch.
- Exactly two follow-ups, with spacing, and the second closes gracefully.
- Nothing was sent. She sends them.
