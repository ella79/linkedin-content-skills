---
name: li-post
description: Turn one idea into a LinkedIn post. Researches the web first, checks the log so it never re-argues a post you already published, writes a 5-second hook with three alternatives from a 21-formula cheat-sheet, one full draft, humanized before you see it. Reads voice.md and story-bank.md. Never auto-posts.
---

# li-post

One idea, one post, copy-ready. Reads `~/.claude/linkedin/voice.md` for who you
are, who you write for, and your rules. If `voice.md` is missing, say so and ask
the author to fill `templates/voice.md` first; do not invent a voice.

## Non-negotiables
- Research the web FIRST, before proposing the topic. Never draft from memory.
  Gather current, precise facts and cite 1-3 real links (prefer primary docs).
  If a fact cannot be verified live, leave it out. Never invent anything.
- Never invent metrics about the author. Industry stats only with attribution.
- Write in the language and register declared in `voice.md` (English by default).
- Never auto-post. Deliver copy-ready text the author pastes themselves.
- Never re-argue a post the author already published. Before drafting, read the
  last ~10 entries in `~/.claude/linkedin/log.md` (and anything the author pastes).
  If the thesis, the anchor or a line repeats, pick a different angle and say so.
  If `log.md` does not exist yet, say so and ask the author for their last few
  posts before drafting. Do not assume the slate is clean.

## Hook (the 5-second test)
LinkedIn shows ~210 characters on desktop, ~140 on mobile before "see more", so
line 1 must survive alone.
- One punchy line, not two. Contrarian claim, a sharp fact, a short real moment,
  or one line of code that stops the target reader.
- No throat-clearing. Line 2 is the payoff of line 1, not setup.
- Use `li-human/hooks.json` (21 formulas, each with template, example, purpose, and
  how it usually gets ruined). Rotate formulas; do not reuse the last one.
- Always give 2-3 alternative hooks: at least one broad, one sharper/technical.

## Draft shape
Hook, then 3-6 short points or a tight narrative, an honest "where it is not
magic" note when relevant, a takeaway the reader can act on, one soft question
as CTA. Dense bullets go below the fold.

## Distribution rules (how the feed actually treats a post)
These are mechanics, not style. Breaking them costs reach no matter how good the
writing is.

- **No link in the body. Ever.** A post with an external link reaches 50-70% fewer
  people. Put the URL in a separate first comment and deliver that comment text
  alongside the post, so the author pastes it right after publishing.
- **150-300 words.** Long enough to earn the "see more" click, short enough to be
  read. Dwell time carries the most weight of any ranking signal.
- **The target is 8 seconds, not 5.** Under 2 seconds on a post is a scroll-past
  and scores nothing at all. 3 to 8 seconds is a mild positive. Past 8 seconds the
  signal turns strong. The hook stops the scroll; what holds someone past the
  "see more" is structure, so give the opening a reason to expand and put the
  payoff below the fold, not above it.
- **Velocity beats volume.** Reactions and comments inside the first 60 to 90
  minutes matter more than the eventual total, and the author's own replies extend
  distribution further. Plan to be present for that window, not just to publish.
- **Ask something that cannot be answered in one word.** A comment over four words
  counts for more than a generic one, so close on what/how/why rather than a
  question that takes a yes.
- **0-2 hashtags.** They test identical to 5+, so they buy nothing. Never a wall.
- **Image, when there is one: 1080x1350 (4:5) or 1080x1080.** Portrait and square
  fill far more of a phone screen than landscape, and screen time is dwell time.
  1200x627 is the link-preview spec, not the feed-upload spec.
- **Build the image with `li-card`**, which renders at the documented sizes and
  offers a stat, quote or terminal composition. Pick the one this post needs and
  never the one used last time. Often the strongest image is a real artefact,
  terminal output or a failing test, because a designed card can read as
  marketing and a technical reader discounts marketing.
- **The first 30 minutes decide the ceiling.** The post goes to roughly 2-5% of the
  network first and only expands if 5-10% of them engage. Deliver a short golden
  hour plan with every post: when to publish, and two or three posts to comment on
  first (see `li-engagers`), so the author is visible when the window is open.

## Quality bar (aim 10/10)
Substantive, specific, worth the target reader's time. Technically credible:
real tools, real mechanisms, correct terms. Human but professional. One clear
idea, a concrete anchor (from `story-bank.md` when numbers are needed), an
honest trade-off. If a draft is a 7 or 8, revise before showing it.

## Steps
1. Pick/confirm a topic from `voice.md` (rotate; not the last one).
2. Read `~/.claude/linkedin/learned.md` if it exists. It holds what `li-audit`
   found actually worked on this account: hook formulas that landed, topics that
   did not, things to stop. Prefer what the evidence supports over what the
   cheat-sheet suggests, and say which finding you leaned on.
3. Research the web first. Write what you find into a sources file as you go,
   quotes and URLs, because gate three reads it. Note 1-3 links to cite.
4. Draft per the shape above.
5. Self-check against the quality bar; revise if under 10/10.
6. Run `li-human`, all three gates, all mandatory:
   `humanize.py` and `detect.py` until it reads clean, `reach.py` until nothing
   FAILS, and `claims.py --sources` until nothing is UNBACKED. Reporting a draft as
   ready without running them is not allowed. None of them predicts engagement:
   two remove the reasons a post gets buried or spotted, and the third stops an
   unbacked number going out under the author's name.
7. Deliver: the post, 2-3 alternative hooks, and a "Sources:" list.
8. After the author publishes, append one line to `~/.claude/linkedin/log.md`:
   date, title/slug, topic, the hook formula used, and the post URL. That log is
   what `li-audit` reads and what step 2 of the next post checks against.

## Output
Return (1) the post, copy-ready; (2) the **first comment** text carrying the link
and sources, to paste immediately after publishing; (3) 2-3 alternative hooks
(broad + technical); (4) a two-line golden hour plan; (5) Sources as markdown
links. No em-dash in the body. Keep the post itself to 150-300 words.

## Hands off to
-> `li-card` for the image, which needs the finished text so it can carry the
claim rather than decorate it.
-> `li-human` for all three gates. Nothing leaves before they pass.
-> she publishes, then the log line is appended, then
-> `li-reply` for the first 60 to 90 minutes, which is where velocity is won.

## Preconditions
- `~/.claude/linkedin/voice.md` exists and is filled in.
- A sources file exists, written during research, before any drafting.
- `log.md` has been read, or the author has been asked what she published lately.

## Done when (verify, do not assume)
- `detect.py` returns PASS, `reach.py` returns CARRIES, `claims.py` returns BACKED.
- The thesis does not repeat anything in the last ~10 log entries.
- The first-comment text exists and holds every link the post would have carried.
- 2-3 alternative hooks delivered, at least one broad and one technical.
- Nothing was published. The output is text for her to paste.
