import streamlit as st
import requests
import numpy as np
from datetime import datetime

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="ETSP Weather Prediction",
    page_icon="🌦️",
    layout="wide"
)

# ---------------------------
# WEATHER ICONS
# ---------------------------
def get_weather_icon(code):
    if code == 0:
        return "☀️"
    elif code in [1, 2]:
        return "🌤️"
    elif code == 3:
        return "☁️"
    elif code in [51, 53, 55, 61, 63, 65]:
        return "🌧️"
    elif code in [71, 73, 75]:
        return "❄️"
    elif code == 95:
        return "⛈️"
    else:
        return "🌥️"


def get_weather_description(code):
    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Heavy Drizzle",
        61: "Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        81: "Moderate Showers",
        82: "Heavy Showers",
        95: "Thunderstorm"
    }
    return weather_codes.get(code, "Unknown")


# ---------------------------
# LOCATION API
# ---------------------------
def get_location(city):
    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if "results" not in data:
            return None

        result = data["results"][0]

        return (
            result["name"],
            result["latitude"],
            result["longitude"]
        )
    except:
        return None


# ---------------------------
# WEATHER API
# ---------------------------
def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m,"
        f"relative_humidity_2m,"
        f"wind_speed_10m,"
        f"weather_code"
        f"&hourly=temperature_2m,"
        f"precipitation_probability"
        f"&daily=weather_code,"
        f"temperature_2m_max,"
        f"temperature_2m_min"
        f"&forecast_days=5"
        f"&timezone=auto"
    )

    response = requests.get(url)
    return response.json()


# ---------------------------
# AI MODEL
# ---------------------------
def train_model(current_temp):
    X = np.array([
        [20], [21], [22], [23], [24],
        [25], [26], [27], [28], [29],
        [30], [31], [32], [33], [34]
    ])

    y = np.array([
        21, 22, 23, 24, 25,
        26, 27, 28, 29, 30,
        31, 32, 33, 34, 35
    ])

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    model = MLPRegressor(
        hidden_layer_sizes=(64, 32),
        max_iter=2000,
        random_state=42
    )

    model.fit(X_scaled, y)
    prediction = model.predict(scaler.transform([[current_temp]]))

    return round(prediction[0], 1)


# ---------------------------
# UI
# ---------------------------
st.title("🌦️ ETSP Weather Prediction System")

city = st.text_input(
    "Enter City Name",
    placeholder="Chennai"
)

if st.button("Predict Weather"):

    if city == "":
        st.warning("Please Enter City Name")
        st.stop()

    location = get_location(city)

    if location is None:
        st.error("City Not Found")
        st.stop()

    city_name, lat, lon = location

    weather = get_weather(lat, lon)

    current = weather["current"]
    temp = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]
    weather_code = current["weather_code"]

    icon = get_weather_icon(weather_code)
    description = get_weather_description(weather_code)

    predicted_temp = train_model(temp)

    # ---------------------------
    # CURRENT WEATHER
    # ---------------------------
    st.markdown("---")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(
            f"<h1 style='font-size:90px'>{icon}</h1>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <h2>📍 {city_name}</h2>
            <h1>{temp}°C</h1>
            <h3>{description}</h3>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # ---------------------------
    # METRICS
    # ---------------------------
    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("💧 Humidity", f"{humidity}%")

    with m2:
        st.metric("🌬 Wind Speed", f"{wind_speed} km/h")

    with m3:
        st.metric("🤖 AI Predicted Temp", f"{predicted_temp}°C")

    st.divider()

    # ---------------------------
    # HOURLY FORECAST
    # ---------------------------
    st.subheader("⏰ Hourly Updates")

    hourly_cols = st.columns(5)

    for i in range(5):
        with hourly_cols[i]:
            time_str = weather["hourly"]["time"][i]
            hour = datetime.fromisoformat(time_str).strftime("%I %p")
            
            st.metric(
                hour,
                f"{weather['hourly']['temperature_2m'][i]}°C",
                f"💧 {weather['hourly']['precipitation_probability'][i]}%"
            )

    st.divider()

    # ---------------------------
    # 5 DAYS FORECAST
    # ---------------------------
    st.subheader("📅 5-Days Weather")

    forecast_cols = st.columns(5)

    for i in range(5):
        # INDENTATION FIX: Fixed a formatting glitch here too
        date_obj = datetime.strptime(
            weather["daily"]["time"][i],
            "%Y-%m-%d"
        )

        day = date_obj.strftime("%a")
        date = date_obj.strftime("%d %b")

        max_temp = weather["daily"]["temperature_2m_max"][i]
        min_temp = weather["daily"]["temperature_2m_min"][i]

        code = weather["daily"]["weather_code"][i]
        forecast_icon = get_weather_icon(code)

        with forecast_cols[i]:
            st.markdown(
                f"""
                <div style="padding:15px;
                            border-radius:10px;
                            text-align:center;
                            background-color:#262730;">
                    <h4>{day}</h4>
                    <div style="color:#BBBBBB; font-size:14px; margin-bottom:10px;">
                        {date}
                    </div>
                    <h1>{forecast_icon}</h1>
                    <h3>{max_temp}°C</h3>
                    <h5>{min_temp}°C</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")
    st.success(f"Current Condition: {description}")