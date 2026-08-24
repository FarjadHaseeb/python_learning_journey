try:
    from sklearn.linear_model import LinearRegression
    import numpy as np
except ImportError:
    print("Install dependencies with: pip install scikit-learn numpy")
    raise

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[7]])
print("Prediction for 7:", prediction[0])
