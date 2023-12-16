import math
import numpy as np
import matplotlib.pyplot as plt

T = [np.Infinity, 25000, 20000, 12000, 8000, 6000, 5000, 4000, 3300, 3000] #temp from MatthewsSandage1963
UB = [-1.28, -1.13, -1.06, -0.83, -0.53, -0.26, -0.10, 0.36, 0.78, 1.07]#B-V for the temps listed above from MatthewsSandage1963
K = 0
C = 0

for i in range(len(T)):
    T[i] = 10000/T[i]

#Graph
# x axis values
x = UB

# corresponding y axis values
y = T
  
# plotting the points
plt.scatter(x, y, c ="blue")

#find line of best fit
a, b = np.polyfit(x, y, 1)
mx = [i * a for i in x]

#add line of best fit to plot
plt.plot(x, mx+b)

#add fitted regression equation to plot
plt.text(0, 0, 'y = ' + '{:0.2e}'.format(a) + 'x + ' + '{:0.2e}'.format(b), size=5)
#print("10000K/T = "+str(a)+"x + " + str(b))

#print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')
K = a
C = b

# naming the x axis
plt.xlabel('B-V')

# naming the y axis
plt.ylabel('10000K/T')
  
# giving a title to my graph
plt.title('B-V Tempurature Fit From Data provided by Cietti et al.')
  
# function to show the plot
plt.show()

'''

'''
