
'''Time in days from files supplied by the user'''
tdays = [12.1, 15.1, 20.1, 37.2, 46.1]#days since explosion in regular days
tjulian = [2458423.4, 2458426.4, 2458431.4, 2458447.5, 2458457.4]#days since explosion in julian days

'''Tempurature values using different methods'''
'''
BVtemp = []
for i in range(len(tdays)):
    BVtemp.append(BV.T[i])
'''
'''Velocities derived using a method chosen by the user'''
v = [6485, 5355, 4713, 3861, 3566]#velocity in km/s


'''Filter magnitudes from the files supplied by the user'''
Umag = [18.12, 18.36, 18.16, 17.43, 17.10]#magnatude of U filter
Bmag = [17.03, 17.07, 16.96, 16.27, 15.86]#magnatude of B filter
Vmag = [16.11, 16.01, 15.84, 15.22, 14.82]#Magnatude of V filter
Rmag = [15.72, 15.62, 15.44, 14.82, 14.53]#Magnatude of R filter
Imag = [15.58, 15.42, 15.16, 14.57, 14.27]#Magnatude of I filter

'''Constants for calculating synthetic magnitude, derived in (Hamuy, 2001)'''
Bconst = [-45.144, 7.159, -4.301, 2.639, -0.811, 0.098]#constants for the B magnitudes
Vconst = [-44.766, 6.793, -4.523, 2.695, -0.809, 0.096]#constants for the V magnitudes
Rconst = [-44.597, 6.628, -4.693, 2.770, -0.831, 0.099]#constants for the R magnitudes
Iconst = [-44.345, 6.347, -4.732, 2.739, -0.811, 0.096]#constants for the I magnitudes

z = 0.00241 #red shift for the supernova

'''Dilution Factor Constants'''
BVdilution = [0.7557, -0.8997, 0.5199]
BVIdilution = [0.7336, -0.6942, 0.3740]



'''
Unused Equations
    #synthMag[i] = -44.766+6.793*((10**4)/(temp[i]))-4.523*((10**4/temp[i])**2)+2.695*((10**4/temp[i])**3)-0.809*((10**4/temp[i])**4)+0.096*((10**4/temp[i])**5)
    #dilution_factor[i] = 0.5356+0.2116*((10**4)/(temp[i]))-0.0384*((10**4/temp[i])**2)



'''