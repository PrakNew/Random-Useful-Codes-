

import pandas as pd

df = pd.read_csv("loan_small.csv")

dt[cols] = dt[cols].astype("category")

df2 = pd.get_dummies(df)# One hot encoding

df = df.fillna(df.median())

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

df = df.drop(["Loan_ID"], axis=1)


columns = df.columns


for cols in df.columns:
    df[cols] = df[cols].fillna(df[cols].mode()[0])


data_to_scale = df.loc[:, ["ApplicantIncome", "CoapplicantIncome", "LoanAmount"]]

df.dtypes

from sklearn.preprocessing import StandardScaler

ss_scaler = StandardScaler().fit_transform(data_to_scale)

from sklearn.model_selection import train_test_split as tts

X = data_to_scale.iloc[:, :-1]
Y = data_to_scale.iloc[:, -1]

x_train, x_test, y_train, y_test = tts(X, Y, test_size=0.2, random_state=1234)
