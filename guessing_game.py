# --------------------------------------------------------------------------------
# How to create a simple trivia game with Python - Basic Approach
# Made with ❤️ in Python 3 by Alvison Hunter - March 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def guess_game():
    questions_dict = {
        "What is the capital of France?": "Paris",
        "What is the capital of Ecuador?": "Quito",
        "Where is Managua located?": "Nicaragua",
    }
    # list out keys and values separately
    key_list = list(questions_dict.keys())
    val_list = list(questions_dict.values())
    curr_question = 0
    attempts = 0
    correct_answers = 0
    try:
        while True:
            if attempts == 3:
                print("You've used all of the possible attempts. Try again later!")
                break

            print(f"{key_list[curr_question]}")
            answer = input()
            if (answer.title() == val_list[curr_question]):
                print("Good job! let's go to the next question:")
                correct_answers += 1
                curr_question += 1
                print(correct_answers, curr_question)
                if(correct_answers>len(key_list)):
                    print("YOU WIN! Congratulations!")
                    break
                else:
                    pass
            else:
                print("Uh oh! that is not the correct answer!")
                attempts = 1
                pass
    except Exception as e:
        print("Uh oh! Something went really wrong!")
        print(e)
        quit()

guess_game()
