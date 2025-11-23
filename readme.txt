Project Title:
Sentiment-Enhanced Chatbot with Real-Time Emotion Detection (HuggingFace)

Overview:
This project is an intelligent chatbot that analyzes both sentiment and emotion from every user message.
It uses HuggingFace Transformer models to classify:

Sentiment: Positive, Negative, Neutral

Emotion: Joy, Sadness, Anger, Fear, Surprise, Disgust

The bot replies based on the user's mood, saves conversation history, and provides a final sentiment trend at the end.

How to Run:

Setup Environment:
python -m venv .venv

Install all dependencies:
pip install -r requirements.txt

Run the chatbot:
python main.py

Commands:
/history → show chat history
/end → end session and save history

Features:

Real-time sentiment analysis for every message

Emotion detection using HuggingFace models

Dynamic and mood-aware bot replies

View chat history using /history

Auto-save full chat history to history.json

Final mood summary and trend detection

Project Structure:

Chatbot-Sentiment/
─ main.py 
─ sentiment.py 
─ history.json 
─ requirements.txt 
─ README.txt 

Technologies Used:

Python

HuggingFace Transformers

DistilBERT sentiment model

Emotion classification model

JSON for history storage

Tier 2 Status: 
All Tier 2 requirements are succesfully completed in running conditions.

Notes:

Uses CPU only, safe for normal laptops

No paid APIs needed

Lightweight, fast, and accurate.
By :
Abhishek Sharma
B.Tech – Artificial Intelligence and Data Science

Conclusion:
This project shows how emotion and sentiment analysis can improve conversational systems.
It is simple, effective, and useful for support systems, feedback tools, and mood-aware applications.

Architecture Diagram:


     User Input        
          |
          v
     Sentiment Model      
    (HuggingFace Pipeline) 
          |
          v
     Emotion Model       
     (distilbert-base-emo)  
          |
          v
     Response Generator 
     (Rule-based Logic)     
          |
          v
     History Logger       
     (history.json)       

FlowChart: 

     Start Chatbot    
          |
          v
      Get user message

          |
          v
     Run Sentiment Analysis     
          |
          v
     Run Emotion Detection
          |
          v
     Generate Bot Response       
          |
          v
     Save to history.json
          |
          v
     Continue or Exit?  
           |
     Yes / No

