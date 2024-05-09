import random

import numpy
import numpy  as np


x = np.linspace(-1.0, 1.0, 50)
y = np.random.rand(50) - 0.5
r = np.ones(50)
g = np.zeros(50)
b = np.zeros(50)

vertices = np.dstack([x, y, r, g, b])
print(vertices)

a=numpy.ones((5,2))
b=numpy.ones((5,2))

sub=numpy.subtract.outer(a[:,0], a[:,0])
print(a,b,sub)

array1 = numpy.random.rand(1, 3) - 0.5
print(array1)

point_list=[]
for x in range(320):
    for y in range(160):
        point=[x,y,0]
        point_list.append(point)




print(point_list)
coords = numpy.zeros((160*320, 3))
y,x= numpy.mgrid[0:160, 0:320]
coords[:, 0] =x.flatten()
coords[:, 1] =y.flatten()

theta= numpy.deg2rad(3)
matrix_r = numpy.matrix([[numpy.cos(theta), -numpy.sin(theta), 0], [numpy.sin(theta), numpy.cos(theta), 0], [0, 0, 1]])
print(matrix_r)

obj = numpy.dot(matrix_r, [1, 23, 3])
print(obj)

vector_list=[]
for index in range(160*320):
    vector=[random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1) ]
    vector_list.append(vector)

print(vector_list)

