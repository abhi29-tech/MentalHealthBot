import os
import re
import string
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------------------------------------
# Download required NLTK resources
# ---------------------------------------
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# ---------------------------------------
# Load Stopwords & Lemmatizer
# ---------------------------------------
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ---------------------------------------
# Model Paths
# ---------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "mental_health_emotion_model.pkl")
TFIDF_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

# ---------------------------------------
# Load Trained Model
# ---------------------------------------
try:
    model = joblib.load(MODEL_PATH)
    tfidf = joblib.load(TFIDF_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
    print("✅ ML model loaded successfully.")
except Exception as e:
    print("⚠️ Model loading failed:", e)
    model = None
    tfidf = None
    label_encoder = None

# ---------------------------------------
# Text Cleaning Function
# ---------------------------------------
def clean_text(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenize
    words = text.split()

    # Remove stopwords and perform lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# ---------------------------------------
# Emotion Prediction
# ---------------------------------------
def predict_emotion(user_text):
    # If model couldn't load, return a default emotion
    if model is None or tfidf is None or label_encoder is None:
        return "neutral"

    cleaned_text = clean_text(user_text)

    vector = tfidf.transform([cleaned_text])

    prediction = model.predict(vector)

    emotion = label_encoder.inverse_transform(prediction)[0]

    return emotion