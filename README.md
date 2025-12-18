# 📉 Customer Churn Prediction: End-to-End ML Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red)
![Cloud](https://img.shields.io/badge/Cloud-Render-purple)

A full-stack Machine Learning application that predicts whether a customer is likely to churn (cancel service). The project includes a trained Random Forest model, a production-ready Flask API, and an interactive frontend dashboard.

## 🔗 Live Demo
* **Interactive Dashboard:** https://churn-prediction-api-uy2vdq9zlyrhvhou79v9bj.streamlit.app/
* **Prediction API:** https://churn-api-portfolio.onrender.com

## 🚀 Project Overview
**The Problem:** Customer churn is a critical metric for subscription businesses. Identifying at-risk customers early allows companies to intervene and improve retention.

**The Solution:**
1.  **Data Engineering:** Preprocessed the Telco Customer Churn dataset (cleaning, one-hot encoding, scaling).
2.  **Model Training:** Trained a **Random Forest Classifier** (Accuracy: ~79%).
3.  **Backend API:** Built a RESTful API using **Flask** to serve predictions in real-time.
4.  **Frontend UI:** Developed a user-friendly dashboard using **Streamlit**.
5.  **Deployment:** Deployed the API to **Render** and the Dashboard to **Streamlit Cloud**.

## 🛠️ Technical Architecture
The system handles the "Schema Skew" problem by aligning user input with the exact feature columns used during training, ensuring reliable predictions even with missing data.

* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Web Framework:** Flask (Backend), Streamlit (Frontend)
* **Deployment:** Docker/Render (API), Streamlit Cloud (UI)

## 📂 Repository Structure
```text
├── data/                  # Raw dataset
├── models/                # Saved models (.pkl) and column maps
├── notebooks/             # Jupyter Notebooks for EDA & Training
├── src/
│   └── app.py             # Flask API source code
├── dashboard.py           # Streamlit Dashboard source code
├── Procfile               # Deployment configuration for Render
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
