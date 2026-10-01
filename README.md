# linkedin-content-skills

Sixteen Claude skills that run a LinkedIn presence from the draft side: write
posts, carousels, comments, replies and outreach, plan the week, audit what
shipped, and keep everything in your own voice. **Nothing posts to LinkedIn.**
Every skill produces copy-ready text you paste yourself.

Free and open source, for anyone who wants a serious LinkedIn workflow without
sounding like a template.

## What makes it different
- **Voice-agnostic.** The machinery is shared; your voice lives in one file
  (`voice.md`) that you fill in and keep private. Every skill reads it.
- **Three gates that run, not advice.** `detect.py` scores the draft on five
  human-vs-machine checks, `reach.py` checks what the feed actually penalises (hook
  length, dwell length, hashtags, a question that takes a yes), `claims.py` refuses
  any number that is not in your research file. `humanize.py` strips invisible
  characters, em-dashes and 100+ slop phrases before any of them run. A failing gate
  blocks the draft. It is not a caveat.
- **A router in front.** `li-router` works out which skill a request is, checks that
  skill's preconditions, runs the chain, and hands off to the next skill instead of
  leaving you to remember the order.
- **Grounded.** The writing skills research the web first and never invent
  numbers about you.
- **No auto-posting.** Drafts only. You stay in control of your account.
- **Every skill verifies itself.** Each one declares what it needs before it
  starts and what has to be true before it reports done, so finishing is a check
  rather than a feeling.
- **It learns from your account.** `li-audit` writes what actually worked to
  `learned.md`, and `li-post` and `li-plan` read it before drafting, so evidence
  from your own numbers outranks generic advice and the cheat-sheet.
- **It will not repeat you.** Every post and carousel checks the log of what you
  already published and refuses to re-argue the same thesis. Publishing writes the
  log back, which is also what the audit reads.

## The skills
| Command | What it does |
|---|---|
| `li-router` | The entry point. Works out which skill a request is, checks its preconditions, runs the chain, verifies before calling it done. |
| `li-post` | One idea into a post. 3 hook options from 21 formulas, one draft, humanized. |
| `li-carousel` | Document posts. Slide-by-slide copy, a cover that earns the swipe, a PDF. |
| `li-repurpose` | One video, article or transcript into 4-6 posts that each stand alone. |
| `li-comment` | Comments on others' posts, picked by what the post is. Never "Great post!". |
| `li-reply` | The thread under your post, sorted lead / substance / peer / support / noise. |
| `li-dm` | A connection + outreach sequence: invite note, first message, two follow-ups. |
| `li-inbox` | Triages the inbox into lead / recruiter / peer / ask / spam, with the tell. |
| `li-profile` | Scores your profile on a 12-part rubric, rewrites in fix-first order. |
| `li-plan` | The week: what to post, when, and who to engage with. |
| `li-audit` | Post-mortem on what you published, ranked by engagement rate, not impressions. |
| `li-interview` | Interviews you into a Story Bank so drafts stop saying `{{your number}}`. |
| `li-hooks` | Takes apart a post that worked: formula, build, why, a blank template. |
| `li-engagers` | The ~10 people and posts worth a real comment this week. |
| `li-card` | The post image, at the size the feed rewards. Portrait 1080x1350, stat / quote / terminal layouts. |
| `li-human` | Three gates that run: `detect.py` human enough, `reach.py` will the feed carry it, `claims.py` is any of it backed. |

## Install
Copy the skills into Claude Code, global or project-local.

Global (available in every Claude Code session, no project needed - you can
delete the clone afterwards):
```bash
git clone https://github.com/ella79/linkedin-content-skills.git
cp -r linkedin-content-skills/skills/li-* ~/.claude/skills/
```
The scripts live inside the skill folders that use them, so they come along with the
copy: the four gates in `skills/li-human/`, the image renderer in `skills/li-card/`.
Nothing else to wire up.

Project-local: copy the same `skills/li-*` folders into your repo's
`.claude/skills/`.

No Claude Code at all? Paste any single `SKILL.md` at the top of a chat and it
runs as a mode. You lose the Python scripts (most of the point of `li-human`),
but the rest works.

## Then spend ten minutes on your voice
```bash
cp templates/voice.md ~/.claude/linkedin/voice.md
cp templates/story-bank.md ~/.claude/linkedin/story-bank.md
```
Fill `voice.md` in, or paste three of your own posts into Claude and say
"write my voice.md from these". Every skill reads that file. Skip it and
everything comes out sounding like everyone else.

**Your topics live there too.** Set what you post about in the "Topics I post
about" section of `voice.md`; `li-post`, `li-plan` and `li-hooks` read that list.
The repo ships only a blank template, so your topics stay in your private copy.

**Your voice stays yours.** The filled `voice.md` and `story-bank.md` live under
`~/.claude/linkedin/` and are gitignored here, so they never end up in a public
repo. The repo ships only blank templates.

## Requirements
- Python 3 for the four `li-human` scripts (`humanize.py`, `detect.py`, `reach.py`,
  `claims.py`). Standard library only.
- Pillow for `skills/li-card/card.py`, which renders the post image:
  `pip install pillow`. Everything else works without it.
- Claude Code to run the skills as commands (optional, see above).

## No publishing step, on purpose
This kit has no auto-post. Automating posts to a personal profile without your
per-post go-ahead is against LinkedIn's User Agreement, and the point here is a
draft good enough that you are happy to paste it yourself.

## Credits
The idea and the humanizer approach build on
[nessalazne/linkedin-agent-skill](https://github.com/nessalazne/linkedin-agent-skill)
(a fork of Jakeschincariol's work, MIT). This kit is an independent rebuild:
voice-agnostic, grounded-first, no publishing step, with the scripts and skill
prompts rewritten.

## License
MIT. See [LICENSE](LICENSE).
