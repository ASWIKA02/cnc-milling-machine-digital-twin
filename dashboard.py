import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CNC Digital Twin",
    layout="wide"
)

# Load Random Forest results
data = pd.read_csv("data/anomaly_results.csv")

st.title("AI-Powered Digital Twin for CNC Milling Machine")
st.subheader("Predictive Maintenance and Failure Simulation")

# Latest machine status from Random Forest
status = data["Predicted_Status"].iloc[-1]

# ---------------- MACHINE STATUS ----------------
st.header("Machine Status")

if status == "Normal":
    st.success("Machine Status: NORMAL")
else:
    st.error("Machine Status: ABNORMAL")

# ---------------- SENSOR DATA ----------------
st.header("Sensor Monitoring")

st.line_chart(
    data[
        [
            "ActualVelocity",
            "ActualAcceleration",
            "OutputCurrent"
        ]
    ]
)

# ---------------- HEALTH SCORE ----------------
st.header("Machine Health Score")

if status == "Normal":
    health_score = 100
else:
    health_score = 50

st.progress(health_score / 100)
st.write(f"Health Score: {health_score}%")

# ---------------- MAINTENANCE ----------------
st.header("Maintenance Recommendation")

if status == "Normal":
    st.success("Continue normal machine monitoring.")
else:
    st.warning("Inspect machine condition and schedule maintenance.")

# ---------------- FAILURE SIMULATION ----------------
st.header("Failure Simulation")

simulate = st.checkbox("Enable Failure Simulation")

if simulate:

    current_increase = st.slider(
        "Simulated Output Current Increase (%)",
        0,
        100,
        30
    )

    acceleration_increase = st.slider(
        "Simulated Acceleration Increase (%)",
        0,
        100,
        30
    )

    current_value = data["OutputCurrent"].iloc[-1]
    acceleration_value = data["ActualAcceleration"].iloc[-1]

    simulated_current = current_value * (1 + current_increase / 100)
    simulated_acceleration = acceleration_value * (1 + acceleration_increase / 100)

    st.write(f"Simulated Output Current: {simulated_current:.2f}")
    st.write(f"Simulated Acceleration: {simulated_acceleration:.2f}")

    if current_increase >= 50 or acceleration_increase >= 50:
        st.error("SIMULATED ABNORMAL CONDITION")
        st.warning("Maintenance Alert: Machine requires inspection.")
    else:
        st.success("Machine condition is within simulated range.")

# ---------------- DIGITAL TWIN INFO ----------------
st.header("Digital Twin")

st.info(
    "The digital twin monitors CNC machine sensor parameters, "
    "uses a Random Forest model to classify machine condition, "
    "and simulates abnormal conditions for predictive maintenance."
)