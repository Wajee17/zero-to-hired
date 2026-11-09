# Week 2 — Decisions, Loops and Lists

09 Nov 2026 – 15 Nov 2026

## What this week covered

<!-- Three or four lines in your own words. Not the syllabus. If you cannot write this without
     looking it up, that is the first useful signal of the week. -->

## What I got wrong

<!-- The actual mistakes, with enough detail to be useful in six months.

     Good:  Assumed `list.sort()` returned the sorted list. It returns None and sorts in place.
            Cost me 20 minutes because the traceback pointed at the next line, not the real cause.
     Bad:   Struggled with sorting. -->

- I wrote `if member != 'y' or 'Y' or 'n' or 'N':` as a validity check. It fired for
  EVERY input, because `'Y'` on its own is a non-empty string, which is always truthy;
  `or 'Y'` isn't a comparison at all. Fix: compare each time, and reject with `and`:
  `if member != 'y' and member != 'n':` (`!=` joined with `or` is always True).
  Rule: a bare string is always truthy.

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
