import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load our self-created CNC dataset
data = pd.read_csv("data/cnc_machine_dataset.csv")

# Input features
features = [
    "ActualPosition",
    "ActualVelocity",
    "ActualAcceleration",
    "CurrentFeedback",
    "DCBusVoltage",
    "OutputCurrent",
    "OutputVoltage",
    "Vibration",
    "Temperature",
    "SpindleSpeed"
]

# Input and target
X = data[features]
y = data["Machine_Status"]

# Convert target labels into numbers
y = y.map({
    "Normal": 0,
    "Abnormal": 1
})

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Random Forest training completed!")

print("\nAccuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Normal", "Abnormal"]
))

# Predict machine status for complete dataset
data["Prediction"] = model.predict(X)

data["Predicted_Status"] = data["Prediction"].map({
    0: "Normal",
    1: "Abnormal"
})

print("\nPredicted Machine Status:")
print(data["Predicted_Status"].value_counts())

# Save results
data.to_csv("data/anomaly_results.csv", index=False)

print("\nResults saved as: data/anomaly_results.csv")
