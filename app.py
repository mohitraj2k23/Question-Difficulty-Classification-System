from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# -----------------------------
# 📚 Training Dataset (Expandable)
# -----------------------------
questions = [
    "What is voltage?",
    "Define energy",
    "List types of actuators",
    "Explain Ohm's Law",
    "Explain energy conservation",
    "Describe working of motor",
    "Calculate current in circuit",
    "How does a generator work",
    "Derive Ohm's Law",
    "Design a power supply",
    "Analyze system stability",
    "Compare AC and DC circuits",
    "Explain and calculate resistance",
    "Prove Kirchhoff's law",
    "Design and analyze amplifier"
]

labels = [
    "Easy","Easy","Easy",
    "Medium","Medium","Medium","Medium","Medium",
    "Hard","Hard","Hard","Hard","Hard","Hard","Hard"
]

# -----------------------------
# 🤖 ML Model Training
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = LogisticRegression()
model.fit(X, labels)

# -----------------------------
# 🧠 Rule-Based Logic (Hybrid)
# -----------------------------
def classify_with_rules(question):
    q = question.lower()

    if " and " in q:
        return "Hard"

    if any(word in q for word in ["design", "analyze", "prove", "derive"]):
        return "Hard"

    if any(word in q for word in ["explain", "describe", "calculate", "how"]):
        return "Medium"

    if any(word in q for word in ["what", "define", "list"]):
        return "Easy"

    return None

# -----------------------------
# 🌐 API Route
# -----------------------------
@app.route('/')
def home():
    return "✅ API is running. Use /predict endpoint."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    question = data.get("question", "")

    # Safety check
    if question.strip() == "":
        return jsonify({"difficulty": "Medium"})

    # Rule-based prediction first
    rule_result = classify_with_rules(question)
    if rule_result:
        return jsonify({"difficulty": rule_result})

    # ML prediction
    q_vec = vectorizer.transform([question])
    prediction = model.predict(q_vec)[0]

    return jsonify({"difficulty": prediction})

# -----------------------------
# ▶ Run Server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
