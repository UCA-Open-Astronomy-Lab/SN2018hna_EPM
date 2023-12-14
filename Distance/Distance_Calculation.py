import math
import numpy as np
import matplotlib.pyplot as plt

#importinng files for calcualating tempuratures
import Data.EPMvariables as Var

#Data from SN 2018hna
#Variables
z = 0.00241 #red shift
v = [6485, 5355, 4713, 3861, 3566] #in km per sec

#t = [12.1, 15.1, 20.1, 37.2, 46.1] # days
t = [2458423.4, 2458426.4, 2458431.4, 2458447.5, 2458457.4] #julian days

theta = [0,0,0,0,0]#Mag theta
dilution_factor = [0,0,0,0,0]
synthMag = [0,0,0,0,0]

temp = [] #in kelvin
for i in range(len(t)):
    temp.append(Var.BVtemp[i])

#variables for magnitude no flux
mag = [] #in kelvin
for i in range(len(t)):
    mag.append(Var.Bmag[i])




#Calculations
for i in range(len(t)):
    for x in range(6):
        synthMag[i] += Var.Bconst[x]*(((10**4)/(temp[i]))**(x))
    for x in range(3):
        dilution_factor[i] += Var.BVdilution[x]*(((10**4)/(temp[i]))**(x))


    #theta[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(mag[i] - synthMag[i])+0.5*math.log(1+z))
print(dilution_factor)


for i in range(len(t)):
    theta[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(mag[i] - synthMag[i])+0.5*math.log(1+z))























#Graph
# x axis values
res = []
for i in range(len(v)):
    res.append((theta[i])/ ((v[i]*(24*60*60))))

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
#print("y = "+str(round(a/3.086E13/1000000,2))+"x + (" + str(round(b,2)) + ")")

print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')
print("Distance : "+str(round(a/3.086E13/1000000,2))+" Mpc")

# naming the x axis
plt.xlabel(r"$\dot{\Theta}$/v")

# naming the y axis
plt.ylabel('t(days)')
  
# giving a title to my graph
plt.title(r"$\dot{\Theta}$/v"+' of SN 2018hna over time')
  
# function to show the plot
plt.show()