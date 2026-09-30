# AI-Powered Digital Twin for Predictive Maintenance and Failure Simulation of a CNC Milling Machine

## Project Overview

This project develops an AI-powered digital twin for monitoring the condition of a CNC milling machine using sensor data.

The system performs data preprocessing, anomaly detection, machine monitoring, failure simulation, and maintenance recommendation through an interactive dashboard.

## Objectives

- Monitor CNC machine sensor parameters
- Clean and preprocess machine data
- Detect abnormal machine conditions
- Visualize machine parameters
- Simulate abnormal machine conditions
- Generate maintenance alerts
- Display machine health status

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib

## Machine Learning Model

### Isolation Forest

Isolation Forest is used for unsupervised anomaly detection.

It identifies unusual patterns in CNC machine sensor data and classifies observations as Normal or Abnormal.

## Project Workflow

Dataset  
↓  
Data Preprocessing  
↓  
Cleaned Data  
↓  
Isolation Forest  
↓  
Anomaly Detection  
↓  
Digital Twin Dashboard  
↓  
Failure Simulation  
↓  
Maintenance Alert

## Dataset Parameters

The dataset contains CNC machine sensor parameters such as:

- Actual Position
- Actual Velocity
- Actual Acceleration
- Command Position
- Command Velocity
- Command Acceleration
- Current Feedback
- DC Bus Voltage
- Output Current
- Output Voltage

## Main Features

### 1. Data Preprocessing
The dataset is cleaned by removing duplicate records and handling missing values.

### 2. Anomaly Detection
Isolation Forest detects unusual sensor patterns.

### 3. Digital Twin Dashboard
A Streamlit dashboard displays machine parameters and machine status.

### 4. Failure Simulation
The dashboard allows simulated changes to selected machine parameters to demonstrate abnormal conditions.

### 5. Maintenance Alert
The system displays a maintenance alert when a simulated abnormal condition is detected.

### 6. Machine Health Score
The dashboard displays a machine condition score based on the detected machine status.

## How to Run

Install the required libraries:

```bash
python -m pip install pandas scikit-learn streamlit
