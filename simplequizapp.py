questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What color do you get when you mix red and white?": "Pink",
    "What is the output of 3 * 2?": "6",
    "Which planet is known as the Red Planet?": "Mars"
}

score = 0

print("🧠 Welcome to the Quiz App!")
print("Answer the following questions:\n")

for question, answer in questions.items():
    user_answer = input(f"{question} ").strip()

    if user_answer.lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {answer}\n")

print(f"🎉 Quiz complete! You got {score} out of {len(questions)} correct.")
