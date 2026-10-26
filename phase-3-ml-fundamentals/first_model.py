"""Phase 3 starter: train and evaluate a first classifier with scikit-learn.

Run:  python phase-3-ml-fundamentals/first_model.py
"""

from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# 1. Data: features X (numbers describing each example) and labels y (the answer)
data = load_breast_cancer()
X, y = data.data, data.target
print(f"{X.shape[0]} examples, {X.shape[1]} features")

# 2. Split. The test set is locked away until the very end.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Baseline: always predict the most common class. Any real model must beat this.
baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
print(f"\nBaseline accuracy: {baseline.score(X_test, y_test):.3f}")

# 4. Candidate models, compared with cross-validation on the TRAINING set only
models = {
    "logistic_regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "random_forest": RandomForestClassifier(n_estimators=200, random_state=42),
}
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
    print(f"{name}: cross-val F1 = {scores.mean():.3f} (+/- {scores.std():.3f})")

# 5. Pick the best, fit on all training data, and evaluate on the test set ONCE
best = models["logistic_regression"]
best.fit(X_train, y_train)
pred = best.predict(X_test)

print("\nTest-set results")
print(classification_report(y_test, pred, target_names=data.target_names))
print("Confusion matrix (rows = true, columns = predicted):")
print(confusion_matrix(y_test, pred))

# ----------------------------------------------------------------------
# YOUR TURN:
# 1. Change test_size to 0.5 and then 0.05. What happens to the scores, and why?
# 2. Remove stratify=y. Does anything change?
# 3. Which kind of mistake (false positive or false negative) is worse for this
#    dataset? Which metric should you watch?
# 4. Try a DecisionTreeClassifier with max_depth=None, and compare its train score
#    to its test score. That gap is overfitting.
# ----------------------------------------------------------------------
