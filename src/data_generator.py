import random
import pandas as pd
import os

def create_correct_box():
    return (100, 80, 200, 150)

def create_wrong_box(box):
    x, y, w, h = box
    return (
        x + random.randint(-50, 50),
        y + random.randint(-50, 50),
        w + random.randint(-80, 80),
        h + random.randint(-80, 80)
    )

def generate_dataset(n=200):
    data = []

    for _ in range(n):
        correct = create_correct_box()
        wrong = create_wrong_box(correct)

        data.append((*correct, 1))
        data.append((*wrong, 0))

    df = pd.DataFrame(data, columns=["x", "y", "w", "h", "label"])

    # ensure folder exists
    os.makedirs("data", exist_ok=True)

    df.to_csv("data/dataset.csv", index=False)
    print("✅ Dataset created at data/dataset.csv")

# 👇 THIS IS CRITICAL
if __name__ == "__main__":
    print("Running data generator...")
    generate_dataset()