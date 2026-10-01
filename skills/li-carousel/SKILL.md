---
name: li-carousel
description: Turn an idea with sequence into a LinkedIn document post (carousel), the highest-dwell format. 8-12 slides, a cover that earns the swipe, one idea per slide, and the PDF to upload. Reads voice.md. Researches first.
---

# li-carousel

For ideas that have a sequence: steps, before/after, a framework. If the idea is
a single claim, it is a text post (`li-post`), not a carousel.

## Structure (8-12 slides)
- **Slide 1, cover:** the hook in <=6 words plus one promise. It earns the swipe.
- **Slide 2:** the stake - why this matters, who it is for.
- **Slides 3..N:** one idea per slide. A 3-7 word headline, <=25 words of body.
- **Last slide:** one CTA (follow, comment a keyword, read the full post).

## Rules
- Research the web first; cite sources in the post body under the carousel.
- One idea per slide; if a slide needs two, split it.
- Voice from `~/.claude/linkedin/voice.md`; real anchors from `story-bank.md`.
- Run `li-human` on the slide copy and the caption.
- Check `~/.claude/linkedin/log.md` first: do not rebuild a carousel around a
  thesis the author already published.
- After publishing, append the log line (date, slug, topic, hook formula, URL).
- Keep links out of the caption; put them in the first comment. Slides are 1080x1350.

## Output
1. Slide-by-slide copy (numbered).
2. The post caption (hook + context + sources).
3. A PDF to upload (build it from the slide copy; 1080x1350 portrait works well).

## Hands off to
-> `li-card` for the slides and the PDF at 1080x1350.
-> `li-human` for the caption gates.
-> she publishes, log line, then `li-reply` in the first 60 to 90 minutes.

## Preconditions
- `voice.md` exists. The idea genuinely has a sequence; a single claim is a text post.
- Research done and written to a sources file.

## Done when (verify, do not assume)
- Cover slide states the hook in <=6 words plus one promise.
- Every slide carries exactly one idea, headline <=7 words, body <=25 words.
- The caption passes the three gates, and carries no link.
- A PDF exists at 1080x1350, not just slide text.
