import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_and_process_data():
    # Load Titanic dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print("Data loaded successfully. Shape:", df.shape)

    # ---------------------------------------
    # 🧹 Basic Data Cleaning
    # ---------------------------------------
    # Drop duplicate rows if any
    df = df.drop_duplicates()
    print("Duplicates removed. Shape:", df.shape)

    # Fill missing numeric values (Age, Fare) with median
    df["Age"].fillna(df["Age"].median(), inplace=True)
    df["Fare"].fillna(df["Fare"].median(), inplace=True)

    # Fill missing categorical values (Embarked) with mode
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

    # Drop rows with missing critical values if any remain
    df = df.dropna(subset=["Sex", "Survived"])
    print("Missing values handled. Remaining NA count:\n", df.isna().sum())

    # ---------------------------------------
    # Feature Engineering
    # ---------------------------------------
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

    # Select features and target
    X = df[["Pclass", "Age", "Fare", "Sex", "FamilySize", "Embarked_Q", "Embarked_S"]]
    y = df["Survived"]

    # ---------------------------------------
    # Split Data
    # ---------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------------------------------------
    # Train Model
    # ---------------------------------------
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, model.predict(X_train))
    print(f"Model trained successfully.")
    print("Training Accuracy:", round(train_acc, 3))

    # ---------------------------------------
    # 💾 Save Predictions (as per updated instructions)
    # ---------------------------------------
    y_pred = model.predict(X_test)

    # Re-attach PassengerId and Name (for readability)
    test_passengers = df.loc[X_test.index, ["PassengerId", "Name"]].reset_index(drop=True)

    output = pd.DataFrame({
        "PassengerId": test_passengers["PassengerId"],
        "Name": test_passengers["Name"],
        "PredictedSurvival": y_pred
    })

    # Save to CSV
    output.to_csv("predictions.csv", index=False)
    print("✅ Predictions saved to predictions.csv")

    # Display a sample of predictions in terminal
    print("\n🔍 Sample Predictions:")
    print(output.head(10).to_string(index=False))

if __name__ == "__main__":
    load_and_process_data()
