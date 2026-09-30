import pandas as pd
from sklearn.ensemble import IsolationForest

# Load cleaned data
data = pd.read_csv("data/cleaned_cnc_data.csv")

# Select sensor features
features = [
    "X1_ActualPosition",
    "X1_ActualVelocity",
    "X1_ActualAcceleration",
    "X1_CommandPosition",
    "X1_CommandVelocity",
    "X1_CommandAcceleration",
    "X1_CurrentFeedback",
    "X1_DCBusVoltage",
    "X1_OutputCurrent",
    "X1_OutputVoltage"
]

X = data[features]

# Create anomaly detection model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Predict machine condition
data["Anomaly"] = model.fit_predict(X)

# Convert result to readable labels
data["Machine_Status"] = data["Anomaly"].map({
    1: "Normal",
    -1: "Abnormal"
})

print("Anomaly detection completed!")

print("\nMachine Status:")
print(data["Machine_Status"].value_counts())

# Save result
data.to_csv("data/anomaly_results.csv", index=False)

print("\nSaved as: data/anomaly_results.csv")