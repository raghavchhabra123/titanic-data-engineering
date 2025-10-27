import pandas as pd

def load_and_process_data():
    # Load Titanic dataset from an online source (no local file)
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)

    # Simple transformation
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    print(df.head())
    print("\nAverage survival rate:", round(df["Survived"].mean(), 3))

if __name__ == "__main__":
    load_and_process_data()
