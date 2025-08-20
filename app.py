import streamlit as st
import requests
import os

# -----------------------------
# Setup API keys
# -----------------------------
WEATHER_API_KEY = "your_openweather_api_key"
NEWS_API_KEY = "your_newsapi_key"

# -----------------------------
# Weather Tool
# -----------------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"🌡️ {data['main']['temp']}°C, {data['weather'][0]['description']}"
    else:
        return "⚠️ Could not fetch weather."

# -----------------------------
# News Tool
# -----------------------------
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        headlines = [a["title"] for a in articles[:5]]
        return headlines
    else:
        return ["⚠️ Could not fetch news."]

# -----------------------------
# Simple AI Response (Mock LLM)
# -----------------------------
def generate_response(city, weather, news_list):
    news_summary = "\n".join([f"- {n}" for n in news_list])
    return f"""
Hello! 👋  
Here is your update for **{city}**:  

🌤️ **Weather**: {weather}  

📰 **Top News Headlines**:  
{news_summary}  

✅ Stay informed & have a great day!
"""

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Weather & News Assistant", page_icon="🤖", layout="centered")

st.title("🤖 Weather & News Assistant")
city = st.text_input("Enter your city:", "Delhi")

if st.button("Get Update"):
    weather = get_weather(city)
    news = get_news()
    response = generate_response(city, weather, news)
    st.success(response)
