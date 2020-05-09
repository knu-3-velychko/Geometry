import matplotlib.pyplot as plt
import numpy as np

def Bezier_Interpolation(point_list, t):
    if len(point_list) == 1:
        return point_list[0]
    else:
        P1 = Bezier_Interpolation(point_list[0:-1], t)
        P2 = Bezier_Interpolation(point_list[1:], t)
        nt = 1. - t
        return (nt * P1[0] + t * P2[0], nt * P1[1] + t * P2[1])

with open('points.txt') as file:
    points = []
    for line in file:
        row = line.split()
        points.append([float(row[0]), float(row[1])])

x, y = [], []
t = np.arange(0, 1, 0.001)
for val in t:
    b = Bezier_Interpolation(points,val)
    x.append(b[0])
    y.append(b[1])

def column(matrix, i):
    return [row[i] for row in matrix]

plt.plot(x,y)
plt.scatter(column(points,0), column(points,1))
plt.show()