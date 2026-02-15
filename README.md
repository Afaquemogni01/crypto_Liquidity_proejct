# 🚀 Crypto Liquidity Prediction System

## 📌 Overview
This Machine Learning project predicts whether a Cryptocurrency has **High Liquidity** (Safe to trade) or **Low Liquidity** (Risky) based on market data like Price, Volume, and Market Cap. It uses a **Random Forest Classifier** and serves predictions via a **Flask Web Interface**.

## 🎥 Demo
Here is the Flask Web Interface predicting Liquidity:

![Dashboard Output](./Screenshots/dashbord.png)

here is the Architecture of the project :

![Dashboard Output](./Screenshots/arch.png)


## 📊 Key Insights from EDA
During analysis, we found that **Trading Volume** has the highest correlation with Liquidity.

### 1. Correlation Heatmap
![Heatmap](./Screenshots/heat.png)

### 2. Disrtibution of liquity_ratio
![Trend Graph](./Screenshots/Liquidity.png)

### 3 confusion matrix 
![confusion_matrix](./Screenshots/confidence.png)


### 4 Market cap VS vol of market
![scatterplot](./Screenshots/scatter.png)

### 5 Distribution of Liquidity_ratio
![distributionPlot](./Screenshots/Liquidity.png)

## 🛠 Tech Stack
- **Frontend:** HTML, CSS (Glassmorphism UI), JavaScript
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn (Random Forest), Pandas, NumPy
- **Deployment:** Netlify / Gunicorn

## 📂 Project Structure