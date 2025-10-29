# Titanic Data Engineering Project

This project demonstrates containerized data engineering and machine learning pipelines in **both Python and R** using the Titanic dataset.  
The goal is to practice reproducible data processing, model training, and deployment inside Docker containers, ensuring that anyone can reproduce results easily.


## Project Structure
```
titanic-data-engineering/
├── data/
│ ├── train.csv
│ ├── test.csv
│ └── gender_submission.csv
│
├── src/
│ └── main.py # Python pipeline: data loading, cleaning, logistic regression, predictions
│
├── src_r/
│ ├── main.R # R pipeline: data cleaning, logistic regression (caret), predictions
│ ├── install_packages.R # Installs required R libraries
│ └── Dockerfile # Dockerfile for R container
│
├── Dockerfile # Dockerfile for Python container
├── requirements.txt # Python dependencies
├── predictions.csv # Model predictions output (Python)
├── .gitignore
└── README.md
```

## Overview

The project runs two independent pipelines (Python and R) to predict passenger survival on the Titanic dataset.

### Python container:
- Loads and preprocesses data from `/data/train.csv`
- Removes duplicates, fills missing values, and encodes categorical features
- Trains a logistic regression model using `scikit-learn`
- Saves predictions to `predictions.csv`

### R container:
- Loads and cleans data using `tidyverse`
- Handles missing values and performs a logistic regression model using `caret`
- Outputs predictions to `predictions_r.csv`
- Prints training accuracy and a sample of predictions in the console

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/raghavchhabra123/titanic-data-engineering.git
cd titanic-data-engineering
```
### Verify Data Files

Ensure your `data/` folder contains:


Ensure your data/ folder contains:
```
data/
├── train.csv
├── test.csv
└── gender_submission.csv
```
If you downloaded the Kaggle zip file, extract it and place all three CSVs into the /data directory.

### Build the Docker image:
docker build -t titanic-model-py --no-cache -f Dockerfile .

### Run the container:
docker run titanic-model-py

### Expected Output:

Data loaded successfully. Shape: (891, 12)
Duplicates removed. Shape: (891, 12)
Missing values handled.
Feature engineering complete.
Model trained successfully.
Predictions saved to predictions.csv

Sample Predictions:
PassengerId  Name                          PredictedSurvival
1            Braund, Mr. Owen Harris       0
4            Futrelle, Mrs. Jacques Heath  1
5            Allen, Mr. William Henry      0
...

### R Pipeline:

### Build the Docker Image:
docker build -t titanic-model-r --no-cache -f src_r/Dockerfile .

### Run the Container:
docker run titanic-model-r

### Expected Output:
Packages installed successfully
Data loaded successfully. Shape: 891 rows, 12 columns
Duplicates removed
Missing values handled
Feature engineering complete
Model trained successfully
Predictions saved to predictions_r.csv

Sample Predictions:
Name                                    PredictedSurvival
Braund, Mr. Owen Harris                 0
Futrelle, Mrs. Jacques Heath (Lily)     1
Allen, Mr. William Henry                0
...

### Outputs:

After running both containers, you should see:
predictions.csv        # Output from Python model
predictions_r.csv      # Output from R model


Both contain passenger names and their predicted survival values.

### Requirements Summary

Python:
pandas
scikit-learn

R:
tidyverse
caret
lattice

### How to Reproduce
1. Clone the repository

git clone https://github.com/raghavchhabra123/titanic-data-engineering.git
cd titanic-data-engineering

2. Add your Titanic dataset files to /data

3. Build and run containers:

   For Python:
   docker build -t titanic-model-py -f Dockerfile .
   docker run titanic-model-py

   For R:
   docker build -t titanic-model-r -f src_r/Dockerfile .
   docker run titanic-model-r

4. Verify output files in the project root.

### Summary

This project showcases:
Using Docker for reproducible ML environments
Implementing and comparing Python + R pipelines

Author: Raghav Chhabra
Date: October 2025
