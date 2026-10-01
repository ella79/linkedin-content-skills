---
name: li-inbox
description: Triage your LinkedIn inbox into lead / recruiter / peer / ask / spam, say which tell gave each away, and draft the reply that fits. Reads voice.md. You paste the messages; never scrape.
---

# li-inbox

The author pastes their messages (never scrape). You sort and draft replies in
their voice (`~/.claude/linkedin/voice.md`).

## Buckets
- **Lead** - a real opportunity (client, collaboration, role worth a look).
- **Recruiter** - a role pitch. Worth a reply even when declining, politely.
- **Peer** - someone in the field building a relationship.
- **Ask** - wants your time or help for free.
- **Spam** - pods, mass outreach, pitch-slaps.

For each, name the **tell** that classified it (the phrase or pattern), so the
author learns to read them too.

## Replies
- Lead: move it forward (a question, or a time to talk).
- Recruiter: a clear yes-with-questions or a gracious no with your criteria.
- Peer: warm, specific, one thing to continue on.
- Ask: a boundary that is still kind (a pointer, a link, or a clear no).
- Spam: ignore, or one line if it is borderline.

## Output
A table: message summary, bucket, the tell, and the reply to paste. Run
`li-human` on anything longer than a line.

## Hands off to
-> `li-dm` for any lead that needs a real sequence rather than a single reply.
Everything else ends here, with drafts she sends herself.

## Preconditions
- The messages are pasted. Never scraped.
- `voice.md` exists.

## Done when (verify, do not assume)
- Every message is bucketed, and **the tell that classified it is named**, so she learns the pattern.
- Each bucket got the reply that fits it, including a kind boundary for asks.
- Nothing was sent.
