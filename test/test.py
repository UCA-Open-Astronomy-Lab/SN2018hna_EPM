import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.900333875672855e-20, 3.8385248457305476e-20, 4.823441594035199e-20, 7.633504511963332e-20, 9.903145504848894e-20])

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