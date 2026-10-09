# Penguin Species Classifier

An end-to-end machine learning project that predicts a penguin's **species** from island, culmen measurements, flipper length, body mass, and sex.

The project covers data exploration, missing value handling, feature preprocessing, model comparison, hyperparameter tuning, test set evaluation, and prediction through a Streamlit app.

---

## Table of Contents

* [Overview](#overview)
* [Problem Statement](#problem-statement)
* [Dataset](#dataset)
* [Tools & Technologies](#tools--technologies)
* [Project Structure](#project-structure)
* [Data Preparation](#data-preparation)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Model Training & Evaluation](#model-training--evaluation)
* [Prediction App](#prediction-app)
* [How to Run](#how-to-run)
* [Future Improvements](#future-improvements)

---

## Overview

Penguin species can be distinguished using physical measurements and information about where the penguin was observed. This project trains classification models on those features and provides a simple form for entering measurements and requesting a species prediction.

### Project Workflow

```text
Penguin Dataset
       ↓
Data Inspection and Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Preprocessing Pipelines
       ↓
Baseline and Model Comparison
       ↓
Stratified Cross-Validation
       ↓
Hyperparameter Tuning
       ↓
Test Set Evaluation
       ↓
Streamlit Species Prediction
```

---

## Problem Statement

The goal is to predict the species label for a penguin from its available physical measurements and categorical attributes. This is a multi-class classification task.

A trained classifier can provide a quick species estimate from the values entered in the app. The notebook also evaluates how well different models perform on held-out data.

---

## Dataset

The project uses `Data/Penguin Species Prediction Dataset.csv`. It contains the target column `species` and these input features:

* `island`
* `culmen_length_mm`
* `culmen_depth_mm`
* `flipper_length_mm`
* `body_mass_g`
* `sex`

The notebook reads the CSV from the `Data` folder. The Streamlit app uses the same dataset to populate the island and sex choices and set input ranges.

---

## Tools & Technologies

* **Python**
* **Pandas** and **NumPy** for data handling
* **Scikit-learn** for preprocessing, model training, and evaluation
* **Matplotlib** and **Seaborn** for exploration and visualizations
* **Jupyter Notebook** for analysis
* **Streamlit** for the prediction interface
* **Joblib** for loading and saving model artifacts

### Models Compared

The notebook compares the following classifiers:

* Logistic Regression
* Decision Tree
* K-Nearest Neighbors
* Random Forest
* Gaussian Naive Bayes

It uses 5-fold stratified cross-validation and reports accuracy, weighted precision, weighted recall, and weighted F1. Randomized search is then used to tune Random Forest and Logistic Regression with weighted F1 as the search score.

---

## Project Structure

```text
Penguin_sepecies_classifier/
│
├── Data/
│   └── Penguin Species Prediction Dataset.csv
├── Notebook/
│   └── Penguin_species_prediction.ipynb
├── app.py
├── penguin_model.pkl
├── label_encoder.pkl
├── bg.jpg
└── README.md
```

---

## Data Preparation

The notebook inspects the dataset shape, data types, missing values, and duplicate rows. It builds preprocessing pipelines that impute missing numeric values with the mean and categorical values with the most frequent value.

Categorical input features are one-hot encoded for the applicable classifiers. Numeric features are scaled for Logistic Regression, K-Nearest Neighbors, and Gaussian Naive Bayes; the Decision Tree and Random Forest pipelines use unscaled numeric inputs. The target species is label encoded.

---

## Exploratory Data Analysis

The notebook explores the feature distributions and relationships using a pair plot, numeric correlation and covariance, and species counts. These steps help inspect how the measurements vary across the dataset before fitting models.

---

## Model Training & Evaluation

The data is split into training and test sets with an 80/20 split and a fixed random state. Model comparison uses stratified 5-fold cross-validation on the training data. The notebook ranks candidate models by weighted recall, tunes Random Forest and Logistic Regression, then evaluates fitted candidates on the held-out test set.

Evaluation includes accuracy, a confusion matrix, and a classification report with per-class precision, recall, and F1. The notebook does not record a fixed performance summary in this README; rerun it to produce metrics for the current environment and data.

---

## Prediction App

The Streamlit app collects island, sex, culmen length and depth, flipper length, and body mass. It sends these values to the saved model pipeline and displays the predicted species.

The app loads `penguin_model.pkl` and `label_encoder.pkl`, reads the CSV under `Data/`, and uses `bg.jpg` for its background. Keep these files in their listed locations when running the app.

---

## How to Run

### 1. Install dependencies

From the project root, install the libraries used by the notebook and app:

```bash
python -m pip install streamlit pandas numpy scikit-learn joblib jupyter matplotlib seaborn
```

### 2. Launch the prediction app

```bash
streamlit run app.py
```

### 3. Open the notebook

Run Jupyter from the `Notebook` folder so its relative path to the dataset resolves:

```bash
cd Notebook
jupyter notebook Penguin_species_prediction.ipynb
```

Rerun the notebook's training and model export cells to regenerate the saved artifacts after changing the data or training process.

---

## Future Improvements

* Add a requirements file to make environment setup reproducible.
* Add automated checks for input values and missing or invalid data.
* Record the selected model's test metrics and compare them with a simple baseline.
* Add a saved model training script so artifacts can be regenerated without running notebook cells manually.
* Improve the app with prediction confidence and clearer feature descriptions.
