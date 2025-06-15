def language_quiz():
    questions = [
        {
            "question": "1. What is the most spoken language in the world by native speakers?",
            "options": ["A. English", "B. Tamil", "C. Mandarin Chinese", "D. Spanish"],
            "answer": "C"
        },
        {
            "question": "2. Which language is primarily spoken in Brazil?",
            "options": ["A. Spanish", "B. Portuguese", "C. Italian", "D. French"],
            "answer": "B"
        },
        {
            "question": "3. What is the official language of Egypt?",
            "options": ["A. Arabic", "B. Turkish", "C. Persian", "D. French"],
            "answer": "A"
        },
        {
            "question": "4. Which of the following languages uses the Cyrillic script?",
            "options": ["A. Greek", "B. Russian", "C. Hindi", "D. Korean"],
            "answer": "B"
        },
        {
            "question": "5. Which language family does English belong to?",
            "options": ["A. Romance", "B. Semitic", "C. Slavic", "D. Germanic"],
            "answer": "D"
        },
        {
            "question": "6. What language is primarily spoken in Iran?",
            "options": ["A. Arabic", "B. Urdu", "C. Persian (Farsi)", "D. Pashto"],
            "answer": "C"
        },
        {
            "question": "7. Which is the official language of the United Nations?",
            "options": ["A. Arabic", "B. Russian", "C. Chinese", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "8. What is the writing system used for Japanese?",
            "options": ["A. Hangul", "B. Kanji and Kana", "C. Devanagari", "D. Cyrillic"],
            "answer": "B"
        },
        {
            "question": "9. Which language is considered a Oldest language?",
            "options": ["A. Tamil", "B. Sanskrit", "C. Chinese", "D. Arabic"],
            "answer": "A"
        },
        {
            "question": "10. Which country has the most official languages?",
            "options": ["A. India", "B. Switzerland", "C. South Africa", "D. Canada"],
            "answer": "C"
        }
    ]

    score = 0
    print("Welcome to the World Languages Quiz!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if answer == q["answer"]:
            print("You Are Rocked!\n")
            score += 1
        else:
            print(f"Oops. The correct answer is {q['answer']}.\n")

    print(f" Quiz finished! Your final score: {score} out of {len(questions)}")

if __name__ == "__main__":
    language_quiz()
