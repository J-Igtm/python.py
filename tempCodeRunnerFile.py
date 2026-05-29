import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# CSV load
data = pd.read_csv("house.csv")

# Show data
print(data)

# Inputs
X = data[["Area", "Rooms"]]

# Output
y = data["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)

print("Accuracy =", score)

# User input
area = int(input("Enter house area: "))
rooms = int(input("Enter number of rooms: "))

# Prediction
prediction = model.predict([[area, rooms]])

# Output
print("Predicted House Price =", prediction[0])