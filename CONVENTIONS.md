# Conventions

Rules for myself, so the repository stays readable when there are 58 weeks in it.

## Committing

**Commit at the end of every lesson, even when the work is small or wrong.** The value of this
repository is the trajectory, and a trajectory needs points. A week that appears as one large commit
on Sunday tells a reader nothing.

Commit messages follow `area: what changed`, in the imperative:

```
week-04: add aliasing and deep-copy exercises
week-04: fix off-by-one in slice_window
week-07: mini-project — CLI expense tracker, first working version
problems: add Two Sum, hash map approach, 1 hint
progress: week 4 checkpoint 86/100
```

Keep the subject under about 70 characters. If a commit needs explaining, put it in the body — what
was tried, what broke, why this fix. Future me is the main reader and has forgotten everything.

Never commit: API keys, `.env` files, datasets, model weights, virtualenvs. The `.gitignore` covers
these, but check `git status` before committing rather than trusting it blindly.

## Folder naming

```
part-1-python/week-04-data-model-numbers-text/
part-2-ml-ai/week-24-classification-metrics/
```

Lowercase, hyphens, zero-padded week number, short descriptive slug. Inside a week:

```
week-04-data-model-numbers-text/
├── README.md         what I learned, what I got wrong, what is still shaky
├── lessons/          code written during the three lessons
├── problems/         the practice problems, one file each
├── mini-project/     the end-of-week build
└── requirements.txt  only if the week needs packages
```

Create it with `python tools/new_week.py 4 "The Data Model, Numbers and Text"` rather than by hand.

## Code

- Python 3.12+, PEP 8, four-space indent, `snake_case`.
- Meaningful names. `n` and `i` are fine in a loop; `data2` is not fine anywhere.
- A docstring on anything non-obvious, saying what it does and what it assumes.
- Type hints from Week 9 onward, once they have been taught.
- Tests with `pytest` from Week 7 onward, in a `tests/` folder beside the code.

Solutions to practice problems carry a short header comment: the approach, the time and space
complexity, and how many hints were needed. The hint count matters — it is how I find the patterns I
am still weak on.

```python
"""Two Sum — hash map, O(n) time, O(n) space. 1 hint (nudged toward a dict)."""
```

## READMEs

Every week gets one, written the same day, not retroactively. Four sections:

1. **What this week covered** — three or four lines, in my own words, not copied from the syllabus.
2. **What I got wrong** — the actual mistakes. This is the most useful section in the whole repo.
3. **Still shaky** — what I would fail a question on right now.
4. **Checkpoint** — the score, and what the weak sections were.

Write section 2 honestly. A learning repository where nothing ever goes wrong is not believable, and
more importantly it is useless to me when I come back to revise.

## Portfolio projects

Projects get their own repository, not a folder here. When a project repo exists, link it from the
table in the root README. The week folder keeps only planning notes and a link.

A project repo is finished when it has: a README with the problem, the approach, the measured
results and the limitations; reproducible setup; tests; and an honest section on what did not work.
