def run_quiz(questions):
    score = 0
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nYour final score: {score} out of {len(questions)}")

# Define your questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. William Shakespeare", "C. Jane Austen", "D. Charles Dickens"],
        "answer": "B"
    }
]

# Start the quiz
print("Welcome to the Quiz Game!")
run_quiz(quiz_questions)
