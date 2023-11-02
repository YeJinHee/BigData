import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
#a = np.random.uniform(size=10).reshape(2, 5) #균등분포
a = np.random.uniform(size=10000)
b = np.random.normal(50, 1, 100) #정규분포
print(a)
print(b)
plt.hist(b)
plt.show()