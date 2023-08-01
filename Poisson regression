import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import numpy as np


# Load the data
data = pd.read_csv(r'dataset.csv')

# Load the dependent variable
y = data['y1']

# Load the independent variables and perform standardization
X = data[["X1", "X2", "X3", "X4"]].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Build the Poisson regression model
poisson_model = sm.Poisson(y, X_scaled).fit()

# Output regression results
print(poisson_model.summary())
