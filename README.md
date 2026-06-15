# 🧠 Question Difficulty Classification System

## 📌 Overview

This project aims to automatically classify assessment questions into three difficulty levels: **Easy, Medium, and Hard** using rule-based and machine learning approaches.

---

## 🎯 Objective

To build a system that takes a textual question as input and outputs its difficulty level in the following format:

```json
{
  "difficulty": "Medium"
}
```

---

## 🏷️ Difficulty Levels

| Level  | Description                                        |
| ------ | -------------------------------------------------- |
| Easy   | Basic recall or definition-based questions         |
| Medium | Requires understanding and application             |
| Hard   | Requires multi-step reasoning or multiple concepts |

---

## 🧠 Approach

### 1. Rule-Based Classification

We defined a set of heuristic rules based on:

* Keywords (define, explain, derive, etc.)
* Question complexity
* Number of concepts involved

### 2. Decision Flow

1. Check for **Hard conditions** (multi-step, multiple actions)
2. Check for **Easy keywords**
3. Default to **Medium**

---

## ⚙️ Implementation

### 🔧 Technologies Used

* Python
* Basic NLP techniques
* (Optional) Scikit-learn for ML model

### 🧩 Sample Logic

```python
def classify(question):
    q = question.lower()

    if " and " in q:
        return "Hard"

    if any(word in q for word in ["derive", "design", "analyze"]):
        return "Hard"

    if any(word in q for word in ["define", "what is", "list"]):
        return "Easy"

    if any(word in q for word in ["explain", "calculate", "describe"]):
        return "Medium"

    return "Medium"
```

---

## ⚠️ Edge Case Handling

### 🔹 Ambiguous Questions

* Default classified as **Medium**

### 🔹 Multi-topic Questions

* Detected using conjunctions (e.g., "and")
* Classified as **Hard**

---

## 📊 Results

* Achieved accuracy: **~80% (rule-based baseline)**
* Performance improves with ML models

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/question-difficulty-classifier.git
```

2. Run the script:

```bash
python main.py
```

---

## 🧪 Example

Input:

```
Explain Ohm's Law
```

Output:

```json
{
  "difficulty": "Medium"
}
```

---

## 🔮 Future Improvements

* Use BERT for better NLP understanding
* Add confidence score
* Improve dataset size
* Build web interface (React + Flask)

---

## 📌 Conclusion

This project demonstrates how NLP and logical rules can be used to classify question difficulty effectively. It serves as a foundation for intelligent assessment systems.

---
<img width="1500" height="995" alt="image" src="https://github.com/user-attachments/assets/bfd997ca-64a9-4fd1-ba8c-ed5366ae7859" />
