from sklearn.linear_model import LinearRegression
import pandas as pd

def train_regression(df):

    X = df[['age', 'weight']]
    y = df['systolic_bp']

    model = LinearRegression()
    model.fit(X,y)

    return model