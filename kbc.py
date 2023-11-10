# # Create a program capable of displaying questions to the user like KBC.
# # Use List data type to store the questions and their correct answers.
# # Display the final amount the person is taking home after playing the game.


print("""Welcome to KBC \nAnswer the 10 questions and win \nHighest winning value is Rs 1,00,000 \n""")

questions_kbc = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "correct": "c",
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["a) 1912", "b) 1920", "c) 1905", "d) 1935"],
        "correct": "a"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "correct": "c"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"],
        "correct": "b"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["a) Nucleus", "b) Ribosome", "c) Mitochondria", "d) Endoplasmic reticulum"],
        "correct": "c"
    },
    {
        "question": "Which of the following is a primary color?",
        "options": ["a) Green", "b) Yellow", "c) Red", "d) Orange"],
        "correct": "c"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["a) 8", "b) 6", "c) 10", "d) 12"],
        "correct": "a"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["a) Jupiter", "b) Venus", "c) Mars", "d) Saturn"],
        "correct": "c"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Stephen Hawking"],
        "correct": "b"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) H2O ", "b) CO2", "c) O2", "d) CH4"],
        "correct": "a"
    }
]


def run_kbc(questions):
    score = 0
    prize = 1000
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
            
        user_answer = input("Enter your answer").lower()
        if user_answer == question["correct"].lower():
            print("That's correct!")
            score+=1
            prize*=2
        else:
            print("Sorry, that's incorrect.")
            
    print(f"Your final score is: {score} out of {len(questions)}")
    print(f"Your prize money is: Rs{prize}")

    
    
run_kbc(questions_kbc)
            
            


# #Example of accessing the first question and its options
# first_question = questions[0]["question"]
# first_options = questions[0]["options"]
# print(f"Question: {first_question}")
# print("Options:")
# for option in first_options:
#     print(option)

# for choice in first_options:
#     input("Enter your choice: ")
#     if (choice == "c"):
#         print("You are correct! The answer is c)")
#     else:
#         print("Incorrect. Please try again.")
#         break




