import pandas as pd
import numpy as np

# Fixed seed for reproducible results
np.random.seed(42)

# Number of samples
n = 1200

# Generate machine conditions
conditions = np.random.choice(
    ["Normal", "Abnormal"],
    size=n,
    p=[0.75, 0.25]
)

data = []

for condition in conditions:

    if condition == "Normal":
        actual_position = np.random.normal(50, 5)
        actual_velocity = np.random.normal(120, 10)
        actual_acceleration = np.random.normal(2.5, 0.5)
        current_feedback = np.random.normal(4.0, 0.7)
        dc_bus_voltage = np.random.normal(310, 8)
        output_current = np.random.normal(4.5, 0.8)
        output_voltage = np.random.normal(220, 5)
        vibration = np.random.normal(1.5, 0.3)
        temperature = np.random.normal(35, 3)
        spindle_speed = np.random.normal(3000, 150)

    else:
        actual_position = np.random.normal(50, 8)
        actual_velocity = np.random.normal(105, 15)
        actual_acceleration = np.random.normal(5.0, 1.0)
        current_feedback = np.random.normal(7.0, 1.2)
        dc_bus_voltage = np.random.normal(290, 15)
        output_current = np.random.normal(8.0, 1.5)
        output_voltage = np.random.normal(210, 10)
        vibration = np.random.normal(3.5, 0.7)
        temperature = np.random.normal(50, 5)
        spindle_speed = np.random.normal(2700, 250)

    data.append([
        actual_position,
        actual_velocity,
        actual_acceleration,
        current_feedback,
        dc_bus_voltage,
        output_current,
        output_voltage,
        vibration,
        temperature,
        spindle_speed,
        condition
    ])

# Create DataFrame
columns = [
    "ActualPosition",
    "ActualVelocity",
    "ActualAcceleration",
    "CurrentFeedback",
    "DCBusVoltage",
    "OutputCurrent",
    "OutputVoltage",
    "Vibration",
    "Temperature",
    "SpindleSpeed",
    "Machine_Status"
]

df = pd.DataFrame(data, columns=columns)

# Save dataset
output_file = "data/cnc_machine_dataset.csv"
df.to_csv(output_file, index=False)

# Display information
print("CNC machine dataset created successfully!")
print("\nDataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMachine Status Count:")
print(df["Machine_Status"].value_counts())

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset saved as:", output_file)