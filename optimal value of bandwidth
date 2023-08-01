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

# Bandwidth selection function
gwr_selector = Sel_BW(coords, y, X_scaled)
gwr_bw = gwr_selector.search(search_method='golden_section', criterion='AICc')
print('The optimal bandwidth size is:', gwr_bw)
