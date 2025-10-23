# model_comparison_challenge.py
# Day 6 of #75AIEngineeringChallenge
# Author: Gabriel

import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import os

# ============================
# Step 1: Load the Iris dataset
# ============================
iris = load_iris()
X, y = iris.data, iris.target

# Train-test split for proper model training (though we’ll use test_samples later)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# ============================
# Step 2: Define and train models
# ============================
models = {
    "decision_tree_model.pkl": DecisionTreeClassifier(random_state=42),
    "logistic_regression_model.pkl": LogisticRegression(max_iter=200),
    "random_forest_model.pkl": RandomForestClassifier(n_estimators=100, random_state=42),
    "svm_model.pkl": SVC(probability=True, random_state=42),
    "knn_model.pkl": KNeighborsClassifier(n_neighbors=5)
}

# Train and save each model
for filename, model in models.items():
    model.fit(X_train, y_train)
    with open(filename, "wb") as file:
        pickle.dump(model, file)

print(" Models trained and saved successfully.\n")

# ============================
# Step 3: Define test data
# ============================
test_samples = [
    [5.1, 3.5, 1.4, 0.2],
    [6.2, 2.9, 4.3, 1.3],
    [7.3, 3.0, 6.3, 1.8],
    [4.9, 3.1, 1.5, 0.1],
    [5.8, 2.7, 5.1, 1.9],
    [6.3, 3.3, 4.7, 1.6],
    [5.0, 3.4, 1.5, 0.2],
    [6.7, 3.1, 5.6, 2.4],
    [5.5, 2.4, 3.8, 1.1],
    [7.7, 3.0, 6.1, 2.3]
]

true_labels = [0, 1, 2, 0, 2, 1, 0, 2, 1, 2]

# ============================
# Step 4: Load models and evaluate
# ============================
results = {}

for filename in models.keys():
    try:
        with open(filename, "rb") as file:
            model = pickle.load(file)
        
        predictions = model.predict(test_samples)
        accuracy = accuracy_score(true_labels, predictions)
        correct_preds = sum(predictions == true_labels)
        
        results[filename] = {
            "correct_predictions": correct_preds,
            "accuracy": accuracy * 100
        }

    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")

# ============================
# Step 5: Display results
# ============================
print(" Model Performance Comparison\n")
for model_name, info in results.items():
    print(f"{model_name.replace('_model.pkl','').title()}: "
          f"{info['correct_predictions']} correct | "
          f"Accuracy: {info['accuracy']:.2f}%")

# Identify best and worst models
best_model = max(results, key=lambda x: results[x]['accuracy'])
worst_model = min(results, key=lambda x: results[x]['accuracy'])

best_correct = results[best_model]['correct_predictions']
worst_correct = results[worst_model]['correct_predictions']

# ============================
# Step 6: Combined results
# ============================
total_correct = sum(info['correct_predictions'] for info in results.values())
total_predictions = len(results) * len(test_samples)
overall_accuracy = (total_correct / total_predictions) * 100

print("\n🔥 Summary:")
print(f"Best Model: {best_model.replace('_model.pkl','').title()} ({best_correct}/10)")
print(f"Worst Model: {worst_model.replace('_model.pkl','').title()} ({worst_correct}/10)")
print(f"Total Correct Predictions (All Models): {total_correct}/50")
print(f"Overall Accuracy Across All Models: {overall_accuracy:.2f}%")

# ============================
# Step 7: Final Answer Formula
# ============================
final_answer = (best_correct * 100) + total_correct + (worst_correct * 10)

print(f"\n Final Answer: {final_answer}")
  