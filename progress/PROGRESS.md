# Progress

Where I actually am. Updated at the end of every session.

=== PROGRESS BLOCK ===
Date: 2026-11-17
Current: Part I · Phase 0 · Week 3 · L3.1 mastered (shaky) · Next: L3.2 dictionaries and sets
Mastered lessons: 1.1 (shaky), 1.2 (shaky), 1.3 (shaky), 2.1 (shaky), 2.2 (shaky), 2.3 (shaky), 3.1 (shaky; test-out not passed, then taught)
Review ledger (lesson: box, next due date): 1.1: B3 2026-11-18 · 1.2: B3 2026-11-18 · 1.3: B3 2026-11-20 · 2.1: B3 2026-11-23 · 2.2: B3 2026-11-20 · 2.3: B3 2026-11-23 · 3.1: B1 2026-11-18
Overdue reviews: 0 (1.1, 1.2 and 3.1 due next session)
Weak concepts: [2.3-start-value: start a running best from the data or None, never 0; applied unprompted, B2, 2026-11-13] · [2.3-b: remove() by VALUE, pop(i) by position and returns the item, B2, 2026-11-13] · [2.3-chain: chained brackets act on the previous result, B2, 2026-11-13] · [2.1-c: several conditions can be true, only the first runs, B2, 2026-11-13] · [2.2-c: the accumulator's start value decides its type, B2, 2026-11-11] · [3.1-b: no return → None; NoneType in an error → hunt the missing return; None[0] is TypeError, None.upper() is AttributeError, B1, 2026-11-17] · [3.1-default: defaults created once at def; never a list default, use None; Miss then re-test Solid, B1, 2026-11-17] · [3.1-bare: a bare function name is the object and always truthy; brackets call it; Miss, B1, 2026-11-17] · [3.1-c-errors: a wrong call is a TypeError; name the error, not just 'runtime error', B1, 2026-11-17] · [3.1-edges: convert input at the edges, keep core functions pure; Partial, B1, 2026-11-17] · [ties: max/running best with > keeps the FIRST tie, >= keeps the last, 2026-11-17]
Memory hooks: L1.1 b "Unprinted work is invisible" · c "REPL talks back, script stays quiet" · e "Bottom says what, above says where" · L1.2 c "Convert makes a copy, not a change" · d "Same group? Leftmost wins" · e "input() always hands you text" · L1.3 index "One house: must exist. A range: whatever's there" · slice "Backwards step, backwards blanks" · immutability "No tag, no keep" · L2.1 short-circuit "No A? Don't fetch B" · elif "First match wins, so specific first" · or-trap "A bare string is always truthy" · L2.2 accumulator "Before, inside, after" · loops "For each item; while until" · range "Same wall as slicing" · L2.3 running best "Start from the data, not from zero" · sort "In-place hands back None" · zip "Zip stops at the shortest, silently" · L3.1 none "No return? You get None" · default "Defaults are baked once, at def" · scope "Inside looks out; outside can't"
Shaky topics: ['' vs None; is None, not == None, 2026-11-12] · [.find() returns -1 → silent slicing bug, 2026-11-08] · [float == comparison → abs(a - b) < tiny, 2026-11-09] · [split() vs split(" "), 2026-11-12] · [only-spaces input: check the split LIST, 2026-11-12] · [runtime vs syntax: "the prompts appeared" is the proof, 2026-11-13] · [rounding to 1 dp looks at the 2nd decimal, 2026-11-13] · [exact output: spacing inside strings, type() prints <class 'tuple'>, 2026-11-16] · [docstrings: one line, written by me, must match the code (letter_grade copy-paste slip), 2026-11-17]
Recurring mistakes: skipping the "why" · output "nearly" matches the spec (spacing in strings, <class = 'tuple'>) · test runs not actually run · a fix breaks something else and only the new test is re-run · NEW: skipping parts of multi-part questions (5x in L3.1) · NEW: saying 'runtime error' without naming it · NEW: running code in a scratch file outside the repo
Error log (last 10): [second largest: start 0 broke negatives and 0] · [remove-duplicates kept the LAST copy] · [words[0][-1] read as two list picks] · [s.split() said to split into characters] · [checkpoint fix moved print outside if/else → "0 days (day 2 to day 1)"] · [grades fix: no continue after "Not a whole number" → ValueError, pushed] · [top_three: traced sort() → None but not None[-3:] → crash] · [class_report test: replaced class_report(scores) with class_report([])] · [list default predicted to reset each call → shared ['apple', 'pen']] · [if is_adult: predicted NameError → function object is truthy, always 'Welcome']
Brain dumps / concept maps / own-words cheat sheets done: Week 1 brain dump ✓ · Week 1 concept map ✓ · Week 2 brain dump ✓ · Week 2 concept map ✓ (6 links)
Checkpoints: Wk1 88/100 · Wk2 95/100
Exams: Phase 0 — (end of Week 3), Phase 1 —, Phase 2 —, Part I Final —
Mini-projects (Part I): Week 1 "Mad-libs and unit converter" ✓ · Week 2 "Number-guessing game and grade calculator" ✓
Portfolio projects: P0 —
Problems solved (title: hints used): Week 1: 10 problems, 1 hint · Week 2: Ticket (guided): 0 · Leap year: 0 · FizzBuzz: 0 · Triangle: 0 · PIN check (guided): 0 · Sum 1 to n: 1 · Is prime: 0 · Collatz: 0 · Meter readings (guided): 0 · Even/odd counter: 1 · Second largest: 2 (traced, not run) · Remove duplicates: 2 · Checkpoint Step streak: 0 · Week 3: L3.1 guided grade_tools: 0 hints (several repairs) · is_even: 0 · gcd: 0 · word_stats: 1 lookup (key=len)
Placement: 6/10 · Q4, Q5 and Q10 now solved correctly · L3.1 test-out tried 2026-11-16: not passed (2 Solid, 2 Partial) → taught in full
Setup: Windows, VS Code (System Installer), Python 3.14.6 at C:\Python314, Git (wajeehaider94@gmail.com, linked), Jupyter via VS Code + ipykernel · terminal still opens in C:\Program Files\Microsoft VS Code
Chosen specialisation: — (undecided, decide by Wk 50)
Lane: full (12 h/week) · Flex weeks used: 0 of 4 · note: Week 2 ran ~18 h and L3.1 ~5–6 h (budget ~3 h per lesson); check the lane at the Phase 0 exam
Repo: last push 2026-11-17 (L3.1) · weeks committed: 4
Next up: warm-up (1.1, 1.2, 3.1 due) → L3.2 dictionaries and sets → L3.3 problem solving and debugging → Week 3 checkpoint + mini-project → Phase 0 Exam
Hours this week: Week 3 so far ~5–6 focused (L3.1 incl. test-out)
=== END ===

## Weekly log

One line per week, written at the checkpoint. Short is fine — the week README holds the detail.

| Week | Dates | Checkpoint | Note |
|---|---|---|---|
| 0 | | — | Setup, placement, repository created |
| 1 | 02–08 Nov | 88 | Basics, strings; mini-project mad-libs + converter |
| 2 | 09–15 Nov | 95 | Decisions, loops, lists; regression-testing lesson learned the hard way |

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
