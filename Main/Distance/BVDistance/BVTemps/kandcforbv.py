import math
import numpy as np
import matplotlib.pyplot as plt

T = [np.Infinity, 25000, 20000, 12000, 8000, 6000, 5000, 4000, 3300] #temp from MatthewsSandage1963
BV = [-0.44, -0.21, -0.15, 0.05, 0.35, 0.63, 0.79, 1.13, 1.44]#B-V for the temps listed above from MatthewsSandage1963
K = 0
C = 0

for i in range(len(T)):
    T[i] = 10000/T[i]

#Graph
# x axis values
x = BV

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
C = 0.48

# naming the x axis
plt.xlabel('B-V')

# naming the y axis
plt.ylabel('10000K/T')
  
# giving a title to my graph
plt.title('B-V Tempurature Fit From Data provided by Cietti et al.')
  
# function to show the plot
#plt.show()

'''
The values above are values used to equate color filters to a tempurature using the equation 10,000Kel/T = K(B-V)+C.
Kirsner and Kwan suggested that for the use in determining B-V tempuratures of Type II supernovae, we should use the C value of C = 0.48,
opposed to the C = 0.78 from this program based on the data provided by Cietti et al. These values are only B-V color tempurature. They must
also be corrected for extinction and redshift before being used in the equation above.

To determine the color temperatures for different color filters, I suspect you need to use blackbodies to fit a 
temperature to a color filter difference. 
'''
