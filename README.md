# WordIsBond ChatBot

This is a simple chatbot application built with Python, Streamlit, and TextBlob. The chatbot uses sentiment analysis to generate responses based on the sentiment of the user's input.

## Libraries Used

- `streamlit`: A fast, easy way to create web apps for machine learning and data science.
- `textblob`: A library for processing textual data, providing a simple API for diving into common natural language processing (NLP) tasks.

## Class: ChatBot

The `ChatBot` class is the main class in this application. It has two methods:

### `__init__(self)`

This is the constructor method that initializes the `TextBlob` object for sentiment analysis.

### `get_response(self, user_message)`

This method takes in a user message as input, analyzes its sentiment, and generates a response based on the sentiment score. The sentiment score ranges from -1 (negative) to 1 (positive). 

- If the sentiment score is positive, the chatbot responds positively.
- If the sentiment score is negative, the chatbot offers to transfer the user to an agent.
- If the sentiment score is neutral, the chatbot asks for more information.

## Streamlit UI

The Streamlit UI is simple and intuitive. It consists of a title, a text input field for the user's message, and a text area to display the chatbot's response.
![image](https://github.com/majortank/wordIsBond/assets/41399491/045d655b-613e-4616-b1cb-f57218e661fb)


## Usage

To run the application, use the following command in the terminal:

```bash
streamlit run app.py
