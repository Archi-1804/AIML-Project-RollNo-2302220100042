<div align="center">

# 🏥 Medical Insurance Cost Prediction

## 🌐 Live Demo

🔗 **Live App:** [https://your-app-name.streamlit.app](https://aiml-project-rollno-2302220100042.onrender.com)

### 📊 Predicting Medical Insurance Charges using Linear Regression

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)

---

*A complete Machine Learning project that predicts annual medical insurance charges based on demographic and health-related features.*

</div>

---

# 📌 Project Overview

Medical insurance companies estimate customer medical expenses before determining insurance premiums.

This project develops a **Linear Regression** model that predicts medical insurance charges using:

- 👤 Age
- ⚧ Gender
- ⚖️ BMI
- 👨‍👩‍👧 Number of Children
- 🚬 Smoking Status
- 🌍 Region

To make the model interactive and user-friendly, a Streamlit web application was developed, allowing users to enter their details and receive real-time insurance cost predictions.

The project follows the complete Machine Learning workflow from **data preprocessing** to **model evaluation**.

---

# 🎯 Problem Statement

An insurance company wants to estimate a customer's annual medical insurance charges based on personal attributes such as age, BMI, smoking status, number of children, sex, and region.

The objective is to build a regression model that accurately predicts insurance charges.

---

# 💼 Business Objective

This project helps insurance companies:

- 💰 Estimate insurance premiums
- 📈 Improve pricing strategies
- 🔍 Identify major cost-driving factors
- 📊 Support data-driven business decisions

---

# 📂 Dataset

| Property | Details |
|----------|---------|
| 📄 Dataset | Medical Cost Personal Dataset |
| 🌐 Source | Kaggle |
| 📊 Records | 1338 |
| 🎯 Target Variable | Charges |

### Dataset Features

| Feature | Description |
|----------|-------------|
| Age | Age of the customer |
| Sex | Gender |
| BMI | Body Mass Index |
| Children | Number of dependent children |
| Smoker | Smoking status |
| Region | Residential region |
| Charges | Medical Insurance Cost |

---

# 🛠️ Tech Stack

- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 📈 Matplotlib
- 🎨 Seaborn
- 🤖 Scikit-Learn
- 📓 Jupyter Notebook
- 💻 VS Code
- 🌐 Streamlit
- 💾 Joblib

---

# 📁 Project Structure

```text
Medical-Insurance-Cost-Prediction/
│
├── 📁 Dataset/
│   └── insurance.csv
│
├── 📁 Notebook/
│   └── medical_prediction.ipynb
│
├── 📁 model/
│   ├── insurance_model.pkl
│   └── columns.pkl
│
├── 📁 Images/
│   ├── app_home.png
│   ├── prediction_result.png
│   ├── smoker_vs_charges.png
│   ├── bmi_vs_charges.png
│   └── correlation_heatmap.png
│
├── 📄 app.py
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```

---

# ⚙️ Machine Learning Workflow

```text
📥 Dataset Collection
          │
          ▼
🧹 Data Cleaning & Preprocessing
          │
          ▼
📊 Exploratory Data Analysis (EDA)
          │
          ▼
⚙️ Feature Engineering
          │
          ▼
✂️ Train-Test Split
          │
          ▼
🤖 Linear Regression Model Training
          │
          ▼
📈 Model Evaluation
          │
          ▼
💡 Feature Impact Analysis
          │
          ▼
💾 Model Serialization (Joblib)
          │
          ▼
🌐 Streamlit Web Application
          │
          ▼
🚀 Deployment
```

---

# 🧹 Data Cleaning

✔ Checked missing values

✔ Removed duplicate records

✔ Verified positive values for Age, BMI and Charges

✔ Standardized categorical text

✔ Verified data types

---

# 📊 Exploratory Data Analysis (EDA)

The following visualizations were created.

## 🚬 Smoker vs Insurance Charges

<p align="center">
<img src="Images\Smoker vs Charges.png" width="650">
</p>

---

## ⚖️ BMI vs Insurance Charges

<p align="center">
<img src="Images\BMI vs Charges.png" width="650">
</p>

---

## 🔥 Correlation Heatmap

<p align="center">
<img src="Images\Heatmap.png" width="700">
</p>

---

## 👤 Age vs Insurance Charges

<p align="center">
<img src="Images\Children vs Charges.png" width="650">
</p>

---

## 🎯 Predicted vs Actual Charges

<p align="center">
<img src="Images\Actual vs Predicted plot.png" width="650">
</p>

---

# ⚙️ Feature Engineering

The following feature engineering techniques were applied:

✅ One-Hot Encoding

- Sex
- Smoker
- Region

✅ BMI Category Feature

- Underweight
- Normal
- Overweight
- Obese

✅ Smoker × BMI Interaction Feature

This interaction feature helps the model capture the stronger effect of high BMI among smokers.

---

# 🤖 Model Building

The model was built using **Linear Regression**.

### Steps

- Feature Selection
- Target Selection
- Train-Test Split (80:20)
- Model Training
- Prediction
- Evaluation

---

# 📈 Model Performance

| Metric | Score |
|---------|------:|
| R² Score | 0.8868141245573691 |
| MAE | 2813.0707550847505 |
| RMSE | 4560.547223347653 |

---

# 📌 Feature Impact Analysis

After analyzing the Linear Regression coefficients:

## 🚬 Smoking Status

Smoking emerged as the **strongest predictor** of insurance charges.

Customers who smoke generally have significantly higher predicted insurance costs.

---

## ⚖️ BMI

Higher BMI generally results in higher predicted medical insurance charges.

---

## 🚬 + ⚖️ Smoking × BMI

The interaction feature demonstrates that smokers with higher BMI tend to have the highest predicted insurance expenses.

---

## 👤 Age

Insurance charges generally increase with age.

---

## 👨‍👩‍👧 Children

The number of dependent children has a relatively small effect on insurance costs.

---

## 🌍 Region

Regional differences contribute only a minor effect compared with smoking and BMI.

---

# 📊 Key Findings

- 🚬 Smoking is the strongest predictor of insurance charges.
- ⚖️ Higher BMI is associated with higher medical costs.
- 👤 Older customers generally incur higher insurance expenses.
- 🚬 + ⚖️ Smoking combined with high BMI significantly increases predicted charges.
- 📈 Linear Regression provides a strong baseline model for this dataset.

---

# 🚀 Future Improvements

- 🌲 Random Forest Regressor
- ⚡ XGBoost Regressor
- 🌳 Gradient Boosting
- 🎯 Hyperparameter Tuning
- 🔄 Cross Validation
- 📉 Log Transformation of Charges
- 🤖 Model Deployment using Streamlit

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Archi-1804/AIML-Project-RollNo-2302220100042.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

# 📚 Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting medical insurance charges.

After data cleaning, visualization, feature engineering and model evaluation, **Smoking Status** was identified as the most influential feature affecting insurance costs, followed by **BMI** and **Age**.

The project serves as an excellent beginner-to-intermediate regression project while providing valuable insights into healthcare insurance pricing.

---

# 👨‍💻 Author

<div align="center">

## Archi Shivhare

🎓 B.Tech Computer Science Engineering

💡 Machine Learning • Data Analytics • Python

⭐ If you like this project, consider giving it a **Star** on GitHub!

</div>
