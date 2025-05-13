# 🎓💼 Salary Prediction Web Application

A simple and interactive web app that predicts a **job package (salary)** based on a student's **CGPA**, powered by **Linear Regression** and deployed using **Streamlit**.

## 📌 Overview

This project contains the following key components:

| File                          | Description                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `📄 app.py`                   | Main script for the Streamlit web interface. Takes CGPA as input and shows predicted salary.                             |
| `📘 LinearRegression.ipynb`   | Jupyter Notebook for training the model using `placements.csv`. Includes data analysis, visualization, and model saving. |
| `📦 Linear_Regression.joblib` | Saved Linear Regression model generated after training.                                                                  |
| `📄 requirements.txt`         | Python dependencies for running the project.                                                                             |
| `📊 placements.csv`           | Dataset containing student CGPAs and corresponding job packages.                                                         |

## 📂 Dataset

The dataset used: **`placements.csv`**

| Column       | Description                                   |
| ------------ | --------------------------------------------- |
| `🎓 cgpa`    | Cumulative Grade Point Average of the student |
| `💰 package` | Job package (salary) offered to the student   |

## ⚙️ Setup & Installation

### 🔁 Clone the repository

```bash
git clone <repository_url>
cd Salary_Prediction
```

### 📦 Install dependencies

Using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib
```

---

## 🚀 Running the Application

1. Open terminal and navigate to the project directory.
2. Launch the app using:

   ```bash
   streamlit run app.py
   ```
3. Your browser will open the app.
   🔢 Enter a CGPA (between **3.0 and 10.0**) and click **"Predict Package"** to get your predicted salary 💸.

---

## 🧠 Training the Model

To retrain or view model development:

1. Make sure Jupyter is installed:

   ```bash
   pip install notebook
   ```
2. Open the notebook:

   ```bash
   jupyter notebook LinearRegression.ipynb
   ```
3. Execute all cells to:

   * Load and visualize data 📊
   * Train the model 🧪
   * Save the trained model as `Linear_Regression.joblib` 💾


## 🛠 Libraries & Tools Used

| Library                   | Purpose                       |
| ------------------------- | ----------------------------- |
| `🔵 Streamlit`            | Build the web interface       |
| `📊 Pandas`               | Data handling & preprocessing |
| `📐 NumPy`                | Numerical operations          |
| `📈 Scikit-learn`         | ML model & evaluation         |
| `🖼 Matplotlib & Seaborn` | Data visualization            |
| `💾 Joblib`               | Model serialization           |

**#StreamLit URL** :- https://rio1002-salary-prediction-app-9zhuoi.streamlit.app/
