import numpy as np
a1 = np.ones((3, 3))
a1[:, 2] = 2
print(a1)
a2 = np.full((3, 3), 5)
print(a2)
a3 = np.eye(3) #단위 행렬
print(a3)
a4 = a3[:2, 1:] #일부 잘라서 가져오기
print(a4)
a5 = a3[2:, :]
print(a5)