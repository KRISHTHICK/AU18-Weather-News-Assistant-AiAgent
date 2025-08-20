# AU18-Weather & News Assistant AI Agent
AI Agent
🆕 Agent Topic: Weather & News Assistant
🔹 What it does

Takes a city name as input.

Fetches the current weather (using OpenWeather API).

Fetches the latest news headlines (using NewsAPI).

Combines both into a personalized AI response (via Ollama or OpenAI LLM).

Runs with Python + Streamlit in VS Code.

🔹 How it works (Explanation)

APIs used

OpenWeather → Fetches real-time weather for the given city.

NewsAPI → Gets top 5 headlines.

Agent Logic

Reads user input (city).

Calls Weather Tool → Fetches temperature + condition.

Calls News Tool → Fetches top 5 headlines.

Combines both into a human-like response.

UI (Streamlit)

Input box for city name.

Button → fetches results.

Displays final agent response in a nice readable format.

⚡ Run in VS Code:

pip install streamlit requests
streamlit run app.py
