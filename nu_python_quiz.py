# ====================
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------Philly Quiz!------")

        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses, guesses)

# ====================


def check_answer(answer, guess):
    if answer == guess:
        print("Right Jawn!")
        return 1
    else:
        print("Wrong Jawn!")
        return 0

# ====================


def display_score(correct_guesses, guesses):
    print("--------------------")
    print("How'd you do?:")
    print("--------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")

# ====================


def play_again():

    response = input("Do you want to play again? (Yes or No):")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


# ====================


questions = {
    "Who created the first Cheesesteak?: ": "A",
    "What year was Philadelphia founded?: ": "B",
    "Which Philly Quarterback beat Tom Brady to win the Superbowl in 2018?: ": "C",
    "Is Philadelphia located in Pennsylvania?: ": "A"


}

options = [["A. Pat Olivieri", "B. Elon Musk", "C. Questlove", "D. Betsy Ross"],
           ["A. 1978", "B. 1682", "C. 2003", "D. 2017"],
           ["A. Drew Brees", "B. Russell Wilson",
               "C. Nick Foles", "D. Patrick Mahomes"],
           ["A. Yes", "B. No", "C. Who is Philly?", "D. What is Philly?"]]

new_game()

while play_again():
    new_game()

print("Peace Out!")
