# NHSSAA chapter template

Start your chapter's repo from this template (green "Use this template" button), then make it yours. Your chapter repo is yours: experiment there freely. When something is finished, tested and worth sharing with every chapter, contribute it upstream to [nhssaa/club-resources](https://github.com/nhssaa/club-resources) with a pull request.

## What is in here

- `docs/data-sources.md` - free, legal datasets for sports analytics meetings.
- `docs/git-directions.md` - basic git directions, written so you can paste them to your AI assistant.
- `starters/first_model.py` - a tiny first model that runs in a browser or any Python.
- `CONTRIBUTING.md` - how upstream contributions work.

## House rules (they protect you)

1. Never put personal information in any repo: no student full names, emails, phone numbers, addresses. School name + first name is the most that should ever appear, and prefer none.
2. Never commit secrets: no passwords, API keys, tokens. `.gitignore` blocks the common ones; if one slips in, tell the NHSSAA team immediately.
3. Data does not live in git. Link to datasets (see `docs/data-sources.md`); keep anything large out of the repo.
4. Test before you share. Run your code end to end on a fresh copy before opening a pull request upstream.
5. Give credit: note where data and ideas came from.

## A weekly rhythm that works

1. Pick one small question ("do shots from closer go in more?").
2. Get one dataset from `docs/data-sources.md`.
3. Spend the meeting answering it in a notebook or script.
4. Commit what you made to your chapter repo.
5. When something is genuinely reusable, open a pull request to `nhssaa/club-resources`.
