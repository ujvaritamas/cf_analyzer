import pandas as pd

def create_dataframe(csv_file):
    df = pd.read_csv(csv_file, index_col=False)
    print(df.to_string())


    print(df.describe())

    print(df['age'].mean())

create_dataframe("parsedAthletes.csv")