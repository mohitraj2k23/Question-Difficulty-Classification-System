from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# 📚 Dataset
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
# 🤖 ML Model
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = LogisticRegression()
model.fit(X, labels)

# -----------------------------
# 🧠 Rule-Based Logic
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
# 🌐 Routes
# -----------------------------
@app.route('/')
def home():
    return "✅ API is running. Use /predict endpoint."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    question = data.get("question", "")

    if question.strip() == "":
        return jsonify({"difficulty": "Medium"})

    # Rule first
    rule_result = classify_with_rules(question)
    if rule_result:
        return jsonify({"difficulty": rule_result})

    # ML fallback
    q_vec = vectorizer.transform([question])
    prediction = model.predict(q_vec)[0]

    return jsonify({"difficulty": prediction})

# -----------------------------
# ▶ Run Server (Production Ready)
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
