# Email Spam Predictor

## 📌 Project Overview

Email Spam Predictor is a Machine Learning project that classifies emails as **Spam** or **Not Spam**.

The project uses Natural Language Processing (NLP) techniques to analyze email text and identify patterns commonly associated with spam messages.

## 🎯 Objective

The main objective of this project is to:

* Detect spam emails automatically
* Classify emails as Spam or Not Spam
* Reduce unwanted and potentially harmful emails
* Demonstrate the use of NLP and Machine Learning for text classification

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorization
* Streamlit

## 📊 Dataset

The dataset contains email messages along with their corresponding labels.

The main information includes:

* Email Text
* Spam / Not Spam Label

## 🤖 Machine Learning Model

The project uses a Machine Learning classification model to predict whether an email is **Spam** or **Not Spam**.

The email text is converted into numerical features using **TF-IDF Vectorization** before being passed to the machine learning model.

The model predicts two classes:

* **Spam**
* **Not Spam**

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Text Preprocessing
5. TF-IDF Feature Extraction
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

## 📈 Model Evaluation

The model was evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

## 🌐 Streamlit Application

The trained model is deployed using Streamlit.

Users can enter an email message through the web interface and receive a prediction:

**🚫 Email is classified as SPAM**

or

**✅ Email is classified as NOT SPAM**

## 📁 Project Structure

text
email-spam-predictor/
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md

