# 🏨 Hotel Room Booking Predictor

An AI-powered hotel room booking predictor built using Streamlit. This application uses a trained machine learning model (XGBoost) to predict the number of room bookings for a given date based on historical data.

## 🛠️ Features

✅ Predicts hotel room bookings based on date selection  
✅ Uses a trained XGBoost model for accurate predictions  
✅ Interactive Streamlit UI for ease of use  
✅ Visualization of historical booking trends  
✅ Reads data from an Excel file for flexible data management  

## 📂 Project Structure

```bash
hotel-booking-predictor/
├── app.py                 # Main Streamlit application
├── room_bookings.xlsx     # Historical hotel booking data
├── xgb_model.pkl          # Trained XGBoost model
├── requirements.txt       # List of dependencies
├── README.md              # Documentation
└── .gitignore             # Ignore unnecessary files
```

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/hotel-booking-predictor.git
cd hotel-booking-predictor
```

### 2️⃣ Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 🖥️ Running Locally

### 🔹 Start Streamlit Application

```bash
streamlit run app.py
```

Your UI will be available at:

👉 http://localhost:8501

## 📊 How It Works

1️⃣ The app loads historical hotel booking data from `room_bookings.xlsx`.  
2️⃣ It loads a pre-trained XGBoost model from `xgb_model.pkl`.  
3️⃣ The user selects a date in the Streamlit UI.  
4️⃣ The app predicts the number of bookings for the selected date.  
5️⃣ A line chart visualizes historical booking trends.  

## 🌍 Deployment

### 4️⃣ Deploy on Streamlit Cloud

1. Push the project to GitHub.
2. Go to Streamlit Cloud → Click "Deploy an App".
3. Select your GitHub repository.
4. Set the main file path to `app.py`.
5. Deploy and share your app link.

## 🔧 Troubleshooting

💡 **Issue: Model Not Found**  
✔️ Ensure `xgb_model.pkl` exists in the project directory.  
✔️ Retrain the model if necessary and save it as `xgb_model.pkl`.  

💡 **Issue: Missing Dependencies**  
✔️ Run `pip install -r requirements.txt`.  
✔️ Ensure the virtual environment is activated.  

## 🛡️ License

This project is open-source under the MIT License.

## 📩 Contact & Contributions

🔹 Feel free to fork this repo & contribute!  
🔹 Found a bug? Create an issue on GitHub.  
🔹 Questions? Reach out via email: venkatsaimacha123@gmail.com  

🚀 Built with ❤️ using Streamlit 🚀

