# Week 3 — Functions, Dictionaries and Problem Solving

16 Nov 2026 – 22 Nov 2026

## What this week covered

<!-- Three or four lines in your own words. Not the syllabus. If you cannot write this without
     looking it up, that is the first useful signal of the week. -->

Functions: `def`, parameters vs arguments, `return` vs `print` (no return gives `None`), defaults made
once at definition, and scope by LEGB. Dictionaries are phone books and sets hold unique items; both are
hashed, so lookup by key is fast while searching values is a scan. Counting and grouping with dicts; union,
intersection and difference with sets. Problem solving: understand, plan, code, test, reflect; debugging by
reproducing, shrinking the input and narrowing the bad line; edge cases with decided results and exact asserts.

## What I got wrong

<!-- The actual mistakes, with enough detail to be useful in six months.

     Good:  Assumed `list.sort()` returned the sorted list. It returns None and sorts in place.
            Cost me 20 minutes because the traceback pointed at the next line, not the real cause.
     Bad:   Struggled with sorting. -->

- I predicted that a list default (`def add_item(item, basket=[])`) resets on every call.
  It doesn't: the default is created once, when `def` runs, so every call shares one list
  and the second call printed `['apple', 'pen']`. Fix: `basket=None`, then
  `if basket is None: basket = []` inside. Rule: defaults are baked once, at def.

- Asked to remove duplicates from `tags` but keep their order, I couldn't do it without help.
  `list(set(tags))` loses the order, because sets have none. I had already solved this in
  Week 2 with a `seen` list; the fast version makes `seen` a set: `if tag not in seen:
  unique.append(tag); seen.add(tag)`. Rule: list for order, set for seen.

- To accept ints and floats I wrote `isinstance(num, int or float)`. `int or float` is just
  `int` (`or` returns the first truthy value), so every float was rejected. I had skipped the
  float test I was asked to add, and that was exactly the test that caught it. Fix:
  `isinstance(num, (int, float))`. Rule: the skipped test is the one that bites.

- In the Week 3 checkpoint, my five asserts for `owners(phonebook, number)` skipped the spec's
  own example: two owners, in order (`["Ali", "Omar"]`). That was the only case that tested
  `append` collecting more than one name and keeping the dict's order; a broken `return [name]`
  on the first match would have passed all five. Fix: added
  `assert owners(book, "0300-111") == ["Ali", "Omar"]` and re-ran all six.
  Rule: the spec's own examples are tests too.

- In the quiz-game mini-project, `check_answers` compared with `.lower()` only, even though I
  had already written `clean_reply` (strip + lower). So a stored answer with a stray space,
  `"Paris "`, could never match the reply `"paris"`: `{'Q': False}`. Fix: run `clean_reply` on
  BOTH sides, and add an assert with a messy stored answer.
  Rule: clean both sides with the same function, at the comparison.

## Still shaky

<!-- What you would fail a question on right now. Being honest here is what makes the spaced
     reviews aim at the right things. -->

- Reading a chained line one step at a time, left to right: `groups[k].append(w)` is a lookup first,
  then a method on whatever that returned; `{"a": 1}["b"]` works the same on a literal.
- The group-by pattern: make the bucket first, then append. Never assign `append`'s result back, it's `None`.
- Testable design: pulling the decisions out of functions that call `input()` or `print()` into small pure
  helpers that asserts can reach.

## Checkpoint

| | |
|---|---|
| Score | 89 / 100 (questions 56/60, coding 33/40) |
| Weakest section | Coding tests: missed the spec's two-owners-in-order case |
| Repair done | Added the missing assert, cut the docstring to one line, re-ran all 6: pass |

## Files

| Path | What it is |
|---|---|
| `lessons/` | Code from the three lessons |
| `problems/` | Practice problems, one file each |
| `mini-project/` | End-of-week build |
