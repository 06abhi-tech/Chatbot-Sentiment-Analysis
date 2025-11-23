import sys
import json
from sentiment import analyze, aggregate, detect_trend

history = []

def add(speaker, text, meta=None):
    entry = {"speaker": speaker, "text": text}
    if meta:
        entry.update(meta)
    history.append(entry)

def show_history():
    for i, m in enumerate(history, 1):
        if "sentiment_label" in m:
            print(
                f"{i}. {m['speaker']}: {m['text']} -> "
                f"{m['sentiment_label']} ({m['sentiment_score']:+.3f}), "
                f"Emotion: {m['emotion']} ({m['emotion_score']:+.3f})"
            )
        else:
            print(f"{i}. {m['speaker']}: {m['text']}")

# --------------------------------------
# SAVE HISTORY IN JSON
# --------------------------------------
def save_history_json():
    formatted = []

    for h in history:
        formatted.append({
            "speaker": h.get("speaker", ""),
            "text": h.get("text", ""),
            "sentiment": h.get("sentiment_label", ""),
            "sentiment_score": h.get("sentiment_score", ""),
            "emotion": h.get("emotion", ""),
            "emotion_score": h.get("emotion_score", "")
        })

    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=4, ensure_ascii=False)

    print("History saved → history.json")

# --------------------------------------

def bot_reply(user_text, analysis):
    senti = analysis["sentiment_score"]
    emotion = analysis["emotion"].lower()

    # Emotion-based replies
    if emotion == "sadness":
        return "I'm here for you. Want to talk about what's making you feel sad?"

    if emotion == "anger":
        return "I understand you're feeling angry. Want to tell me what caused it?"

    if emotion == "fear":
        return "It sounds scary. I'm here with you. What made you feel this way?"

    if emotion == "joy":
        return "That's wonderful! Tell me more about what's making you happy!"

    if emotion == "disgust":
        return "That sounds unpleasant. What happened exactly?"

    if emotion == "surprise":
        return "Wow, that sounds surprising! What made that happen?"

    # Sentiment fallback
    if senti <= -0.6:
        return "I hear your frustration. Can you tell me what specifically bothered you?"

    if senti <= -0.3:
        return "I understand you're feeling upset. What caused this feeling?"

    if senti >= 0.6:
        return "Great! That’s good to hear. Want to share more?"

    # Keyword replies
    t = user_text.lower()
    if any(x in t for x in ["hi", "hello", "hey"]):
        return "Hello! How are you feeling today?"

    if any(x in t for x in ["thank", "thanks"]):
        return "You're welcome! Anything else you'd like to ask?"

    if any(x in t for x in ["problem", "issue", "error"]):
        return "Let’s sort this out. Can you explain the issue a bit more?"

    return "I understand. Tell me more or type /end when you're done."

def run():
    print()
    print("Sentiment Chatbot (HuggingFace)")
    print("Type /end to finish, /history to view conversation")
    print()

    while True:
        try:
            user = input("You: ").strip()
        except:
            user = "/end"

        if not user:
            continue

        # End session
        if user.lower() == "/end":
            print()
            msgs = [m for m in history if m["speaker"] == "User"]
            agg = aggregate(msgs)

            print(f"Final overall sentiment: {agg['label']} (compound={agg['compound']:+.3f})")
            print(detect_trend(msgs))

            # SAVE JSON HERE
            save_history_json()

            print()
            break

        # Show history
        if user.lower() == "/history":
            show_history()
            continue

        # Analyse the message
        analysis = analyze(user)
        add("User", user, analysis)

        print(f"Sentiment: {analysis['sentiment_label']} ({analysis['sentiment_score']:+.3f})")
        print(f"Emotion: {analysis['emotion']} ({analysis['emotion_score']:+.3f})")

        # Bot reply
        resp = bot_reply(user, analysis)
        add("Bot", resp, {
            "sentiment_label": analysis["sentiment_label"],
            "sentiment_score": analysis["sentiment_score"],
            "emotion": analysis["emotion"],
            "emotion_score": analysis["emotion_score"]
        })
        print("Bot:", resp)

if __name__ == "__main__":
    run()
