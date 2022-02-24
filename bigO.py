#  Student Name: Marilyn Shen

#  Student UT EID: mys467

#  Partner Name: Jennifer Truong

#  Partner UT EID: jat5244

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 2/22/2022

#  Date Last Modified: 2/24/2022

# Problem 1: Use python to create 3 different plots
import numpy as np
import matplotlib.pyplot as plt


# first plot, going from x = 0 to x = 5
msize = 5

t = np.arange(0, msize, 0.1)

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**3.5 - 2**10, 'bs', t, 100*t**2.1 + 50, 'g^')

plt.plot(t, (2 ** 10) * t + (2 ** 10), 'red', t, t ** 3.5 - 1000, 'blue', t,
         100*t**2.1 + 50, 'green')

plt.xlim(0, msize)
plt.rcParams["figure.figsize"] = (7, 7)
plt.show()


# second plot, going from x = 0 to x = 15
msize = 15

t = np.arange(0, msize, 0.1)

plt.plot(t, (2 ** 10) * t + (2 ** 10), 'red', t, t ** 3.5 - 1000, 'blue', t,
         100*t**2.1 + 50, 'green')

plt.xlim(0, msize)
plt.rcParams["figure.figsize"] = (7, 7)
plt.show()


# third plot, going from x = 0 to x = 50
msize = 50

t = np.arange(0, msize, 0.1)

plt.plot(t, (2 ** 10) * t + (2 ** 10), 'red', t, t ** 3.5 - 1000, 'blue', t,
         100*t**2.1 + 50, 'green')

plt.xlim(0, msize)
plt.rcParams["figure.figsize"] = (7, 7)
plt.show()
