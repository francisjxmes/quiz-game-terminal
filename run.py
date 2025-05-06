# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# List of quiz questions and their answers
quiz_questions = [
    {
        "question": "What is the capital of Canada?",
        "answer": "ottawa"
    },
    {
        "question": "Which river flows through Cairo?",
        "answer": "nile"
    },
    {
        "question": "What country has the most natural lakes?",
        "answer": "canada"
    },
    {
        "question": "Who played Iron Man in the Marvel Cinematic Universe?",
        "answer": "robert downey jr"
    },
    {
        "question": (
            "What is the name of the Netflix series featuring a chess "
            "prodigy named Beth Harmon?"
        ),
        "answer": "the queen's gambit"
    },
    {
        "question": "Which artist released the hit song 'Bad Guy' in 2019?",
        "answer": "billie eilish"
    },
    {
        "question": "Who is the current president of the United States?",
        "answer": "donald trump"
    },
    {
        "question": "Which country exited the European Union in 2020?",
        "answer": "united kingdom"
    },
    {
        "question": "What international organization is abbreviated as 'UN'?",
        "answer": "united nations"
    }
]


# Function to run the quiz


def run_quiz():
    score = 0  # Start the score at 0

    for q in quiz_questions:
        # Validation loop: Keeps asking until user provides a non-empty answer
        while True:
            user_answer = input(q["question"] + " ").strip().lower()
            if user_answer:  # if not empty
                break
            else:
                print("Please enter an answer!")

        # Check answer correctness
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer'].title()}\n")

    # Final score
    print(f"You got {score} out of {len(quiz_questions)} correct.\n")

# Main function: adds replay loop


def main():
    print("Welcome to the Quiz Game!")
    while True:
        run_quiz()
        # Ask if user wants to play again
        play_again = input(
            "Do you want to play again? (yes/no): "
        ).strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye.")
            break


# Start the game by calling the main menu


main()
