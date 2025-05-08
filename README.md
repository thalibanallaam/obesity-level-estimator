# Obesity Level Estimator

The Obesity Level Estimator is a machine learning application designed to predict an individual's obesity category based on their dietary habits and physical condition. Utilizing a dataset from the UCI Machine Learning Repository, the project aims to provide insights into obesity levels through data analysis and predictive modeling.

## Repository Outline
```
1. README.md - This file
2. Obesity_Estimation.ipynb - The main notebook containing the data analysis, data processing and modeling process.
3. Obesity_Estimation_Inference.ipynb - Model inference of the model made in the main notebook.
4. url.txt - File containing URL of the dataset and model deployment.
5. Deployment - Folder containing files required for the deployment.
    a. app.py - The main script.
    b. eda.py - Script for the deployment of the Exploratory Data Analysis (EDA) results.
    c. prediction.py - Script for the deployment of the model inference.
```

## Problem Background
Through this project, we analyze health-related factors to create a machine learning model that can predict an individual’s obesity level based on their physical condition and daily habits. In 2018, Indonesia had an obesity rate of 21.8% which is higher than the average world obesity rate of 12.5%. The Indonesian government plans to reduce this number to 3% by 2030. This machine learning model can help doctors and nutritionists in diagnosing their patients.

## Project Output
The output of the project is a deployable machine learning model that can predict an individual's obesity level based on the required physical condition and daily habits.

## Data
The dataset contains information regarding an individual's obesity level based on their physical condition and daily habits. The people in the dataset represents people from Mexico, Peru, and Colombia. The data was collected through a web platform survey and the final result was a total of 2111 entries with 17 features. The features represents the individual's physical condition as well as their daily habits. The target is "Obesity Level" which is represented by NObesity in the original dataset and divided into seven different classes, including `Insufficient Weight`, `Normal Weight`, `Overweight Level I`, `Overweight Level II`, `Obesity Type I`, `Obesity Type II` and `Obesity Type III`.

## Method
This is a machine learning project that utilize supervised learning algorithms. We tested five different algorithms (KNN, SVM, Decision Tree, Random Forest, and XGBoost) to solve our classification case.

XGBoost was chosen as the best performing model based on the results of cross-validation. The model was later tuned using GridSearchCV.

## Stacks
Language:
- Python

Tools:
- Visual Studio Code
- Google Colab

Library:
- Pandas
- NumPy
- SciPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Pickle

## Reference
Dataset:
- https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition
- https://www.sciencedirect.com/science/article/pii/S2352340919306985

Deployment:
- https://huggingface.co/spaces/thalibanallaam/ObesityLevelPrediction

Exploratory Data Analysis:
- https://vitalflux.com/differences-between-random-forest-vs-adaboost/
- https://stacyy.medium.com/itp-449-exploratory-data-analysis-project-obesity-levels-based-on-eating-habits-and-physical-82fa10775c2e
- https://www.health.harvard.edu/staying-healthy/why-people-become-overweight
- https://www.betterhealth.vic.gov.au/health/healthyliving/Alcohol-and-weight-gain
- https://www.cepal.org/en/insights/malnutrition-among-children-latin-america-and-caribbean

---
