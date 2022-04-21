import numpy as np

vector1 = np.array([1,2,3,4,5])

print('vector1 = ', vector1)

vector2 = vector1 + vector1

print('vector2', vector2)

vector3 = 3*vector2

print('vector3 : ', vector3)

matrix1 = np.array(([0,1],[1,3]))

print(matrix1)

print('Matrix1 shape = ',matrix1.shape)

print('Matrix1 * Matrix1 = \n',(matrix1*matrix1))
