# Zero to Hired

[![tests](https://github.com/Wajee17/zero-to-hired/actions/workflows/tests.yml/badge.svg)](https://github.com/Wajee17/zero-to-hired/actions/workflows/tests.yml)

Learning machine learning and AI engineering from zero programming knowledge, in public.

I started with no programming background. This repository is the complete record of the work — every
lesson, every exercise, every failed attempt and every project — across a 58-week course from first
`print()` statement to job-ready ML/AI engineer.

I am keeping it public from day one, including the parts that are bad. The useful thing about a
learning repository is not the polish, it is the trajectory.

**Started:** November 2026 · **Target:** early 2028 · **Currently:** Week 0, setup

---

## Progress

| Phase | Weeks | Focus | Status |
|---|---|---|---|
| Phase 0 — Foundations | 1-3 | First programs, types, control flow, functions, dictionaries | Not started |
| Phase 1 — Core Python | 4-7 | Data model, containers, functions, errors, files, testing | Not started |
| Phase 2 — Real Python | 8-11 | OOP, iterators, generators, decorators, algorithms | Not started |
| Phase 3 — Data Stack | 12-16 | NumPy, pandas, Matplotlib, first models, **capstone** | Not started |
| Stage A — Maths | 17-21 | Linear algebra, calculus, probability, statistics, SQL | Not started |
| Stage B — Classical ML | 22-29 | Regression, classification, ensembles, feature engineering | Not started |
| Stage C — Deep Learning | 30-37 | Backprop, PyTorch, CNNs, sequences, attention, a small GPT | Not started |
| Stage D — LLMs | 38-42 | How LLMs work, APIs, embeddings, RAG, evaluation | Not started |
| Stage E — Agents | 43-48 | Agents, guardrails, fine-tuning, alignment | Not started |
| Stage F — Production | 49-52 | Serving, Docker, MLOps, specialisation | Not started |
| Stage G — Job Ready | 53-58 | Portfolio, interviews, system design, mock loop | Not started |

Detail lives in [`progress/PROGRESS.md`](progress/PROGRESS.md).

---

## Portfolio projects

The substantial work lives in its own repository, so each project can be read on its own terms.
They appear here as they are built.

| # | Project | Week | Repository |
|---|---|---|---|
| 0 | Python capstone — a tested, packaged data-analysis tool | 16 | _not yet_ |
| 1 | Tabular ML, end to end, with a served model | 29 | _not yet_ |
| 2 | Deep learning, with ablations and honest failure analysis | 37 | _not yet_ |
| 3 | An LLM application with a real evaluation suite | 47-48 | _not yet_ |
| 4 | Specialisation project — deployed and monitored | 51-52 | _not yet_ |

---

## How this repository is organised

```
part-1-python/      Weeks 0-16   one folder per week
part-2-ml-ai/       Weeks 17-58  one folder per week
problems/           The running log of practice problems and patterns
progress/           Where I actually am, updated every session
templates/          Starting points for a new week and a new project
tools/              new_week.py, which scaffolds the next week's folder
```

Each week folder holds the lesson work, the practice problems, the mini-project, and a README
covering what I learned, what I got wrong, and what I still find shaky. The "got wrong" sections are
the honest ones. They are the reason this is worth keeping.

To start a new week:

```bash
python tools/new_week.py 4 "The Data Model, Numbers and Text"
```

---

## The approach

The course this follows is mastery-based rather than coverage-based. A few things it enforces that
are worth stating, because they shape what you see here:

- **A topic is not finished when it has been explained.** It is finished when I can rebuild it from
  memory, apply it to something it was not taught on, and still have it four weeks later.
- **Build it from scratch, then use the library, then compare.** There is a lot of NumPy in here
  reimplementing things scikit-learn already does. That is the point.
- **Measured results only.** No claim about a model or a prompt without a number next to it, and no
  number without the code that produced it.
- **Old material never goes away.** Every session starts with questions on earlier weeks, chosen by
  spaced repetition. Concepts are only "done" after surviving several spaced reviews.

## On how this is taught

The curriculum is delivered by an AI tutor working from a fixed 58-week syllabus, three reference
textbooks per stage, and a strict set of rules about what counts as understanding. I am saying so
plainly because it shapes what this repository is: a structured course with enforced mastery gates
and spaced review, not a loose collection of tutorials.

The code here is mine. The tutor explains, questions, sets problems and refuses to move on until I
can demonstrate the idea without help — it does not write my solutions, by design.

## Notes

Code is Python 3.12+. Each week's folder is self-contained; where a week needs third-party packages
there is a `requirements.txt` beside it.

Anything in `data/` is gitignored. If an exercise needs a dataset, the README says where to get it.

---

*Wajeeh · [github.com/Wajee17](https://github.com/Wajee17)*
