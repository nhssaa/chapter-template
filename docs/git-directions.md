# Git directions for your chapter (and your AI)

These are written so you can paste them straight to your AI assistant. It will walk you through each step on your machine.

## One-time setup

1. On GitHub, open `nhssaa/chapter-template` and click "Use this template" to create your chapter repo. Name it after your school club, e.g. `briarcliff-sports-analytics`.
2. Ask your AI: "Help me clone the repo <your-repo-url> to this computer and set up Python with pandas."
3. Work in a branch, never directly on main. Ask your AI: "Create a branch called meeting-01 and switch to it."

## Every meeting

1. "Show me what changed with git status and git diff."
2. "Commit these changes with a message that says what we did in ten words or fewer."
3. "Push this branch to GitHub."

## Sharing something upstream (when it is finished and tested)

1. Fork `nhssaa/club-resources` on GitHub.
2. Ask your AI: "Add my finished <lesson/script> from <your-repo> into my fork of nhssaa/club-resources in the right folder, then open a pull request."
3. The pull request gets automated checks (secrets, personal data, size, attribution) and the NHSSAA review agent will ask what it does, how you tested it, and what data it uses. Answer in the PR comments.
4. A member of the NHSSAA core team reviews and merges. The agent never merges.

## Rules your AI must follow too

- No personal information in code, data, comments or commit messages.
- No secrets or API keys. If one is ever committed, tell the NHSSAA team at info@nhssaa.org immediately.
- If the AI writes code, you run it before you share it.
