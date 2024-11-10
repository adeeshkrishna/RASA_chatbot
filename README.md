# Movie Recommendation Chatbot 🎬

A conversational AI chatbot that recommends movies based on user preferences. This project uses Rasa for natural language understanding and dialogue management, TMDb API for fetching movie data, and Flask to create a simple, interactive web interface.

## Features

* 🎥 **Movie Recommendations**: Get personalized movie suggestions.
* 🎭 **Genre Selection**: Choose movie genres based on preferences.
* 🌐 **User-Friendly Interface**: Dark-themed chat interface with interactive design.
* 💬 **Real-Time Interaction**: Seamless conversation experience powered by Rasa.

## Tech Stack

* **Rasa**: For natural language understanding and managing dialogue.
* **TMDb API**: To fetch movie data and provide recommendations.
* **Flask**: Backend framework to handle web requests and connect with Rasa.
* **HTML/CSS**: Frontend interface design.
* **JavaScript**: For dynamic message handling and interactions.

## Installation & Setup

1. **Clone the Repository**:
```bash
git clone https://github.com/adeeshkrishna/RASA_chatbot.git
cd RASA_chatbot
```

2. **Install Dependencies**:
   * Install Python dependencies:
```bash
pip install -r requirements.txt
```
   * Make sure you have Rasa installed.

3. **Set up TMDb API Key**:
   * Sign up at TMDb to get an API key
   * Add the key to your environment variables or directly in the code

4. **Run Rasa Server**:
```bash
rasa run --enable-api --cors "*" --port 5005
```

5. **Run Rasa Action Server**:
```bash
rasa run actions
```

6. **Run Flask App**:
```bash
python app.py
```

6. **Access the Chatbot**:
   * Open `http://localhost:5001` in your browser

## Usage

1. Type in the chat input to start a conversation with the bot
2. Ask for movie recommendations, specify genres, and explore different suggestions

## Project Structure

* `app.py`: Main Flask application connecting the frontend to Rasa
* `templates/index.html`: HTML for chatbot interface
* `static/styles.css`: Styling for a dark-themed user interface
* `actions.py`: Custom actions to integrate TMDb API with Rasa

## Examples of Queries

* "Recommend me a movie"
* "Suggest a thriller movie"
* "I want to watch a comedy"

## Troubleshooting

* **No response from Rasa**: Ensure the Rasa server is running and accessible at the correct URL
* **Flask errors**: Verify Flask dependencies are installed and configured correctly

## Future Enhancements

* Add more conversational flows, such as actor-based or release-year-based recommendations
* Use sentiment analysis to further personalize movie suggestions
* Integrate additional movie details like ratings or trailers