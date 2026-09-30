import pandas as pd
import streamlit as st

# Load anomaly results
data = pd.read_csv("data/anomaly_results.csv")

st.title("AI-Powered CNC Milling Machine Digital Twin")

st.subheader("Machine Monitoring")

# Get latest sensor values
latest = data.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Actual Velocity",
        round(latest["X1_ActualVelocity"], 2)
    )

with col2:
    st.metric(
        "Actual Acceleration",
        round(latest["X1_ActualAcceleration"], 2)
    )

with col3:
    st.metric(
        "Output Current",
        round(latest["X1_OutputCurrent"], 2)
    )

# Current machine status
status = latest["Machine_Status"]
# Machine Health Score

if status == "Normal":
    health_score = 100
else:
    health_score = 50

st.subheader("Machine Health Score")
# Maintenance Recommendation

st.subheader("Maintenance Recommendation")

if status == "Normal":
    st.success("Recommendation: Continue normal machine monitoring.")
else:
    st.warning("Recommendation: Inspect machine condition and schedule maintenance.")

st.progress(health_score / 100)

st.write(f"Health Score: {health_score}%")

st.subheader("Current Machine Status")

if status == "Normal":
    st.success("Machine Status: NORMAL")
else:
    st.error("Machine Status: ABNORMAL")


# ------------------------------------------------
# FAILURE SIMULATION
# ------------------------------------------------

st.subheader("Failure Simulation")

simulation = st.checkbox("Enable Failure Simulation")

if simulation:

    st.warning("Failure simulation is ON")

    # Simulation controls
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

    # Create simulated values
    simulated_current = (
        latest["X1_OutputCurrent"]
        * (1 + current_increase / 100)
    )

    simulated_acceleration = (
        latest["X1_ActualAcceleration"]
        * (1 + acceleration_increase / 100)
    )

    st.subheader("Simulated Machine Parameters")

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "Simulated Output Current",
            round(simulated_current, 2)
        )

    with col5:
        st.metric(
            "Simulated Acceleration",
            round(simulated_acceleration, 2)
        )

    # Simple simulated failure condition
    if current_increase >= 50 or acceleration_increase >= 50:
        st.error("⚠ SIMULATED ABNORMAL CONDITION")
        st.warning("Maintenance Alert: Machine requires inspection")
    else:
        st.info("Machine condition is within simulated range.")

else:
    st.info("Failure Simulation is OFF")


# ------------------------------------------------
# SENSOR GRAPHS
# ------------------------------------------------

st.subheader("Sensor Data")

st.line_chart(
    data[
        [
            "X1_ActualVelocity",
            "X1_ActualAcceleration",
            "X1_OutputCurrent"
        ]
    ]
)