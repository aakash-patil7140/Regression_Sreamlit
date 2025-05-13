# Linear Regression Web App using Streamlit

This project demonstrates how to build a **Linear Regression Web Application** using **Streamlit**, **Scikit-Learn**, and **Python**. The web app allows users to upload their dataset, train a linear regression model, and make predictions interactively.

## 📂 Repository Structure

```
Regression_Streamlit/
├── LinearRegression.ipynb   # Jupyter Notebook demonstrating Linear Regression with Streamlit
└── (other Streamlit app files, if any)
```

## 🚀 Features

* Upload your custom CSV dataset.
* Visualize the dataset.
* Select features and target variable.
* Train a Linear Regression model.
* Display model accuracy and coefficients.
* Predict outcomes using custom inputs.

## 🛠 Technologies Used

* Python 3
* Streamlit
* Pandas
* Scikit-learn
* Seaborn

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/aakash-patil7140/Regression_Streamlit.git
cd Regression_Streamlit
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install manually:

```bash
pip install streamlit pandas scikit-learn seaborn
```

## 💡 How to Run

1. Navigate to the project folder.
2. Run the Streamlit app using:

```bash
streamlit run LinearRegression.ipynb
```

> **Note:** Streamlit natively supports `.py` files. To run a `.ipynb` file, you might need to convert it to `.py` using Jupyter or use tools like `jupyter nbconvert`.

Alternatively, extract the code from the notebook and place it inside a `.py` file.

## 📊 Example Use Case

* Upload a dataset containing independent and dependent variables.
* Select your columns and train a model.
* Get model insights and predict for new data points.

## 📎 References

* [Streamlit Documentation](https://docs.streamlit.io/)
* [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

#Streamlit Url :- https://aakash-patil7140-regression-sreamlit-app-eeicgf.streamlit.app/
