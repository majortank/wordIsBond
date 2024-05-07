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
# Why WordIsBond?
"Word is Bond" for several reasons:

1. **Trustworthiness**: The phrase "word is bond" conveys a sense of trustworthiness and reliability. By using this name, the chatbot suggests that it will uphold its promises and commitments, fostering trust between the user and the AI.

2. **Confidence in Accuracy**: The term "word" implies a commitment to truth and accuracy. Users may feel confident that the chatbot will provide accurate and reliable responses to their queries or discussions about sentiments.

3. **Connection to Communication**: "Word is bond" has roots in colloquial language, particularly within certain cultural contexts. This connection to everyday language can make the chatbot feel more approachable and relatable to users.

4. **Emotional Connection**: Sentiment-based interactions often involve emotional elements. The phrase "word is bond" carries emotional weight, suggesting a bond or connection between the user and the chatbot, which can enhance the emotional resonance of the interaction.

5. **Memorability**: The name "Word is Bond" is memorable and catchy, making it easy for users to recall when seeking out a sentiment-based chatbot for future interactions.

## Usage

To run the application, use the following command in the terminal:

```bash
streamlit run app.py
