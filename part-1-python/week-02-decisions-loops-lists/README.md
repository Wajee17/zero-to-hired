# Week 2 — Decisions, Loops and Lists

09 Nov 2026 – 15 Nov 2026

## What this week covered

<!-- Three or four lines in your own words. Not the syllabus. If you cannot write this without
     looking it up, that is the first useful signal of the week. -->

- Decisions: `if` / `elif` / `else` with comparisons and `and` / `or` / `not`. Order matters: the first true branch runs and the rest are skipped. Empty strings, empty lists and `0` are falsy, but `"0"` is truthy.
- Loops: `for` when I know how many times, `while` until a condition turns false (and something must make it false). `break` stops the loop, `continue` skips to the next round, and `for … else` runs only if no `break` happened.
- Lists are mutable and tuples aren't. `.sort()` changes the list in place, while `sorted()` returns a new one.
- Checkpoint (95/100) and mini-project: a guessing game and a grade calculator. Biggest lesson: after any fix, re-run every old test.

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

- For "sum of 1 to n" I wrote `for num in range(n):` and pasted `Sum of 1 to 10 = 45`
  without comparing it with the expected 55. `range(n)` is 0..n-1, so it skipped n.
  Fix: `range(1, n + 1)`. Rule: range stops before `stop`, the same wall as slicing,
  and always check output against the spec before submitting.

- I started running-best values at 0 three times (meter readings, second largest).
  A made-up 0 silently beats or loses to real data: all-zero readings gave
  "house None", negative readings gave "No second largest". Fix: start from the
  data (best = items[0]) or use None for "nothing yet", never a fake 0.
  Rule: start from the data, not from zero; and always test all-negative/all-zero inputs.

- Twice in one night a fix broke something else: re-run every old test after any change

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
