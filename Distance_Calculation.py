import math
import numpy as np
import matplotlib.pyplot as plt

#B- 4380 angstroms
#V- 




#Data from SN 2018hna
#Variables
z = 0.00241 #red shift
v = [6485, 5355, 4713, 3861, 3566] #in km per sec

#t = [12.1, 15.1, 20.1, 37.2, 46.1] # days
t = [2458423.4, 2458426.4, 2458431.4, 2458447.5, 2458457.4] #julian days

theta = [1,1,1,1,1]#Mag theta

temp = [0, 0, 0, 0, 0] #in kelvin

#Test variables for magnitude no flux
ma = [16.08,16.0,15.81,15.19,14.79]#pretty sure I was given these by Dr. Lusk at some point

dilution_factor = [1,1,1,1,1]
synthMag = [1,1,1,1,1]

#Calculations
for i in range(len(t)):
    dilution_factor[i] = 0.5356+0.2116*((10**4)/(temp[i]))-0.0384*((10**4/temp[i])**2)
    synthMag[i] = -44.766+6.793*((10**4)/(temp[i]))-4.523*((10**4/temp[i])**2)+2.695*((10**4/temp[i])**3)-0.809*((10**4/temp[i])**4)+0.096*((10**4/temp[i])**5)
    theta[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(ma[i] - synthMag[i])+0.5*math.log(1+z))



#Graph
# x axis values
res = []
for i in range(len(v)):
    res.append((theta[i])/ ((v[i]*24*60*60)))

x = res

# corresponding y axis values
y = t #days

  
# plotting the points
plt.scatter(x, y, c ="blue")

#find line of best fit
a, b = np.polyfit(x, y, 1)
mx = [i * a for i in x]

#add line of best fit to plot
plt.plot(x, mx+b)

#add fitted regression equation to plot
plt.text(0, 0, 'y = ' + '{:0.2e}'.format(b) + ' + ' + '{:0.2e}'.format(a) + 'x', size=5)
print("y = "+str(round(a/3.086E13/1000000,2))+"x + (" + str(round(b,2)) + ")")

print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')

# naming the x axis
plt.xlabel(r"$\dot{\Theta}$/v")

# naming the y axis
plt.ylabel('t(days)')
  
# giving a title to my graph
plt.title(r"$\dot{\Theta}$/v"+' of SN 2018hna over time')
  
# function to show the plot
plt.show()