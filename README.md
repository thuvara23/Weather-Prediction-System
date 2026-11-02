# 🌦️ ETSP Weather Prediction System

An interactive, machine-learning-based Weather Prediction Dashboard that provides real-time weather information, hourly forecasts, 5-day forecasts, and AI-based temperature prediction using a Neural Network[cite: 1].

---

## 🚀 Features

* **Search weather by city name:** Automatic geolocation using Open-Meteo Geocoding API[cite: 1].
* **Current weather conditions:** Real-time visibility, temperature, humidity, and wind speed tracking[cite: 1].
* **Hourly weather updates:** View immediate forecasts for upcoming hours[cite: 1].
* **5-Day weather forecast:** Daily breakdowns including weather codes and high/low temperature ranges[cite: 1].
* **AI temperature prediction:** Uses `MLPRegressor` (Multi-Layer Perceptron artificial neural network) to predict next-day values[cite: 1].
* **Interactive dashboard:** Beautifully designed web dashboard built entirely with Streamlit[cite: 1].

---

## 🛠️ Technologies Used

### 💻 Programming Language
* Python

### 🌐 Libraries & Frameworks
* **Streamlit:** Frontend web app framework[cite: 1].
* **Requests:** Seamless Open-Meteo API data retrieval[cite: 1].
* **scikit-learn:** AI scaling (`MinMaxScaler`) and Machine Learning prediction (`MLPRegressor`)[cite: 1].
* **NumPy:** Linear algebra and data processing[cite: 1].

### 🤖 Machine Learning
* Artificial Neural Networks (ANN)[cite: 1]
* MLPRegressor[cite: 1]
* MinMaxScaler[cite: 1]

### 🛰️ APIs
* Open-Meteo Weather API[cite: 1]
* Open-Meteo Geocoding API[cite: 1]

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
git clone [https://github.com/your-username/WeatherPrediction.git](https://github.com/your-username/WeatherPrediction.git)
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

The system uses a Multi-Layer Perceptron Regressor (`MLPRegressor`)[cite: 1] from Scikit-Learn to estimate the next temperature value based on the current temperature.

### ⚙️ Configuration

```python
model = MLPRegressor(
    hidden_layer_sizes=(64, 32),
    max_iter=2000,
    random_state=42
)

```

1. **Fetch:** Current weather data is fetched from Open-Meteo API[cite: 1].
2. **Scale:** Temperature values are scaled using `MinMaxScaler`[cite: 1].
3. **Train:** MLP neural network model is trained on sample temperature data[cite: 1].
4. **Predict:** Climate temperature prediction is generated[cite: 1].
5. **Display:** Results are displayed on the Streamlit dashboard[cite: 1].

---

## 📊 Dashboard Modules

* **Current Weather:** Temperature, humidity, wind speed, and weather condition[cite: 1].
* **AI Prediction:** Neural Network-based temperature forecasting[cite: 1].
* **Hourly Forecast:** Hourly temperature updates and precipitation probability[cite: 1].
* **5-Day Forecast:** Maximum & minimum temperature and weather conditions[cite: 1].

---

## 📸 Application Preview

*Insert your screenshots here:*


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
