# Quiz Game

This is a small quiz game that runs in the terminal. It asks 5 questions, you type your answers, and at the end it tells you your score and percentage.

Your answers don't have to match the case exactly and extra spaces are ignored, so "  PaRiS " counts the same as "paris". The stored answers get cleaned the same way before comparing. If you press Enter without typing anything, or only type spaces, it says "Not a valid input" and asks the same question again.

Before the game starts, the file runs some asserts to test clean_reply, check_answers and score. If they all pass it prints "All tests passed" and then the game starts.

To run it, open a terminal in this folder and type:

```
python quiz_game.py
```

## Sample run

I ran this in a Windows PowerShell window and copied it from there. I pressed Enter on a blank line for the first question and typed only spaces for the third one, used mixed case and extra spaces, and typed "seven" instead of "7" on purpose:

```
PS F:\dev\zero-to-hired\part-1-python\week-03-functions-dictionaries-problem-solving\mini-project> python quiz_game.py
All tests passed
Capital of France:
Not a valid input
Capital of France:   PaRiS
2 + 2: 4
Largest planet:
Not a valid input
Largest planet: Jupiter
Days in a week: seven
Opposite of hot: COLD
4/5 (80.00%)
```

## Limitations

- Typos and synonyms are marked wrong. In the run above "seven" didn't count because the answer is "7", and "jupitr" wouldn't count either.
- You can't skip a question. You have to type something for every question before you get your score.
- The questions are always asked in the same order and they are written straight into the code.

## What I'd do next

Add a real skip option that leaves the skipped question out of the score, and load the questions from a file so I can add more without changing the code.
