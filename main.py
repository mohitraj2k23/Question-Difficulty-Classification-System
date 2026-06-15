def classify(question):
    q = question.lower()

    # HARD conditions
    if " and " in q or any(word in q for word in ["derive", "design", "analyze", "prove", "compare"]):
        return "Hard"

    # EASY conditions
    elif any(word in q for word in ["define", "what is", "list", "name"]):
        return "Easy"

    # MEDIUM conditions
    elif any(word in q for word in ["explain", "describe", "calculate", "how"]):
        return "Medium"

    return "Medium"


if __name__ == "__main__":
    while True:
        question = input("\nEnter your question (or type 'exit'): ")

        if question.lower() == "exit":
            print("Exiting...")
            break

        result = classify(question)
        print({"difficulty": result})
