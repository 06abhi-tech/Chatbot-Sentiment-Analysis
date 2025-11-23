from transformers import pipeline

sentiment_model = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

emotion_model = pipeline(
    task="text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def analyze(text: str) -> dict:
    if not text or not text.strip():
        return {
            "sentiment_label": "NEUTRAL",
            "sentiment_score": 0.0,
            "emotion": "neutral",
            "emotion_score": 0.0
        }

    s = sentiment_model(text)[0]
    label = s["label"]
    score = s["score"]
    sentiment_score = score if label == "POSITIVE" else -score

    emotions = emotion_model(text)[0]
    top_emotion = max(emotions, key=lambda x: x["score"])

    return {
        "sentiment_label": "POSITIVE" if sentiment_score >= 0 else "NEGATIVE",
        "sentiment_score": round(sentiment_score, 3),
        "emotion": top_emotion["label"],
        "emotion_score": round(top_emotion["score"], 3)
    }


def aggregate(messages: list) -> dict:
    if not messages:
        return {"label": "NEUTRAL", "compound": 0.0}

    scores = [msg["sentiment_score"] for msg in messages]
    avg_score = sum(scores) / len(scores)

    return {
        "label": "POSITIVE" if avg_score >= 0 else "NEGATIVE",
        "compound": round(avg_score, 3)
    }


def detect_trend(messages: list) -> str:
    if len(messages) < 2:
        return "Not enough messages to determine trend."

    first = messages[0]["sentiment_score"]
    last = messages[-1]["sentiment_score"]

    if last > first:
        return "Emotion trend: Improving 🙂"
    elif last < first:
        return "Emotion trend: Getting worse ☹️"
    else:
        return "Emotion trend: Stable 😐"
