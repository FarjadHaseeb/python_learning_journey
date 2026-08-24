import csv
from pathlib import Path

DATA_FILE = Path("students.csv")

def create_sample_data():
    rows = [
        ["name", "python", "math", "attendance"],
        ["Ali", 85, 78, 92],
        ["Sara", 94, 89, 97],
        ["Hamza", 72, 75, 81],
        ["Ayesha", 88, 91, 95],
    ]
    with DATA_FILE.open("w", newline="") as f:
        csv.writer(f).writerows(rows)

def analyze():
    if not DATA_FILE.exists():
        create_sample_data()

    with DATA_FILE.open(newline="") as f:
        students = list(csv.DictReader(f))

    for student in students:
        score = (
            float(student["python"]) * 0.4 +
            float(student["math"]) * 0.4 +
            float(student["attendance"]) * 0.2
        )
        student["score"] = score

    students.sort(key=lambda x: x["score"], reverse=True)

    print("Student Performance Report")
    print("-" * 30)

    for student in students:
        print(f'{student["name"]}: {student["score"]:.2f}')

    print("\nTop student:", students[0]["name"])

if __name__ == "__main__":
    analyze()
