import math
import numpy as np
import matplotlib.pyplot as plt

#importinng files for calcualating tempuratures
import EPMvariables as Var

#Data from SN 2018hna
#Variables
theta = [0,0,0,0,0]#Mag theta
dilution_factor = [0,0,0,0,0]
synthMag = [0,0,0,0,0]

print()
print()
print()
print()


#Calculations
for i in range(len(Var.tdays)):
    for x in range(3):
        dilution_factor[i] += Var.BVdilution[x]*(((10**4)/(Var.BVtemp[i]))**(x))
print('dilution_factor',dilution_factor)
print()




for i in range(len(Var.tdays)):
    for x in range(6):
        synthMag[i] += Var.Bconst[x]*(((10**4)/(Var.BVtemp[i]))**(x))
   
    theta[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(Var.Bmag[i] - synthMag[i])+0.5*math.log(1+Var.z))
print("Theta",theta)
print("synthMag",synthMag)

#Graph
# x axis values
res = []
for i in range(len(Var.v)):
    res.append((theta[i])/ ((Var.v[i]*24*60*60)))

x = res

# corresponding y axis values
y = Var.tjulian #days
  
# plotting the points
plt.scatter(x, y, c ="blue")

#find line of best fit
a, b = np.polyfit(x, y, 1)
mx = [i * a for i in x]

print("Distance B: "+str(round(a,2))+" Mpc")

theta = [0,0,0,0,0]#Mag theta
synthMag = [0,0,0,0,0]
print()

for i in range(len(Var.tdays)):
    for x in range(6):
        synthMag[i] += Var.Vconst[x]*(((10**4)/(Var.BVtemp[i]))**(x))

    theta[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(Var.Vmag[i] - synthMag[i])+0.5*math.log(1+Var.z))
print("Theta",theta)
print("synthMag",synthMag)


#Graph
# x axis values
res = []
for i in range(len(Var.v)):
    res.append((theta[i])/ ((Var.v[i]*24*60*60)))

x = res

# corresponding y axis values
y = Var.tjulian #days
  
# plotting the points
plt.scatter(x, y, c ="blue")

#find line of best fit
a, b = np.polyfit(x, y, 1)
mx = [i * a for i in x]

print("Distance V: "+str(round(a,2))+" Mpc")
print()
print()
print()
print()
