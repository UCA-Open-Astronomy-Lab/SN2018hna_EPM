import math
import numpy as np

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
x = res

y = Var.tjulian #days

a, b = np.polyfit(x, y, 1)

print("B Mag Distance: "+str(round(a/3.086E13/1000000,2))+" Mpc")
print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')
print()


'''Calculation for the V synth mag, distance and time of explosion'''
for i in range(len(Var.tdays)):
    for x in range(6):
        synthMagV[i] += Var.Vconst[x]*(((10**4)/(Var.BVtemp[i]))**(x))

    thetaV[i] = 10**(-math.log(dilution_factor[i],10)-0.2*(Var.Vmag[i] - synthMagV[i])+0.5*math.log(1+Var.z))

res = []
for i in range(len(Var.v)):
    res.append((thetaV[i])/ ((Var.v[i]*24*60*60)))
x = res

y = Var.tjulian #days

a, b = np.polyfit(x, y, 1)

print("V Mag Distance: "+str(round(a/3.086E13/1000000,2))+" Mpc")
print('t\N{SUBSCRIPT ZERO} = ' + str(round(b,2)) + ' days')