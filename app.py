import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib


# Load dataset
def load_data():
    file_path = "room_bookings.xlsx"
    df = pd.read_excel(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.day
    df["Weekday"] = df["Date"].dt.weekday
    return df

# Load trained model
def load_model():
    try:
        model = joblib.load("xgb_model.pkl")
    except:
        df = load_data()
    return model

# Predict function
def predict_bookings(model, input_date):
    date_obj = pd.to_datetime(input_date)
    features = pd.DataFrame({
        "Month": [date_obj.month],
        "Day": [date_obj.day],
        "Weekday": [date_obj.weekday()],
    })
    return model.predict(features)[0]

# Streamlit UI
st.title("🏨 Hotel Room Booking Predictor")

# Load dataset and model
df = load_data()
model = load_model()

# User input for prediction
input_date = st.date_input("📅 Select a date:", datetime.date(2025, 1, 1))

if st.button("🔮 Predict Bookings"):
    prediction = predict_bookings(model, input_date)
    st.write(f"### 📊 Predicted Room Bookings: {round(prediction)}")

# Visualization
df["Year-Month"] = df["Date"].dt.strftime("%Y-%m")  # Convert to string format (YYYY-MM)
monthly_avg = df.groupby("Year-Month")["Total Bookings"].mean().reset_index()

# Streamlit line chart
st.line_chart(data=monthly_avg, x="Year-Month", y="Total Bookings")


