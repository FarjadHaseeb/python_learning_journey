try:
    import pandas as pd
except ImportError:
    print("Install pandas with: pip install pandas")
    raise

data = {
    "student": ["Ali", "Sara", "Hamza", "Ayesha"],
    "marks": [82, 91, 74, 88]
}

df = pd.DataFrame(data)
print(df)
print("\nAverage:", df["marks"].mean())
print("\nTop student:")
print(df.loc[df["marks"].idxmax()])
