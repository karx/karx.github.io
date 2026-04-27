---
published: true
title: "Advanced Git Workflows"
tags:
  - git
  - devops
  - engineering
  - version-control
description: "Comprehensive reference on Git branching strategies, rebase vs merge philosophy, and advanced operational mechanisms — from GitFlow to Trunk-Based Development."
---

Git's flexibility is its greatest liability. Without explicit workflow discipline, teams descend into merge hell. The selection of branching strategy, history philosophy, and advanced tooling fundamentally defines delivery velocity.

---

## 1. THE FOUR WORKFLOW PARADIGMS

| Workflow | Integration Frequency | Best For | Key Mechanism |
|---|---|---|---|
| **GitFlow** | Low (end of cycle) | Versioned/on-premise software | `--no-ff` merges, 5 branch types |
| **GitHub Flow** | High | SaaS / continuous deployment | Short-lived branches + PRs |
| **GitLab Flow** | Medium–High | Staging/production gating | Downstream environment branches |
| **Trunk-Based Dev** | Multiple times daily | DevOps-mature CI/CD teams | Feature flags + micro-commits |

### GitFlow (Vincent Driessen, 2010)
- Two infinite branches: `master` (production tags) + `develop` (integration)
- Three temporary types: `feature/` (from develop), `release/` (→ master + develop), `hotfix/` (from master only)
- Rule: **always `--no-ff`** — forces a merge commit even when fast-forward is possible, preserving branch topology for bulk revert
- Fatal flaw: structurally incompatible with CI/CD. Long-lived branches create code drift → merge hell

### GitHub Flow
1. Branch from `main` with a descriptive name
2. Push commits frequently for visibility
3. Open PR for review + CI checks
4. Merge to `main` → deploy immediately
5. Delete the branch

### GitLab Flow
- Code flows **downstream only**: `main` → staging → pre-production → production
- Never rebase shared/public branches — it silently invalidates prior CI test results
- If a merged branch is reverted and later reinstated: **revert the revert** (do not re-merge the original branch — Git already recorded those commit hashes as integrated)

### Trunk-Based Development
Requires:
1. **True CI** — daily integration eliminates code drift entirely
2. **Feature Flags** — decouple deployment from release; enable canary rollouts; instant rollback without Git operations
3. **Branch by Abstraction** — large refactors inline on trunk via abstraction layer, no long-lived branch needed

---

## 2. REBASE vs MERGE

The philosophical split: **authentic history** vs **curated history**.

| Philosophy | Command | Graph Shape | Cultural Archetype |
|---|---|---|---|
| Authenticity | `git merge` | Nonlinear, branching | Linux kernel, open-source maintainers |
| Curation | `git rebase` | Strictly linear | High-velocity product teams |

### The Golden Rule
- **Rebase privately** — local cleanup before opening a PR is expected and professional
- **Merge publicly** — rebasing shared branches rewrites SHA hashes, creating divergent parallel histories with no reconciliation path

### `git rebase -i` (interactive)
- `pick` — keep commit
- `squash` — meld into previous commit, keep both messages
- `fixup` — meld silently (discard message)
- `reword` — change message only
- `drop` — remove commit entirely

### Autosquash workflow
```bash
git commit --fixup <hash>          # creates "fixup! <original message>"
git rebase -i --autosquash <base>  # auto-reorders + pre-configures fixup! entries
```
Extended: `--fixup=amend:<hash>` and `--fixup=reword:<hash>` for async log message editing.

---

## 3. FORCE-PUSH SAFETY: CAS PATTERN

Every Git safety mechanism is a **compare-and-swap** variant: validate expected state before writing.

```
git push --force                    ← blind overwrite, EXTREME risk
git push --force-with-lease         ← CAS against remote tracking hash, LOW risk
git push --force-with-lease \
         --force-if-includes        ← CAS + ancestry check, NEAR-ZERO risk
```

