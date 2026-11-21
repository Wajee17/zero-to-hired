# Progress

Where I actually am. Updated at the end of every session.

=== PROGRESS BLOCK ===
Date: 2026-11-21
Current: Part I · Phase 0 · Week 3 · all 3 lessons mastered (shaky) · checkpoint 89/100 · Phase 0 mini-project ✓ · whole-phase review ✓ · Next: Phase 0 Exam
Mastered lessons: 1.1 (shaky), 1.2 (shaky), 1.3 (shaky), 2.1 (shaky), 2.2 (shaky), 2.3 (shaky), 3.1 (shaky; test-out not passed, then taught), 3.2 (shaky), 3.3 (shaky)
Review ledger (lesson: box, next due date): 1.1: B4 2026-12-09 · 1.2: B4 2026-12-09 · 1.3: B3 re-test 2026-11-23 (R3 Partial: split(" ") pieces; same-day re-test Solid) · 2.1: B4 2026-12-12 · 2.2: B4 2026-12-10 · 2.3: B4 2026-12-12 · 3.1: B3 2026-11-28 (re-test Solid 11-21) · 3.2: B1 2026-11-22 (R7 Miss: groups[k].append on a missing key; repaired) · 3.3: B2 2026-11-23
Overdue reviews: 0 (3.2 due 11-22; 1.3 re-test and 3.3 due 11-23)
Weak concepts: [2.3-start-value: start a running best from the data or None, never 0; applied unprompted, B2, 2026-11-13] · [2.3-b: remove() by VALUE, pop(i) by position and returns the item, B2, re-test Solid 2026-11-21] · [2.3-chain: chained brackets act on the previous result, step by step, left to right — also on literals: {"a": 1}["b"], [1, 2][5]; Miss again 11-21 (R7, R10), B1, 2026-11-21] · [2.1-c: several conditions can be true, only the first runs, B2, 2026-11-13] · [2.2-c: the accumulator's start value decides its type, B2, 2026-11-11] · [3.1-b: no return → None; NoneType in an error → hunt the missing return; None[0] is TypeError, None.upper() is AttributeError, B2, re-test Solid 2026-11-18] · [3.1-default: defaults created once at def; never a list default, use None; Miss then re-test Solid, B2, re-test Solid 2026-11-18] · [3.1-bare: a bare function name is the object and always truthy; brackets call it; Miss, B2, re-test Solid 2026-11-18] · [3.1-c-errors: a wrong call is a TypeError; name the error, not just 'runtime error', B2, re-test Solid 2026-11-18] · [3.1-edges: convert input at the edges, keep core functions pure; Partial, B2, re-test Solid 2026-11-18] · [ties: max/running best with > keeps the FIRST tie, >= keeps the last, 2026-11-17] · [3.2-errors: a list as a dict key is TypeError (unhashable); KeyError is only a missing lookup, B2, re-test Solid 2026-11-19] · [growth words: nested loops are quadratic (double the input, 4x the work), not exponential, B2, re-test Solid 2026-11-19] · [3.2-order: keep order + uniqueness with a seen SET + keep list (or dict.fromkeys); needed a hint; re-test Solid from memory, B2, 2026-11-19] · [3.2-c: a new key goes last, an updated key keeps its place; skipped in recall 11-19, re-test Solid 2026-11-21] · [3.3-f: a help question has five parts: goal, minimal runnable code, expected, actual + exact error, what I tried; B1, 2026-11-19] · [3.3-asserts: assert the EXACT value (== expected), not truthiness; B1, 2026-11-19] · [3.3-expected: every edge case needs a decided expected result, a value or a deliberate error; B1, 2026-11-19] · [types: isinstance(x, (int, float)); `int or float` is just int; don't restrict numbers to int; B1, 2026-11-19] · [1.3-find: s.find() returns -1 and s[-1:] silently gives the last char; check before slicing; Partial 11-19, re-test Solid 2026-11-20] · [3.2-values: only KEYS are hashed; `x in d.values()` scans every value; Miss, same-day re-test Solid, B1, 2026-11-20] · [3.3-spec: the spec's own examples are tests; owners() asserts missed the two-owners-in-order case, B1, 2026-11-20] · [errors: IndexError = bad position; right type + bad value (empty list) → ValueError; Partial then Solid, 2026-11-20] · [3.3-loop: problem-solving loop = understand → plan (pseudocode) → code → test → reflect; NOT the debugging steps; merged in brain dump, B1, 2026-11-20] · [design: pull decisions out of input()/print() functions into pure helpers so asserts can reach them; 'it can't go wrong' is not a reason to skip tests; needed the answer, B1, 2026-11-21] · [compare: clean BOTH sides with the same function at the comparison (check_answers used .lower() only), B1, 2026-11-21] · [3.2-groupby: bucket first, then append (groups[k] = groups.get(k, []); groups[k].append(w)); never assign the result of append — it's None; Miss then repaired, B1, 2026-11-21]
Memory hooks: L1.1 b "Unprinted work is invisible" · c "REPL talks back, script stays quiet" · e "Bottom says what, above says where" · L1.2 c "Convert makes a copy, not a change" · d "Same group? Leftmost wins" · e "input() always hands you text" · L1.3 index "One house: must exist. A range: whatever's there" · slice "Backwards step, backwards blanks" · immutability "No tag, no keep" · L2.1 short-circuit "No A? Don't fetch B" · elif "First match wins, so specific first" · or-trap "A bare string is always truthy" · L2.2 accumulator "Before, inside, after" · loops "For each item; while until" · range "Same wall as slicing" · L2.3 running best "Start from the data, not from zero" · sort "In-place hands back None" · zip "Zip stops at the shortest, silently" · L3.1 none "No return? You get None" · default "Defaults are baked once, at def" · scope "Inside looks out; outside can't" · L3.2 lookup "Phone book: straight to the name" · group-by "New key? Make the bucket first" · dedupe "List for order, set for seen" · L3.3 process "The skipped test is the one that bites" · asserts "Silent pass, loud AssertionError" · debugging "Shrink the input, halve the code"
Shaky topics: ['' vs None; is None, not == None, 2026-11-12] · [.find() returns -1 → silent slicing bug, 2026-11-08] · [float == comparison → abs(a - b) < tiny, 2026-11-09; review Solid 2026-11-21] · [split() vs split(" "): split(" ") never keeps the space; every cut makes a piece, adjacent/edge spaces give '' (cuts + 1 pieces); Partial then Solid 2026-11-21] · [only-spaces input: check the split LIST, 2026-11-12] · [runtime vs syntax: "the prompts appeared" is the proof, 2026-11-13] · [rounding to 1 dp looks at the 2nd decimal, 2026-11-13] · [exact output: spacing inside strings, type() prints <class 'tuple'>, 2026-11-16] · [docstrings: one line, written by me, must match the code (letter_grade copy-paste slip), 2026-11-17]
Recurring mistakes: skipping the "why" (again 11-20: concept-map links, Q6 cause chain; 11-21: 'check before the loop' why) · skipping parts of multi-part questions (5x on 11-21 in the mini-project plan) · output "nearly" matches the spec (spacing in strings, <class = 'tuple'>) · test runs not actually run · a fix breaks something else and only the new test is re-run · NEW: skipping parts of multi-part questions (5x in L3.1) · NEW: saying 'runtime error' without naming it · NEW: running code in a scratch file outside the repo · NEW: docstring doesn't match the code after an edit (twice: letter_grade) · design answers give a choice without the trade-off · NEW: pasted code differs from the code that ran (3x in L3.3) · a review comment not applied to sibling functions (float check in second_largest)
Error log (last 10): [if is_adult: predicted NameError → function object is truthy, always 'Welcome'] · [list as a dict key predicted KeyError → TypeError: unhashable type] · [two_sum_slow's growth called exponential → quadratic] · [isinstance(num, int or float) accepted only int; the skipped float test would have caught it] · [K2: said 'read the traceback' for a bug with no error] · [said `2 in d.values()` is as fast as a key lookup → it scans every value] · [owners(): 5 asserts skipped the spec's two-owners-in-order example] · [quiz: check_answers used .lower() not clean_reply → stored "Paris " never matched] · [quiz: printed a 'skip' prompt but both if-branches did break → skip saved as a wrong answer] · [R7: groups[word[0]].append on a missing key called AttributeError (it's KeyError); fix assigned append's None into the dict]
Brain dumps / concept maps / own-words cheat sheets done: Week 1 brain dump ✓ · Week 1 concept map ✓ · Week 2 brain dump ✓ · Week 2 concept map ✓ (6 links) · Week 3 brain dump ✓ (merged the two loops; missed get/KeyError, hashable keys, order, group-by) · Week 3 concept map ✓ (6 links, 3 to older weeks; most whys missing) · Phase 0 whole-phase review ✓ 2026-11-21 (R1–R10: 7 Solid, R3 Partial, R7 Miss, R10 needed literal-indexing explained)
Checkpoints: Wk1 88/100 · Wk2 95/100 · Wk3 89/100
Exams: Phase 0 — (end of Week 3), Phase 1 —, Phase 2 —, Part I Final —
Mini-projects (Part I): Week 1 "Mad-libs and unit converter" ✓ · Week 2 "Number-guessing game and grade calculator" ✓ · Phase 0 "Text-based quiz game" ✓ (5 questions; clean_reply/check_answers/score pure + asserts; ask_questions/play do I/O; empty quiz → ValueError; blank reply re-asked)
Portfolio projects: P0 —
Problems solved (title: hints used): Week 1: 10 problems, 1 hint · Week 2: Ticket (guided): 0 · Leap year: 0 · FizzBuzz: 0 · Triangle: 0 · PIN check (guided): 0 · Sum 1 to n: 1 · Is prime: 0 · Collatz: 0 · Meter readings (guided): 0 · Even/odd counter: 1 · Second largest: 2 (traced, not run) · Remove duplicates: 2 · Checkpoint Step streak: 0 · Week 3: L3.1 guided grade_tools: 0 hints (several repairs) · is_even: 0 · gcd: 0 · word_stats: 1 lookup (key=len) · L3.2 guided group_by_grade: 0 · letter_freq: 0 · common: 0 · two_sum: 1 hint (level 1) · L3.3 guided trimmed_mean (tests first): 0 · debug_demo: 0 · P1 find-the-bug: 5/5 · fizzbuzz + asserts: 0 · second_largest tests-first: 0 · Checkpoint owners: 0 hints (missed the spec-example test; repaired)
Placement: 6/10 · Q4, Q5 and Q10 now solved correctly · L3.1 test-out tried 2026-11-16: not passed (2 Solid, 2 Partial) → taught in full
Setup: Windows, VS Code (System Installer), Python 3.14.6 at C:\Python314, Git (wajeehaider94@gmail.com, linked), Jupyter via VS Code + ipykernel · terminal still opens in C:\Program Files\Microsoft VS Code
Chosen specialisation: — (undecided, decide by Wk 50)
Lane: full (12 h/week) · Flex weeks used: 0 of 4 · note: Week 2 ran ~18 h; Week 3 lessons ~12–14 h (L3.1 5–6, L3.2 3–4, L3.3 3–4); check the lane at the Phase 0 exam
Repo: last push 2026-11-21 (Wk3 checkpoint + Phase 0 mini-project) · weeks committed: 4
Next up: Phase 0 Exam (60 min, closed-book, 10 questions + 3 coding tasks: warm-up, easy, easy+; pass 80; ≥30% from Weeks 1–2) → lane recheck · reviews: 3.2 due 11-22; 1.3 re-test and 3.3 due 11-23
Hours this week: Week 3 ~16–18 focused (L3.1 5–6, L3.2 3–4, L3.3 3–4, checkpoint 1.5, mini-project 1.5, phase review 0.75)
=== END ===

## Weekly log

One line per week, written at the checkpoint. Short is fine — the week README holds the detail.

| Week | Dates | Checkpoint | Note |
|---|---|---|---|
| 0 | | — | Setup, placement, repository created |
| 1 | 02–08 Nov | 88 | Basics, strings; mini-project mad-libs + converter |
| 2 | 09–15 Nov | 95 | Decisions, loops, lists; regression-testing lesson learned the hard way |
| 3 | 16–22 Nov | 89 | Functions, dicts and sets, debugging; the spec's own examples are tests too |

---

## Exams

| Exam | Week | Score | Retake |
|---|---|---|---|
| Phase 0 | 3 | — | |
| Phase 1 | 7 | — | |
| Phase 2 | 11 | — | |
| Part I final mock interview | 16 | — | |
| Stage A | 21 | — | |
| Stage B | 29 | — | |
| Stage C | 37 | — | |
| Stage D | 42 | — | |
| Stage E | 48 | — | |
| Stage F | 52 | — | |
| Final mock loop | 58 | — | |
