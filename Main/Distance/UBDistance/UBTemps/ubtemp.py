import math
import numpy as np
import matplotlib.pyplot as plt
import UBTemps.kandcforub as KC

'''
10000K/T = K(B-V)+C 

This is the equation from MatthewsSandage1963 to calculate tempurature based on B and V filters and prior data 
collected and displayed in the Appendix of the paper above.
 '''

T = [0,0,0,0,0]
K = KC.K #1.58#slope calculated from the 
U = [18.12, 18.36, 18.16, 17.43, 17.10]#Ultraviolet light mag
A_U = 0 #correction for the U mag
B = [17.03, 17.07, 16.96, 16.27, 15.86]#Blue light mag
A_B = 0.048 #correction for the B magnitude
C = KC.C #0.48#constant based on color filters

for i in range(len(T)):
    T[i] = round(10000/( K * ((U[i] - A_U) - (B[i] - A_B)) + C ),2)