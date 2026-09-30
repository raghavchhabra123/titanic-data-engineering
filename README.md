# Titanic Data Engineering: Containerized Python and R Pipelines

A coursework project on reproducible data processing. The same Titanic survival pipeline (load, clean, engineer features, fit a logistic regression, write predictions) is implemented twice, in **Python** and in **R**, and each runs inside its own Docker container.

## Project structure

```
titanic-data-engineering/
├── data/
│   └── README.md          # the Kaggle CSVs go here (not committed)
├── src/
│   └── main.py            # Python pipeline: pandas + scikit-learn
├── src_r/
│   ├── main.R             # R pipeline: tidyverse + caret
│   ├── install_packages.R # installs the R dependencies
│   └── Dockerfile         # R container
├── Dockerfile             # Python container
├── requirements.txt       # Python dependencies
└── README.md
```

## What each pipeline does

**Python (`src/main.py`)**
- Loads `data/train.csv`, removes duplicates, and fills missing `Age`, `Fare`, and `Embarked` values
- Engineers `FamilySize`, encodes `Sex`, and one-hot encodes `Embarked`
- Trains a scikit-learn logistic regression on an 80/20 split
- Writes predictions for the held-out rows to `predictions.csv`

**R (`src_r/main.R`)**
- Loads `data/train.csv` with `tidyverse`; drops rows with missing `Age`, `Fare`, or `Embarked` instead of imputing them
- Engineers `FamilySize` and encodes `Sex`
- Uses `caret` for an 80/20 split and fits a logistic regression (`glm`)
- Writes predictions for the held-out rows to `predictions_r.csv`

Both pipelines use only Kaggle's labeled `train.csv`, split into training and held-out rows.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/raghavchhabra123/titanic-data-engineering.git
   cd titanic-data-engineering
   ```

2. Download `train.csv`, `test.csv`, and `gender_submission.csv` from [Kaggle](https://www.kaggle.com/competitions/titanic/data) and put them in `data/`. The CSVs are not committed to this repository.

## Run the Python pipeline

```bash
docker build -t titanic-model-py -f Dockerfile .
docker run --rm -v "$PWD":/app titanic-model-py
```

## Run the R pipeline

```bash
docker build -t titanic-model-r -f src_r/Dockerfile .
docker run --rm -v "$PWD":/app titanic-model-r
```

Mounting the project folder (`-v "$PWD":/app`) makes `predictions.csv` and `predictions_r.csv` appear in the project root on your machine. Without the mount, they are written inside the container only.

## Expected console output (Python)

```
Data loaded successfully. Shape: (891, 12)
Duplicates removed. Shape: (891, 12)
Missing values handled. Remaining NA count:
...
Model trained successfully.
Training Accuracy: ...
Predictions saved to predictions.csv

Sample Predictions:
PassengerId  Name                          PredictedSurvival
...
```

## What this project demonstrates

- Packaging data pipelines in Docker so they run the same way on any machine
- Implementing and comparing equivalent pipelines in Python and R
- Keeping raw data out of version control

*Author: Raghav Chhabra · October 2025*
