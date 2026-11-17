# Week 3 — Functions, Dictionaries and Problem Solving

16 Nov 2026 – 22 Nov 2026

## What this week covered

<!-- Three or four lines in your own words. Not the syllabus. If you cannot write this without
     looking it up, that is the first useful signal of the week. -->

## What I got wrong

<!-- The actual mistakes, with enough detail to be useful in six months.

     Good:  Assumed `list.sort()` returned the sorted list. It returns None and sorts in place.
            Cost me 20 minutes because the traceback pointed at the next line, not the real cause.
     Bad:   Struggled with sorting. -->

- I predicted that a list default (`def add_item(item, basket=[])`) resets on every call.
  It doesn't: the default is created once, when `def` runs, so every call shares one list
  and the second call printed `['apple', 'pen']`. Fix: `basket=None`, then
  `if basket is None: basket = []` inside. Rule: defaults are baked once, at def.

## Still shaky

<!-- What you would fail a question on right now. Being honest here is what makes the spaced
     reviews aim at the right things. -->

## Checkpoint

| | |
|---|---|
| Score | — / 100 |
| Weakest section | — |
| Repair done | — |

## Files

| Path | What it is |
|---|---|
| `lessons/` | Code from the three lessons |
| `problems/` | Practice problems, one file each |
| `mini-project/` | End-of-week build |
