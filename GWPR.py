import pandas as pd
import numpy as np
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW
from mgwr.gwr import Poisson
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'dataset.csv')

# Read the data's x, y coordinates
u = data['x']
v = data['y']
coords = list(zip(u, v))

# Read the dependent variable
y = data['y1'].values

# Read the independent variables and perform standardization
X = data[["X1", "X2", "X3", "X4"]].values
X = np.array(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# GWR fitting, bw (bandwidth) is the parameter that needs to be calculated to determine its optimal value in GWR
model = GWR(coords, y, X_scaled, family=Poisson(), bw=71, fixed=False, kernel='bisquare', sigma2_v1=True).fit()

# Output GWR fitting results
print(model.summary())
