import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random


n = int(input("how many points"))
fig = plt.figure()
ax = plt.axes
x = []
y = []
z = []
sum_of_x = 0
sum_of_x_squared = 0
sum_of_y = 0
sum_of_y_squared = 0
sum_of_xy = 0

for i in range(0, n):
    x.append(random.randint(-10, 10))
    y.append(random.randint(-10, 10))

for i in range(0, n):
    sum_of_xy += x[i]*y[i]
    sum_of_x += x[i]
    sum_of_y += y[i]
    sum_of_x_squared += x[i]**2
    sum_of_y_squared += y[i]**2

sxx = sum_of_x_squared - ((sum_of_x**2)/n)
syy = sum_of_y_squared - ((sum_of_y**2)/n)
sxy = sum_of_xy - ((sum_of_x*sum_of_y)/n)
PMCC = int((sxy)/(np.sqrt(sxx*syy)))

for i in range(0, n):
    z.append(PMCC)


print(PMCC)
print(x)
print(y)
plt.plot(x, z)
plt.scatter(x,y)
plt.show()