import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="CNC Digital Twin",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("data/anomaly_results.csv")
training_data = pd.read_csv("data/cnc_machine_dataset.csv")

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

# ---------------- RANDOM FOREST MODEL ----------------
X = training_data[features]

y = training_data["Machine_Status"].map({
    "Normal": 0,
    "Abnormal": 1
})

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Latest machine data
latest_data = data[features].iloc[[-1]]

prediction = model.predict(latest_data)[0]
probabilities = model.predict_proba(latest_data)[0]

normal_probability = probabilities[0] * 100
abnormal_probability = probabilities[1] * 100

if prediction == 0:
    status = "Normal"
else:
    status = "Abnormal"

# ---------------- SENSOR VALUES ----------------
temperature = data["Temperature"].iloc[-1]
vibration = data["Vibration"].iloc[-1]
current = data["OutputCurrent"].iloc[-1]

# ---------------- TITLE ----------------
st.title("AI-Powered Digital Twin for CNC Milling Machine")
st.subheader("Predictive Maintenance and Failure Simulation")

# ---------------- MACHINE STATUS ----------------
st.header("Machine Status")

if status == "Normal":
    st.success("Machine Status: NORMAL")
else:
    st.error("Machine Status: ABNORMAL")

# ---------------- PREDICTION CONFIDENCE ----------------
st.header("Prediction Confidence")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Normal Probability",
        f"{normal_probability:.2f}%"
    )

with col2:
    st.metric(
        "Abnormal Probability",
        f"{abnormal_probability:.2f}%"
    )

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

# ---------------- SENSOR STATUS ----------------
st.header("Sensor Status")

col1, col2, col3 = st.columns(3)

with col1:
    if temperature > 45:
        st.error(f"Temperature: HIGH ({temperature:.2f})")
    else:
        st.success(f"Temperature: NORMAL ({temperature:.2f})")

with col2:
    if vibration > 2.5:
        st.error(f"Vibration: HIGH ({vibration:.2f})")
    else:
        st.success(f"Vibration: NORMAL ({vibration:.2f})")

with col3:
    if current > 6:
        st.error(f"Output Current: HIGH ({current:.2f})")
    else:
        st.success(f"Output Current: NORMAL ({current:.2f})")

# ---------------- HEALTH SCORE ----------------
st.header("Machine Health Score")

health_score = 100

if temperature > 45:
    health_score -= 20

if vibration > 2.5:
    health_score -= 20

if current > 6:
    health_score -= 20

health_score = max(0, health_score)

st.progress(health_score / 100)
st.write(f"Health Score: {health_score}%")

# ---------------- MAINTENANCE ----------------
st.header("Maintenance Recommendation")

if health_score >= 80:
    st.success(
        "Machine condition is good. Continue normal monitoring."
    )
elif health_score >= 50:
    st.warning(
        "Warning: Inspect machine condition and monitor sensors."
    )
else:
    st.error(
        "Critical: Machine requires immediate inspection and maintenance."
    )

# ---------------- FAILURE SIMULATION ----------------
# ---------------- FAILURE SIMULATION ----------------
st.header("Failure Simulation")

simulate = st.checkbox("Enable Failure Simulation")

if simulate:

    st.subheader("Simulate Machine Failure Conditions")

    current_increase = st.slider(
        "Output Current Increase (%)",
        0,
        100,
        30
    )

    acceleration_increase = st.slider(
        "Acceleration Increase (%)",
        0,
        100,
        30
    )

    vibration_increase = st.slider(
        "Vibration Increase (%)",
        0,
        100,
        20
    )

    temperature_increase = st.slider(
        "Temperature Increase (%)",
        0,
        100,
        20
    )

    # Current sensor values
    current_value = data["OutputCurrent"].iloc[-1]
    acceleration_value = data["ActualAcceleration"].iloc[-1]
    vibration_value = data["Vibration"].iloc[-1]
    temperature_value = data["Temperature"].iloc[-1]

    # Simulated values
    simulated_current = current_value * (
        1 + current_increase / 100
    )

    simulated_acceleration = acceleration_value * (
        1 + acceleration_increase / 100
    )

    simulated_vibration = vibration_value * (
        1 + vibration_increase / 100
    )

    simulated_temperature = temperature_value * (
        1 + temperature_increase / 100
    )

    # Display simulated values
    st.subheader("Simulated Sensor Values")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Simulated Output Current",
            f"{simulated_current:.2f}"
        )

        st.metric(
            "Simulated Acceleration",
            f"{simulated_acceleration:.2f}"
        )

    with col2:
        st.metric(
            "Simulated Vibration",
            f"{simulated_vibration:.2f}"
        )

        st.metric(
            "Simulated Temperature",
            f"{simulated_temperature:.2f}"
        )

    # Calculate simulated health
    simulated_health = 100

    if simulated_temperature > 45:
        simulated_health -= 20

    if simulated_vibration > 2.5:
        simulated_health -= 20

    if simulated_current > 6:
        simulated_health -= 20

    if simulated_acceleration > 4:
        simulated_health -= 20

    simulated_health = max(0, simulated_health)

    st.subheader("Simulated Machine Health")

    st.progress(simulated_health / 100)

    st.write(
        f"Simulated Health Score: {simulated_health}%"
    )

    # Simulated machine status
    if simulated_health >= 80:
        st.success("Simulated Status: NORMAL")

    elif simulated_health >= 50:
        st.warning("Simulated Status: WARNING")

    else:
        st.error("Simulated Status: CRITICAL")

    st.info(
        "This simulation changes sensor values only in software "
        "and does not control or modify a real CNC machine."
    )
# ---------------- FEATURE IMPORTANCE ----------------
st.header("Random Forest Feature Importance")

importance_data = pd.DataFrame({
    "Sensor": features,
    "Importance": model.feature_importances_
})

importance_data = importance_data.sort_values(
    "Importance",
    ascending=False
)

st.bar_chart(
    importance_data.set_index("Sensor")
)
# ---------------- DIGITAL TWIN INFO ----------------
st.header("Digital Twin")

st.info(
    "The digital twin monitors CNC machine sensor parameters, "
    "uses a Random Forest model to classify machine condition, "
    "displays prediction confidence, and simulates abnormal "
    "conditions for predictive maintenance."
)