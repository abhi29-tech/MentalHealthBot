recommendations = {

    "joy": {
        "title": "Maintain Your Happiness 😊",
        "message": (
            "It's wonderful that you're feeling joyful. Continue engaging in activities "
            "that make you happy, spend time with loved ones, practice gratitude, "
            "and maintain a healthy routine to sustain your positive emotions."
        )
    },

    "sadness": {
        "title": "Overcoming Sadness 💙",
        "message": (
            "Feeling sad is completely normal. Try talking to someone you trust, "
            "take a short walk, listen to calming music, write down your thoughts, "
            "and remember that emotions are temporary. If sadness persists, "
            "consider reaching out to a mental health professional."
        )
    },

    "anger": {
        "title": "Managing Anger 😠",
        "message": (
            "Take a few deep breaths before reacting. Practice mindfulness, "
            "count to ten, or step away from the situation temporarily. "
            "Physical exercise and relaxation techniques can also help reduce anger."
        )
    },

    "fear": {
        "title": "Managing Fear 😨",
        "message": (
            "Try grounding exercises such as focusing on your surroundings, "
            "practice slow deep breathing, and remind yourself that fear often "
            "passes with time. Sharing your feelings with someone you trust can help."
        )
    },

    "love": {
        "title": "Celebrate Positive Connections ❤️",
        "message": (
            "It's great to experience feelings of love and connection. "
            "Express your appreciation to those around you, nurture healthy "
            "relationships, and continue building meaningful bonds."
        )
    },

    "surprise": {
        "title": "Processing Unexpected Situations 😲",
        "message": (
            "Unexpected events can bring excitement or uncertainty. "
            "Take a moment to understand what happened before reacting. "
            "Stay calm and approach the situation with an open mind."
        )
    }

}


def get_recommendation(emotion):

    emotion = emotion.lower()

    return recommendations.get(
        emotion,
        {
            "title": "Mental Wellness 🌿",
            "message": (
                "Take care of yourself, maintain a healthy routine, "
                "and don't hesitate to seek professional support if you "
                "feel emotionally overwhelmed."
            )
        }
    )