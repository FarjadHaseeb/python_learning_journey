questions = {
    "What is the output type of input()? ": "str",
    "Which keyword defines a function? ": "def",
    "What is 2 ** 3? ": "8"
}

score = 0

for question, answer in questions.items():
    if input(question).strip().lower() == answer:
        score += 1

print(f"Score: {score}/{len(questions)}")
