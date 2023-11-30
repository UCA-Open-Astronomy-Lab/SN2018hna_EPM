import math
import numpy as np
import matplotlib.pyplot as plt

#importinng files for calcualating tempuratures
import EPMvariables as Var



synthMagNew = [0,0,0,0,0]
dilution_factorold = [0,0,0,0,0]
dilution_factornew = [0,0,0,0,0]

#Bconst = [-45.144, 7.159, -4.301, 2.639, -0.811, 0.098]#constants for the B magnitudes

    #dilution_factor[i] = 0.5356+0.2116*((10**4)/(temp[i]))-0.0384*((10**4/temp[i])**2)

dil = [0.5356, 0.2116, -0.0384]


for i in range(5):
    for x in range(3):
        dilution_factornew[i] += dil[x]*(((10**4)/(Var.BVtemp[i]))**(x))
        

for i in range(5):
    dilution_factorold[i] = 0.5356+0.2116*((10**4)/(Var.BVtemp[i]))-0.0384*((10**4/Var.BVtemp[i])**2)

print("Old",dilution_factorold)
print("New", dilution_factornew)