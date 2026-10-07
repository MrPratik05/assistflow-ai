from app.graph import classify_intent

# Evaluation dataset
test_cases = [
    # Support questions
    ("What is your refund policy?", "support_question"),
    ("How long does shipping take?", "support_question"),
    ("Can I return an item after delivery?", "support_question"),
    ("How can I reset my password?", "support_question"),
    ("What payment methods do you accept?", "support_question"),
    ("Where is my order?", "support_question"),
    ("Can I change my delivery address?", "support_question"),
    ("How do I create an account?", "support_question"),
    ("When will I receive my refund?", "support_question"),
    ("Do you offer international shipping?", "support_question"),

    # Human escalation
    ("I want to speak to a human.", "human_escalation"),
    ("Can I talk to a support agent?", "human_escalation"),
    ("Please connect me with customer service.", "human_escalation"),
    ("I need to speak with a real person.", "human_escalation"),
    ("Can you escalate this to your support team?", "human_escalation"),

    # Out of scope
    ("What is the weather today?", "out_of_scope"),
    ("Who is the prime minister?", "out_of_scope"),
    ("Write me a Python program.", "out_of_scope"),
    ("What is the capital of France?", "out_of_scope"),
    ("Tell me a joke.", "out_of_scope"),
]


correct = 0
results = []

for question, expected in test_cases:
    state = {
        "question": question,
        "messages": [],
        "intent": "",
        "context": "",
        "answer": "",
    }

    try:
        result = classify_intent(state)
        predicted = result["intent"]
        is_correct = predicted == expected

        if is_correct:
            correct += 1

        results.append((question, expected, predicted, is_correct))

        status = "PASS" if is_correct else "FAIL"

        print(f"\n{status}")
        print(f"Question:  {question}")
        print(f"Expected:  {expected}")
        print(f"Predicted: {predicted}")

    except Exception as e:
        results.append((question, expected, "ERROR", False))

        print("\nERROR")
        print(f"Question: {question}")
        print(f"Error: {e}")


total = len(test_cases)
accuracy = (correct / total) * 100

print("\n" + "=" * 50)
print("ASSISTFLOW AI ROUTING EVALUATION")
print("=" * 50)
print(f"Correct: {correct}/{total}")
print(f"Routing Accuracy: {accuracy:.1f}%")
print("=" * 50)