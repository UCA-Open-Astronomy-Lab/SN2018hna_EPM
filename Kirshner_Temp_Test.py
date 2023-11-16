import math
import numpy as np
import matplotlib.pyplot as plt



#10000K/T = K(B-V)+C



days = 5

T = [np.Infinity, 25000, 20000, 12000, 8000, 6000, 5000, 4000, 3300] #temp from MatthewsSandage1963
BV = [-0.44, -0.21, -0.15, 0.05, 0.35, 0.63, 0.79, 1.13, 1.44]#B-V for the temps listed above from MatthewsSandage1963

temp = []
K = []#slope of the graph
B = [17.03, 17.07, 16.96, 16.27, 15.86]#Blue light mag
V = [16.11, 16.01, 15.84, 15.22, 14.82]#Visiblle light mag
C = 0.48#constant based on color filters

'''
for i in range(days):
    temp.append = 10000/( K[i] ( B[i] - V[i] ) + C )
    '''

#Graph
# x axis values
xval = []
for i in range(days):
    xval.append(B[i]-V[i])

x = BV

# corresponding y axis values
yval = []
for i in range(days):
    yval.append(10000/T[i])

y = T
  
# plotting the points
plt.scatter(x, y, c ="blue")

#find line of best fit
a, b = np.polyfit(x, y, 1)
mx = [i * a for i in x]

#add line of best fit to plot
plt.plot(x, mx+b)

#add fitted regression equation to plot
plt.text(0, 0, 'y = ' + '{:0.2e}'.format(b) + ' + ' + '{:0.2e}'.format(a) + 'x', size=5)
print("10000K/T = "+str(a)+"x + " + str(b))

#print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')

# naming the x axis
plt.xlabel('B-V')

# naming the y axis
plt.ylabel('10000K/T')
  
# giving a title to my graph
plt.title('B-V Tempurature of SN 2018hna over time')
  
# function to show the plot
plt.show()