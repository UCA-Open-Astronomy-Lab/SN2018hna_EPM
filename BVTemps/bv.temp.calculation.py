import math
import numpy as np
import matplotlib.pyplot as plt

#KC = __import__(kandcforbv.py)

#import_module(kandcforbv.py)

#import "BVTemps/kandcforbv.py" as KC


#10000K/T = K(B-V)+C

T = [0,0,0,0,0]
K = KC.K#1.58#slope calculated from the 
B = [17.03, 17.07, 16.96, 16.27, 15.86]#Blue light mag
A_B = 0.048 #correction for the B magnitude
V = [16.11, 16.01, 15.84, 15.22, 14.82]#Visiblle light mag
A_V = 0.036 #correction for the V magnitude
C = KC.C#0.48#constant based on color filters

for i in range(len(T)):
    T[i] = round(10000/( K * ((B[i] - A_B) - (V[i] - A_V)) + C ),2)
print(T)

#BVTemps/kandcforbv.py