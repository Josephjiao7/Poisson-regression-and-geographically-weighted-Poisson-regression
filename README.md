# Geographically-weighted-Poisson-regression
The code of python for poisson regression and geographically weighted Poisson regression.

In traditional Poisson regression, it is assumed that the number of events follows a Poisson distribution, and a linear model is used to establish the relationship between the independent variables and the event occurrence rate. However, in spatial data analysis, the spatial heterogeneity of the data may lead to poor model fitting, meaning that the model's relationships may not be globally uniform but rather vary across different geographical locations.

Geographically Weighted Regression (GWR) aims to address the issue of spatial heterogeneity in spatial data. It achieves this by introducing a spatial weight matrix, allowing the model parameters to vary across each geographic location, thus better accommodating the local variations in spatial data.

We used the Sel_BW class from the mgwr (MultiGWR) library to determine the optimal bandwidth. Sel_BW is a bandwidth selector for Geographically Weighted Regression (GWR) models, and it uses criterion-based optimization to find the best bandwidth size.

The code of R, as you can see at https://zia207.github.io/geospatial-r-github.io/geographically-weighted-poisson-regression.html
