# Git and GitHub, Learned by Doing

**Git** tracks changes to your files on your computer. **GitHub** hosts your Git repositories online so others (including employers) can see them. You'll use both every day.

## Part 1: First repo (Phase 1, day 1)

One-time setup:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Turn this folder into a repo:

```bash
cd ai-engineer-roadmap
git init
git add .
git status                 # check that .env is NOT listed
git commit -m "Initial commit: roadmap scaffold"
```

Create an empty repo on github.com (New repository, no README, no .gitignore), then connect and push:

```bash
git remote add origin https://github.com/<your-username>/ai-engineer-roadmap.git
git branch -M main
git push -u origin main
```

GitHub will ask you to sign in. Use the browser flow or a personal access token, or install the GitHub CLI (`gh auth login`), which is the easiest route.

## Part 2: The daily loop

```bash
git status                       # what changed?
git add phase-1-python/exercises.py
git commit -m "Implement word_count and top_n"
git push
```

Good commit messages are short and say what changed: "Add pandas cleaning step for ticket dates", not "stuff" or "update". Commit when one small thing works. Several small commits beat one huge one.

Useful checks:

```bash
git log --oneline                # history
git diff                         # unstaged changes
git diff --staged                # what the next commit will contain
```

## Part 3: Branches and pull requests (Phase 2)

A branch is a safe copy to work on. A pull request (PR) asks to merge it into `main`. Even working alone, use PRs: it's the workflow every team uses and it's good practice.

```bash
git switch -c feature/ticket-analysis     # create and move to a branch
# ...work, commit...
git push -u origin feature/ticket-analysis
```

On GitHub, click "Compare & pull request", write what changed and why, then merge it. Back locally:

```bash
git switch main
git pull
git branch -d feature/ticket-analysis
```

Also start using **Issues**: write one per task ("Add confusion matrix to classifier"). Close them with commit messages like `Fixes #4`.

## Part 4: Secrets and mistakes (Phase 3)

- Put API keys in `.env`. It is in `.gitignore`. Only `.env.example` (with fake values) is committed.
- If you ever push a real key, **revoke it immediately** at the provider and create a new one. Deleting the commit is not enough because the key stays in history.

Undoing things:

| Situation | Command |
|---|---|
| Discard edits to a file you haven't committed | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Undo a commit that's already pushed (safe) | `git revert <commit-hash>` |
| Fix the last commit message (not yet pushed) | `git commit --amend` |

Avoid `git reset --hard` and force-pushing until you understand them. They can destroy work.

## Part 5: Automation with GitHub Actions (Phase 5)

When your Phase 1 exercises pass locally, move the CI template into place:

```bash
mkdir -p .github/workflows
cp docs/templates/tests.yml .github/workflows/tests.yml
git add .github && git commit -m "Add CI: run pytest on push" && git push
```

Now every push runs your tests on GitHub. A green check on your repo is a small but real credibility signal. To use an API key in a workflow, add it under Settings > Secrets and variables > Actions. Never write it in the YAML file.

## Part 6: Collaboration (Phases 6-7)

- **Fork** a small open-source project, fix a typo or documentation gap, and open a PR. Search GitHub for issues labelled `good first issue` or `documentation`.
- **Review your own PRs** before merging: read the diff and ask "would a stranger understand this?"
- Use a **Project board** (GitHub Projects) to track the four portfolio projects.

## Part 7: Make your profile hireable (Phase 8)

1. Create a repo named exactly like your username. Its README becomes your profile page: who you are, what you're building, links to your best projects.
2. Pin your 4 best repos.
3. Each project README needs: what it does, a demo screenshot or GIF, how to run it in under 5 commands, what you learned, known limitations.
4. Tag a release (`git tag v1.0.0 && git push --tags`) on finished projects.
5. Fill in your GitHub bio and link your LinkedIn.

## Common problems

- **"Permission denied" or authentication failed on push**: re-run `gh auth login`, or create a personal access token.
- **"Updates were rejected"**: someone (maybe you, on github.com) changed the remote. Run `git pull`, resolve any conflict, then push.
- **Merge conflict**: open the file, find the `<<<<<<<` markers, keep the right lines, delete the markers, then `git add` and `git commit`.
- **Committed a big file by mistake**: ask for help before pushing. It's easier to fix before the push.

## Practice resources

- GitHub Skills (skills.github.com): short interactive courses that run inside GitHub.
- Pro Git book (git-scm.com/book): free, the reference.
