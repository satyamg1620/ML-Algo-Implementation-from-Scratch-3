from typing import Union
import pandas as pd
import numpy as np

def rmse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the rmse as float
    """
    assert y_hat.size == y.size
    return (((y_hat - y) ** 2).mean()) ** 0.5

def mse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the rmse as float
    """
    assert y_hat.size == y.size
    return (((y_hat - y) ** 2).mean())


def mae(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the mae as float
    """

    assert y_hat.size == y.size
    return (y_hat - y).abs().mean()


def predict(X, coef_, fit_intercept):
  # Funtion to run the LinearRegression on a test data point
  # Make predictions using the regression coefficients
  
  # print(X, coef_)
  # print(X.shape, coef_.shape)
  
  if fit_intercept:
    X = np.hstack((np.ones((X.shape[0], 1)), X))
  y_pred = np.dot(X, coef_)
  return y_pred


def rss(y_hat: pd.Series, y: pd.Series):
  assert y_hat.size == y.size
  return sum((y_hat - y)**2)