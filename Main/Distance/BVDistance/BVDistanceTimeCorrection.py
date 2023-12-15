
import numpy as np
import matplotlib.pyplot as plt
import BVVariables as Var
import BVDistance

v = np.array(Var.v)
print(v)
thetaB = np.array(BVDistance.thetaB)

x = thetaB/v
print(x)

y = np.array([12.1, 15.1, 20.1, 37.2, 46.1])


# Our model is y = a * x, so things are quite simple, in this case...
# x needs to be a column vector instead of a 1D vector for this, however.
x = x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x, y,rcond=None)

plt.plot(x, y, 'bo')

plt.plot(x, a*x, 'r-')
print("Slope: ",a/3.086E13/1000000)


"""https://stackoverflow.com/questions/9990789/how-to-force-zero-interception-in-linear-regression/9994484#9994484"""
#plt.show()