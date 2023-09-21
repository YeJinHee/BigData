import matplotlib.pyplot as plt
# import numpy as np 없어도 됨
import pandas as pd
from sklearn.linear_model import LinearRegression

# Download and prepare the data loding
data_root = "https://github.com/ageron/data/raw/main/"
life_satisfaction = pd.read_csv(data_root + "lifesat/lifesat.csv")
print(Llife_satisfaction.tail(5))
print(Lifesat.shape)
print(Lifesat.descibe(5))

 print)Lisear;
X = lifesat[["GDP per capita (USD)"]].values #2차원 배열
y = lifesat[["Life satisfaction"]].values

print (x)
print(y)

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[37_655.2]]  # Cyprus' GDP per capita in 2020
print(life_satisfaction)
print(model.predict(X_new)) # outputs [[6.30165767]]