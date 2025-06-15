import random
questions = [
    {
        "question": "What is the result of: 5 + 2 * 3",
        "options": ["21", "11", "15", "7"],
        "answer": "B"  # 5 + (2 * 3) = 5 + 6 = 11
    },
    {
        "question": "What is the result of: (8 - 3) * 2",
        "options": ["10", "13", "6", "5"],
        "answer": "A"  # (8 - 3) * 2 = 5 * 2 = 10
    },
    {
        "question": "What is the result of: 18 ÷ 3 + 2",
        "options": ["8", "6", "4", "10"],
        "answer": "D"  # 18 ÷ 3 + 2 = 6 + 2 = 8
    },
    {
        "question": "What is the result of: 12 - 2 * (3 + 1)",
        "options": ["4", "16", "8", "0"],
        "answer": "A"  # 12 - 2 * (3 + 1) = 12 - 2 * 4 = 12 - 8 = 4
    },
    {
        "question": "What is the result of: 3 + 6 ÷ 2 * 3",
        "options": ["9", "12", "15", "18"],
        "answer": "B"  # 3 + ((6 ÷ 2) * 3) = 3 + (3 * 3) = 3 + 9 = 12
    },
]

def quiz():
    score = 0
    print("Welcome to the BODMAS Quiz!\nChoose the correct answer (A, B, C, or D):\n")

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for idx, option in zip(['A', 'B', 'C', 'D'], q['options']):
            print(f"  {idx}. {option}")
        answer = input("Your answer: ").strip().upper()

        if answer == q["answer"]:
            print("You Are Rocked!\n")
            score += 1
        else:
            correct_option = q['answer']
            print(f"Oops! The correct answer was {correct_option}. {q['options'][ord(correct_option)-65]}\n")

    print(f"Quiz finished! Your score: {score}/{len(questions)}")

# Run the quiz
if __name__ == "__main__":
    quiz()
