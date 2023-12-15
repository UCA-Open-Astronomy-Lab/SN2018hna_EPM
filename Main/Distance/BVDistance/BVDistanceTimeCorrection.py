"""https://stackoverflow.com/questions/9990789/how-to-force-zero-interception-in-linear-regression/9994484#9994484"""
import math
import numpy as np
import matplotlib.pyplot as plt
import BVVariables as Var
import BVDistance

v = np.array(Var.v)
thetaB = np.array(BVDistance.thetaB)
thetaV = np.array(BVDistance.thetaV)
y = np.array(Var.tdays)

#Linear regression that forces a 0 y intercept 
x = thetaB/(v*24*60*60)
x = x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y,rcond=None)

print()
print("B mag time corrected BV temp distance: "+str(np.round(a/3.086E13/1000000,2))+" Mpc")

#Linear regression that forces a 0 y intercept 
x = thetaV/(v*24*60*60)
x = x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y,rcond=None)

print()
print("B mag time corrected BV temp distance: "+str(np.round(a/3.086E13/1000000,2))+" Mpc")

'''
plt.plot(x, y, 'bo')
plt.plot(x, a*x, 'r-')
plt.show()
'''