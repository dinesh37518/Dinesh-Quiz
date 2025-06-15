def india_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["a) Mumbai", "b) Kolkata", "c) New Delhi", "d) Chennai"],
            "answer": "c"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["a) Mahatma Gandhi", "b) Sardar Vallabhbhai Patel", "c) Jawaharlal Nehru", "d) B. R. Ambedkar"],
            "answer": "c"
        },
        {
            "question": "Which river is considered the holiest in India?",
            "options": ["a) Yamuna", "b) Godavari", "c) Narmada", "d) Ganga"],
            "answer": "d"
        },
        {
            "question": "Which state is the largest in India by area?",
            "options": ["a) Maharashtra", "b) Rajasthan", "c) Uttar Pradesh", "d) Madhya Pradesh"],
            "answer": "b"
        },
        {
            "question": "Who wrote the Indian national anthem, 'Jana Gana Mana'?",
            "options": ["a) Rabindranath Tagore", "b) Bankim Chandra Chatterjee", "c) Subhash Chandra Bose", "d) Sarojini Naidu"],
            "answer": "a"
        }
    ]

    score = 0
    print("Welcome to the India Quiz! 🇮🇳\n")

    for idx, q in enumerate(questions):
        print(f"Q{idx + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q["answer"]:
            print("You Are Rocked!\n")
            score += 1
        else:
            print(f"Oops! The correct answer was {q['answer']}.\n")

    print(f"You scored {score} out of {len(questions)}!")

if __name__ == "__main__":
    india_quiz()
