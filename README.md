# 🧠 Mental Wellness – AI-Powered Emotion Detection System

## 📌 Overview

Mental Wellness is an AI-powered web application designed to understand users' emotional states through text-based emotion detection. It uses Machine Learning and Natural Language Processing (NLP) techniques to identify emotions and provide personalized wellness suggestions.

The application helps users reflect on their emotions, track their emotional history, and access useful mental wellness resources through a simple and interactive dashboard.

## ✨ Features

- **Emotion Detection:** Identifies six emotions – Joy, Sadness, Anger, Fear, Love, and Surprise.
- **AI-Based Prediction:** Uses TF-IDF and Machine Learning techniques to analyze text and predict emotions.
- **Confidence Score:** Displays the model's confidence level for each prediction.
- **Wellness Recommendations:** Provides suggestions based on the detected emotion.
- **Emotion History:** Allows users to view their previous emotion analysis results.
- **Dashboard:** Displays emotional insights and visualizations.
- **User Authentication:** Provides a login and registration interface.
- **Admin Dashboard:** Includes an interface for administrative management.
- **Responsive Design:** Supports different screen sizes.
- **Light and Dark Mode:** Offers a comfortable viewing experience.

## 🛠️ Technologies Used

### Frontend
- React.js
- Vite
- JavaScript
- CSS
- Recharts
- Axios
- Framer Motion
- Lucide React

### Backend
- Python
- FastAPI
- REST API

### Machine Learning & NLP
- Scikit-learn
- TF-IDF Vectorization
- Label Encoding
- Emotion Classification

### Database
- SQLite

## ⚙️ How It Works

1. The user enters a text describing their thoughts or feelings.
2. The application sends the text to the backend through a REST API.
3. The Machine Learning model processes the text using TF-IDF vectorization.
4. The model predicts the most likely emotion.
5. The application displays the predicted emotion and confidence score.
6. Based on the result, the system provides relevant wellness recommendations.
7. Users can view their previous results through the dashboard.

## 🏗️ System Architecture

**User → React Frontend → FastAPI Backend → ML Model → Emotion Prediction → Wellness Recommendations**

## 🚀 Getting Started

### Prerequisites

Make sure you have installed:

- Python
- Node.js
- npm
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Mental-Wellness
```

### 3. Start the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed in your terminal.

## 🎯 Project Objective

The main objective of this project is to combine Artificial Intelligence, Machine Learning, and Natural Language Processing to build an interactive mental wellness application that helps users understand and reflect on their emotions.

## 🔮 Future Enhancements

- Improve emotion prediction accuracy using larger datasets.
- Add multilingual emotion detection.
- Introduce personalized wellness tracking.
- Add emotion trend analysis and reports.
- Integrate more advanced NLP models.

## ⚠️ Disclaimer

This application is intended for emotional awareness and general wellness support only. It is not a substitute for professional mental health advice, diagnosis, or treatment.

## 👩‍💻 Developed By

**Abhinandana UK**

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/abhi29-tech
