# linkedin-content-skills

Fourteen Claude skills that run a LinkedIn presence from the draft side: write
posts, carousels, comments, replies and outreach, plan the week, audit what
shipped, and keep everything in your own voice. **Nothing posts to LinkedIn.**
Every skill produces copy-ready text you paste yourself.

Free and open source, for anyone who wants a serious LinkedIn workflow without
sounding like a template.

## What makes it different
- **Voice-agnostic.** The machinery is shared; your voice lives in one file
  (`voice.md`) that you fill in and keep private. Every skill reads it.
- **A real humanizer.** Two scripts that actually run (`tools/humanize.py`,
  `tools/detect.py`) strip invisible characters, em-dashes and 100+ slop phrases,
  and score the draft on five human-vs-machine checks. Not vibes.
- **Grounded.** The writing skills research the web first and never invent
  numbers about you.
- **No auto-posting.** Drafts only. You stay in control of your account.

## The skills
| Command | What it does |
|---|---|
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
| `li-human` | The humanizer. Two scripts that run. Used by every writing skill. |

## Install
Copy the skills into Claude Code, global or project-local.

Global:
```bash
git clone https://github.com/ella79/linkedin-content-skills.git
cp -r linkedin-content-skills/skills/li-* ~/.claude/skills/
cp -r linkedin-content-skills/tools ~/.claude/linkedin-tools   # keep the scripts together
```

Project-local: copy the same `skills/li-*` folders into your repo's
`.claude/skills/`.

No Claude Code at all? Paste any single `SKILL.md` at the top of a chat and it
runs as a mode. You lose the two Python tools (most of the point of `li-human`),
but the rest works.

## Then spend ten minutes on your voice
```bash
cp templates/voice.md ~/.claude/linkedin/voice.md
cp templates/story-bank.md ~/.claude/linkedin/story-bank.md
```
Fill `voice.md` in, or paste three of your own posts into Claude and say
"write my voice.md from these". Every skill reads that file. Skip it and
everything comes out sounding like everyone else.

**Your voice stays yours.** The filled `voice.md` and `story-bank.md` live under
`~/.claude/linkedin/` and are gitignored here, so they never end up in a public
repo. The repo ships only blank templates.

## Requirements
- Python 3 for `tools/humanize.py` and `tools/detect.py` (standard library only).
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
