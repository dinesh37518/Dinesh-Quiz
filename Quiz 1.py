def quiz():
    questions = [
        {
            "question": "1. Who was the second person to walk on the Moon?",
            "options": ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Michael Collins", "D. Yuri Gagarin"],
            "answer": "B"
        },
        {
            "question": "2. What was the second country to detonate a nuclear bomb?",
            "options": ["A. USA", "B. Soviet Union", "C. United Kingdom", "D. France"],
            "answer": "B"
        },
        {
            "question": "3. Who was the second president of the United States?",
            "options": ["A. George Washington", "B. Thomas Jefferson", "C. John Adams", "D. James Madison"],
            "answer": "C"
        },
        {
            "question": "4. What is the second largest country by area?",
            "options": ["A. Russia", "B. Canada", "C. China", "D. USA"],
            "answer": "B"
        },
        {
            "question": "5. Which city hosted the second modern Olympic Games (1900)?",
            "options": ["A. Athens", "B. London", "C. Paris", "D. Berlin"],
            "answer": "C"
        },
        {
            "question": "6. What is the second longest river in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Yangtze", "D. Mississippi"],
            "answer": "A"
        },
        {
            "question": "7. Who was the second man in space?",
            "options": ["A. Yuri Gagarin", "B. Alan Shepard", "C. John Glenn", "D. Gherman Titov"],
            "answer": "D"
        },
        {
            "question": "8. What was the second human-made object to reach interstellar space?",
            "options": ["A. Voyager 1", "B. Pioneer 10", "C. Voyager 2", "D. New Horizons"],
            "answer": "C"
        },
        {
            "question": "9. Which is the second most spoken language in the world by native speakers?",
            "options": ["A. English", "B. Spanish", "C. Mandarin", "D. Hindi"],
            "answer": "B"
        },
        {
            "question": "10. What is the second tallest mountain in the world?",
            "options": ["A. Everest", "B. Kangchenjunga", "C. K2", "D. Lhotse"],
            "answer": "C"
        },
    ]

    score = 0
    print("Welcome to the 'Second in History' Quiz!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if user_answer == q["answer"]:
            print("You Are Rocked!\n")
            score += 1
        else:
            print(f"Oops! The correct answer was {q['answer']}.\n")

    print(f"Quiz Over! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz()
