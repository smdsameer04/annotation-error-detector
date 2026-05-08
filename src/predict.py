import joblib
from features import extract_features

model = joblib.load("model.pkl")

test_boxes = [
    (100, 80, 200, 150),
    (10, 10, 400, 400)
]

for box in test_boxes:
    features = extract_features(box)
    pred = model.predict([features])[0]

    result = "Correct" if pred == 1 else "Incorrect"
    print(f"Box {box} → {result}")