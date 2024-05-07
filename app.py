# Importing required libraries
import streamlit as st
from textblob import TextBlob

# Defining the ChatBot class for interaction.
class ChatBot:
    def __init__(self):
        # Initializing the sentiment analysis tool.
        self.sentiment_analyzer = TextBlob("")

    def get_response(self, user_message):
        # Analyzing the sentiment of the user's message
        self.sentiment_analyzer = TextBlob(user_message)
        sentiment_score = self.sentiment_analyzer.sentiment.polarity

        # Generating the chatbot's response based on sentiment.
        if sentiment_score > 0:
            chatbot_message = f"That's great to hear! Sentiment Score: {sentiment_score}"
        elif sentiment_score < 0:
            chatbot_message = f"I am sorry to hear that. Would you like me to transfer you to an agent? Sentiment Score: {sentiment_score}"
        else:
            chatbot_message = f"Hmm, I see. Can you please provide more information? Sentiment Score: {sentiment_score}"

        return chatbot_message

# Creating the chatbot
chatbot = ChatBot()

# Streamlit UI
st.title('ChatBot')
user_message = st.text_input("You: ")

if user_message:
    response = chatbot.get_response(user_message)
    st.text_area("ChatBot:", value=response, height=200, max_chars=None, key=None)