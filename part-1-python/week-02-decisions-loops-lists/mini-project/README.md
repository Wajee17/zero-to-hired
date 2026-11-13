# Week 2 mini-project: Grade calculator and number guessing game

Two small command-line programs from Week 2 of Zero to Hired.

## grades.py

Asks for test scores one at a time until you press Enter on an empty line. Each score gets a letter
grade (A 90+, B 80+, C 70+, D 60+, F below 60). Then it prints every score with its grade, the count,
the average and its letter grade, the highest and lowest scores, and how many of each grade there were.
Text and out-of-range numbers are rejected with different messages, and you're asked again.

**Sample run**
```
Score: 95
Score: 82
Score: abc
Not a whole number
Score: 105
Out of range: scores go from 0 to 100
Score: 71
Score: 58
Score: 88
Score:
Scores: 95 (A), 82 (B), 71 (C), 58 (F), 88 (B)
Count: 5
Average: 78.8 (C)
Highest: 95  Lowest: 58
A: 1  B: 2  C: 1  D: 0  F: 1
```

## guess.py

The computer picks a random number from 1 to 100 and you get 7 guesses to find it. After each guess
it tells you whether you're too high or too low. Invalid input (text, or a number outside 1–100) is
rejected and doesn't use up a guess. When the round ends, `y` starts a new round with a new number.

**Sample run** (a win, then a loss)
```
Number: 50
Too high
Number: 25
Too low
Number: seven
Please enter a whole number
Number: 150
Pick a number between 1 and 100
Number: 37
Too high
Number: 31
Got it in 4 attempts!
Play again? (y/n) y
Number: 50
Too low
Number: 75
Too low
Number: 88
Too high
Number: 82
Too high
Number: 79
Too high
Number: 78
Too high
Number: 77
Too high
Ran out of attempts. Number was 76
Play again? (y/n) n
```

## How to run
```
python grades.py
python guess.py
```

## Concepts used
`while True` loops with `break` and `continue` · nested loops · `for ... else` · `range()` ·
`if` / `elif` / `else` chains · chained comparisons (`0 <= n <= 100`) · lists (`.append()`, `.count()`) ·
`zip()` and `", ".join()` · input validation with `.isdigit()` and `.strip()` · `random.randint()` · `sys.exit()`

## Known limitations

**grades.py**
- Decimal scores are rejected: `87.5` gets `Not a whole number`, because `.isdigit()` only accepts digits
- Negative numbers get the wrong message: `-5` gets `Not a whole number` instead of `Out of range`, because `.isdigit()` fails on the minus sign before the range check runs
- The shown average can disagree with its grade: nineteen 90s and one 89 average 89.95, which prints as `Average: 90.0 (B)`. The grade uses the exact average, but the display rounds to one decimal place
- A superscript digit like `²` crashes it with a `ValueError`: `.isdigit()` counts it as a digit, but `int()` can't convert it
- The grade cut-offs are written out twice, once for each score and once for the average, so changing a boundary means editing both

**guess.py**
- The same superscript problem: entering `²` crashes it with a `ValueError`
- Only an exact `y` plays again. `yes` quits, so does a typo like `t`
- There's no counter showing how many guesses are left, so you only find out you've run out when the round ends
