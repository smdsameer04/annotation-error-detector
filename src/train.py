import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from features import extract_features
import joblib

print("🚀 Training started...")

# load dataset
df = pd.read_csv("data/dataset.csv")

# prepare features
X = df[["x", "y", "w", "h"]].values
X = [extract_features(row) for row in X]
y = df["label"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# evaluate
acc = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {acc:.2f}")

# save model
joblib.dump(model, "model.pkl")
print("💾 Model saved as model.pkl")

print("🎉 Training finished!")