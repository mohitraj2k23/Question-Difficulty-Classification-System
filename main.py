def classify(question):
    q = question.lower()

    # HARD conditions
    if " and " in q:
        return "Hard"
    
    if any(word in q for word in ["derive", "design", "analyze", "prove", "compare"]):
        return "Hard"

    # EASY conditions
    if any(word in q for word in ["define", "what is", "list", "name"]):
        return "Easy"

    # MEDIUM conditions
    if any(word in q for word in ["explain", "describe", "calculate", "how"]):
        return "Medium"

    # Default
    return "Medium"


# Test the function
if __name__ == "__main__":
    while True:
        question = input("Enter your question: ")
        result = classify(question)
        print({"difficulty": result})
