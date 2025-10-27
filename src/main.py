import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_and_process_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df = df.dropna(subset=["Age", "Fare", "Embarked", "Sex"])
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

    X = df[["Pclass", "Age", "Fare", "Sex", "FamilySize"]]
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))

    print("Training Accuracy:", round(train_acc, 3))
    print("Test Accuracy:", round(test_acc, 3))

if __name__ == "__main__":
    load_and_process_data()
