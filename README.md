# 🌦️ ETSP Weather Prediction System

An interactive, machine-learning-based Weather Prediction Dashboard that provides real-time weather information, hourly forecasts, 5-day forecasts, and AI-based temperature prediction using a Neural Network.

---

## 🚀 Features

* **Search weather by city name:** Automatic geolocation using Open-Meteo Geocoding API.
* **Current weather conditions:** Real-time visibility, temperature, humidity, and wind speed tracking.
* **Hourly weather updates:** View immediate forecasts for upcoming hours.
* **5-Day weather forecast:** Daily breakdowns including weather codes and high/low temperature ranges.
* **AI temperature prediction:** Uses `MLPRegressor` (Multi-Layer Perceptron artificial neural network) to predict next-day values.
* **Interactive dashboard:** Beautifully designed web dashboard built entirely with Streamlit.

---

## 🛠️ Technologies Used

### 💻 Programming Language
* Python

### 🌐 Libraries & Frameworks
* **Streamlit:** Frontend web app framework.
* **Requests:** Seamless Open-Meteo API data retrieval.
* **scikit-learn:** AI scaling (`MinMaxScaler`) and Machine Learning prediction (`MLPRegressor`).
* **NumPy:** Linear algebra and data processing.

### 🤖 Machine Learning
* Artificial Neural Networks (ANN)
* MLPRegressor
* MinMaxScaler

### 🛰️ APIs
* Open-Meteo Weather API
* Open-Meteo Geocoding API

---

## 📂 Project Structure

```text
weather-prediction/
├── WeatherPrediction.py
├── README.md
└── requirements.txt

```

---

## 💿 Installation

### 1. Clone Repository

```bash
git clone [(https://github.com/thuvara23/Weather-Prediction-System)]
cd WeatherPrediction

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

*Or install manually:*

```bash
pip install streamlit requests numpy scikit-learn

```

### 3. Run the Application

```bash
streamlit run WeatherPrediction.py

```

The application will start in your browser at:
`http://localhost:8501`

---

## 🧠 Machine Learning Model

The system uses a Multi-Layer Perceptron Regressor (`MLPRegressor`) from Scikit-Learn to estimate the next temperature value based on the current temperature.

### ⚙️ Configuration

```python
model = MLPRegressor(
    hidden_layer_sizes=(64, 32),
    max_iter=2000,
    random_state=42
)

```

1. **Fetch:** Current weather data is fetched from Open-Meteo API.
2. **Scale:** Temperature values are scaled using `MinMaxScaler`.
3. **Train:** MLP neural network model is trained on sample temperature data.
4. **Predict:** Climate temperature prediction is generated.
5. **Display:** Results are displayed on the Streamlit dashboard.

---

## 📊 Dashboard Modules

* **Current Weather:** Temperature, humidity, wind speed, and weather condition.
* **AI Prediction:** Neural Network-based temperature forecasting.
* **Hourly Forecast:** Hourly temperature updates and precipitation probability.
* **5-Day Forecast:** Maximum & minimum temperature and weather conditions.

---

## 📸 Application Preview

<img width="1911" height="1020" alt="Screenshot 2026-10-29 201916" src="https://github.com/user-attachments/assets/14db9cb4-9015-4529-94e2-3f818b0ee699" />



---

## 🔮 Future Enhancements

* Deep Learning using TensorFlow/Keras
* Weather Forecasting using LSTM Networks
* Historical Weather Analysis
* Data Visualization Charts
* Rainfall Prediction
* Weather Alerts and Notifications
* Multiple Location Comparison

---

## 🎓 Learning Outcomes

This project demonstrates:

* API Integration
* Data Preprocessing
* Machine Learning
* Neural Networks
* Weather Forecasting
* Streamlit Dashboard Development
* Real-Time Data Handling

---
