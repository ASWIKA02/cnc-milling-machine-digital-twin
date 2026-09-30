import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/experiment_02-selected-columns.csv"

data = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape:", data.shape)

# Plot Actual Velocity
plt.figure(figsize=(10, 5))
plt.plot(data["X1_ActualVelocity"])
plt.title("CNC Actual Velocity")
plt.xlabel("Sample")
plt.ylabel("Velocity")
plt.grid()
plt.show()

# Plot Actual Acceleration
plt.figure(figsize=(10, 5))
plt.plot(data["X1_ActualAcceleration"])
plt.title("CNC Actual Acceleration")
plt.xlabel("Sample")
plt.ylabel("Acceleration")
plt.grid()
plt.show()

# Plot Output Current
plt.figure(figsize=(10, 5))
plt.plot(data["X1_OutputCurrent"])
plt.title("CNC Output Current")
plt.xlabel("Sample")
plt.ylabel("Current")
plt.grid()
plt.show()
