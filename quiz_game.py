questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Chennai", "C. New Delhi", "D. Kolkata"],
        "answer": "C"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    }
]

score = 0

print("================================")
print("         PYTHON QUIZ GAME")
print("================================")

for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong answer!")

print("\n================================")
print("             RESULT")
print("================================")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! 🏆")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")