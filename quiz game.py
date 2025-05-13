def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("What is your answer?: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("------------------")
    print("Results")
    print("------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    return response == "YES"


# Global Variables
questions = {
    "What is the correct file extension for Python files?": "A",
    "Which of the following is used to define a function in Python?": "A",
    "In Python, what is the boolean value of the integer 0?": "B",
    "Which keyword is used to create a class in Python?": "A"
}

options = [
    ["A. .py", "B. .pyc", "C. .pyo", "D. .pyw"],
    ["A. def", "B. void", "C. function", "D. fun"],
    ["A. True", "B. False", "C. None", "D. Zero"],
    ["A. class", "B. struct", "C. object", "D. function"]
]

# Game Loop
new_game()
while play_again():
    new_game()

print("Thank you for playing!")
