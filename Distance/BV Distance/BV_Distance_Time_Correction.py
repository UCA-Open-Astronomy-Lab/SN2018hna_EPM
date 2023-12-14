import math
import numpy as np
import matplotlib.pyplot as plt

#importinng files for calcualating tempuratures
import Data.EPMvariables as Var

#Data from SN 2018hna
#Variables
dilution_factor = [0,0,0,0,0] #dilution factor calculated using BV coefficients
synthMagB = [0,0,0,0,0] #synthetic magnitude using B coefficients 
synthMagV = [0,0,0,0,0] #synthetic magnitude using V coefficients 
thetaB = [0,0,0,0,0] #theta value for B filter
thetaV = [0,0,0,0,0] #theta value for V filter

#Calculations
'''Dilution factor calulation, its the same for both B and V'''
for i in range(len(Var.tdays)):
    for x in range(3):
        dilution_factor[i] += Var.BVdilution[x]*(((10**4)/(Var.BVtemp[i]))**(x))

'''Calculation for the B synth mag, distance and time of explosion'''
for i in range(len(Var.tdays)):
    for x in range(6):
        synthMagB[i] += Var.Bconst[x]*(((10**4)/(Var.BVtemp[i]))**(x))
   
    thetaB[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(Var.Bmag[i] - synthMagB[i])+0.5*math.log(1+Var.z))

res = []
for i in range(len(Var.v)):
    res.append((thetaB[i])/ ((Var.v[i]*24*60*60)))
print(res)

x = res


y = Var.tdays

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
print("B Mag Distance: "+str(round(a/3.086E13/1000000,2))+" Mpc")
print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')