### The Background Fetch Vulnerability
`--force-with-lease` checks the expected hash against `refs/remotes/origin/<branch>`. If an IDE (VS Code, IntelliJ) silently runs `git fetch`, that tracking hash updates — making the lease check pass even though the developer never reviewed the fetched changes. Collaborator commits are destroyed with no warning.

`--force-if-includes` closes this: it verifies the remote tracking commit is a **physical ancestor** of the local branch, not just a matching hash in the object database.

---

## 4. ADVANCED OPERATIONS

### `git add --patch` (`-p`)
Segments file changes into hunks for surgical staging. Enforces atomic commit discipline.
- `y` — stage hunk
- `n` — skip
- `s` — split into smaller hunks
- `e` — open editor to manually modify the diff

### `git worktree`
Multiple working directories attached to one `.git` database. All worktrees share the same packfiles and remote-tracking refs — a `fetch` in one updates all.

Use case: urgent hotfix on `master` while deep in a feature branch — no stash, no clone, no disruption.
```bash
git worktree add ../hotfix master
# fix, test, push
git worktree remove ../hotfix
```

### `git reset` — The Three Trees
| Mode | HEAD | Index | Working Dir | Use When |
|---|---|---|---|---|
| `--soft` | ✓ | — | — | Recommit multiple commits as one |
| `--mixed` | ✓ | ✓ | — | Unstage everything, keep changes (default) |
| `--hard` | ✓ | ✓ | ✓ | **Destructive** — permanently discards work |

`git restore <file>` — discard unstaged changes
`git restore --staged <file>` — unstage without touching the file

`git revert <commit>` — creates a new forward commit with the inverse diff. The only safe undo for public history.

---

## 5. FORENSICS & RECOVERY

### `git reflog`
Local sequential ledger of every HEAD movement. The escape hatch after a catastrophic `reset --hard` — orphaned commits survive in the object store for **90 days** before GC.
```bash
git reflog show HEAD              # list all movements
git reset --hard HEAD@{3}         # jump back 3 operations
```

### `git rerere` (Reuse Recorded Resolution)
Enable: `git config --global rerere.enabled true`
- On conflict: Git fingerprints the preimage → stores in `.git/rr-cache/`
- On resolution: stores the postimage
- On identical future conflict: auto-applies the postimage (leaves files unstaged for review)
- Cache prune: resolved after 60 days, unresolved after 15 days
- Shareable: commit `.git/rr-cache/` to distribute across the team

### `git bisect`
Binary search over the commit DAG. O(log N) complexity — 1,000 commits isolated in ≤10 steps.
```bash
git bisect start
git bisect bad                    # current commit is broken
git bisect good v2.3.0            # known-good baseline
# Git checks out midpoint, you test and mark good/bad
git bisect reset                  # restore HEAD when done

# Fully automated:
git bisect run npm test           # script exit 0 = good, non-zero = bad
```

### Advanced `git log`
```bash
git log --graph --oneline --decorate --all          # DAG topology as ASCII
git log -S"functionName"                            # pickaxe: when did this string appear/disappear?
git log -G"regex"                                   # regex search across all historical diffs
git log --since="2.weeks" --author="karx"           # temporal + attributional filter
git log --pretty=format:"%h%x09%an%x09%ad%x09%s"   # machine-readable: hash, author, date, subject
```

---

## 6. KEY INSIGHTS

1. **GitFlow is contraindicated for CI/CD** — not just suboptimal, structurally prevents it
2. **Feature flags decouple deployment from release** — the primary unlock for TBD at any team size
3. **Rebase rewrites SHA hashes** — on shared branches this creates divergent histories with no auto-reconciliation
4. **`--force-with-lease` has a silent failure mode** — IDE background fetches make it as dangerous as `--force`
5. **Every advanced safety tool is CAS** — force-with-lease, rerere fingerprinting, bisect partitioning all follow the same "validate state before writing" pattern

---

## Related
[[kaaroCatalogue]] · [[computeTheory]] · [[Github Actions]] · [[kaaroViewer]]
