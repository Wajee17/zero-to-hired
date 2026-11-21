def clean_reply(reply):
    """Return the reply with surrounding whitespace removed and in lowercase."""
    return reply.strip().lower()

def ask_questions(quiz):
    """Ask each quiz question and return a dict mapping each question to the cleaned reply."""
    unchecked_quiz = {}
    for question in quiz:
        while True:
            user_answer = input(f"{question}: ")
            clean_user_answer = clean_reply(user_answer)
            if not clean_user_answer:
                print("Not a valid input")
                continue
            break
        unchecked_quiz[question] = clean_user_answer
    return unchecked_quiz

def check_answers(quiz, replies):
    """Return a dict mapping each question to True if the reply matches the answer, else False."""
    marked_questions = {}
    for question in quiz:
        marked_questions[question] = clean_reply(quiz[question]) == clean_reply(replies[question])
    return marked_questions

def score(results):
    """Return the number of correct answers in the results."""
    count_correct_answers = 0
    for mark in results.values():
        if mark:
            count_correct_answers += 1
    return count_correct_answers

def play(quiz):
    """Run the quiz and print the player's score."""
    if not quiz:
        raise ValueError ("quiz has no questions")
    total = score(check_answers(quiz, ask_questions(quiz)))
    print(f"{total}/{len(quiz)} ({(total / len(quiz) * 100):.2f}%)")


assert clean_reply("  PaRiS \n") == "paris"
assert clean_reply("") == ""
assert clean_reply("   ") == ""

test_quiz = {"Capital of France": "paris", "2 + 2": "4", "Largest planet": "Jupiter"}
test_replies = {"Capital of France": "paris", "2 + 2": "5", "Largest planet": "jupiter"}
assert check_answers(test_quiz, test_replies) == {"Capital of France": True, "2 + 2": False, "Largest planet": True}
assert check_answers({"Capital of France": "  Paris "}, {"Capital of France": "paris"}) == {"Capital of France": True}

assert score({"q1": True, "q2": True, "q3": True}) == 3
assert score({"q1": False, "q2": False, "q3": False}) == 0
assert score({"q1": True, "q2": False, "q3": True}) == 2

print("All tests passed")

quiz = {"Capital of France": "paris", "2 + 2": "4", "Largest planet": "jupiter", "Days in a week": "7", "Opposite of hot": "cold"}
play(quiz)





    

    

