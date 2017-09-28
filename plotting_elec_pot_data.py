import matplotlib.pyplot as plt
import numpy as np
import DWCode as dw
from scipy.optimize import curve_fit

# Loading the data
# x => Electric Potential
# y => Burial Coefficient
# z => B-factor
x, y, z = dw.open_file("buried_water_data_v1.dat", delim=' ')

# Creating an array for the
# Potentials with B-factor < 25
# and filling it
b_fac_plotvec = []
for i in range(len(y)):
    if z[i] <= 25:
        b_fac_plotvec.append(y[i])

# Gaussian fitting function
def gaus(x, a, x0, sigma):
    return a*np.exp(-(((x-x0)**2)/(2*sigma**2)))

# Creating the two figures
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

# Figure 1 -- All data histogram
n1, bins1, patches1 = ax1.hist(y, bins=5000, color='w') # Histogram: n1=count, bins1=value
fit_bins_1 = [(0.5*(bins1[i+1]+bins1[i])) for i in range(len(bins1)-1)] # Bins for fitting
popt1, pcov1 = curve_fit(gaus, fit_bins_1, n1) # Fitting to Guassian
stderr1 = popt1[2]/(np.sqrt(len(fit_bins_1))) # Calculating Standard Error
ax1.plot(fit_bins_1, gaus(fit_bins_1, *popt1), 'r--') # Plotting gaussian
ax1.set_xlabel("Electric Potential [kcal/mol]")
ax1.set_ylabel("Count [#]")
ax1.set_xlim([-40,40])
ax1.set_title("Buried Waters Potential Energy Histogram (all B factors)")
ax1.legend()
print("All data fit params:")
print("Mean: {:.4f}, Stand. Dev.: {:.4f}, Standard Error = {:.4f} \n".format(popt1[1],popt1[2], stderr1))

# Figure 2 -- B-factor < 25 histogram
n2, bins2, patches2 = ax2.hist(b_fac_plotvec, bins=5000, color='w') # Histogram: n2=count, bins2=value
fit_bins_2 = [(0.5*(bins2[i+1]+bins2[i])) for i in range(len(bins2)-1)] # Bins for fitting
popt2, pcov2 = curve_fit(gaus, fit_bins_2, n2) # Fitting to Guassian
stderr2 = popt2[2]/(np.sqrt(len(fit_bins_2))) # Calculating Standard Error
ax2.plot(fit_bins_2, gaus(fit_bins_2, *popt2), 'r--') # Plotting gaussian
ax2.set_xlabel("Electric Potential [kcal/mol]")
ax2.set_ylabel("Count [#]")
ax2.set_xlim([-40,40])
ax2.set_title("Buried Waters Potential Energy Histogram (B factor < 25)")
print("B factor < 25 fit params:")
print("Mean: {:.4f}, Stand. Dev.: {:.4f}, Standard Error: {:.4f}".format(popt2[1],popt2[2],stderr2))

fig1.savefig("Elec_Pot_Hist_total.png", format='png', transparent=True)
fig2.savefig("Elec_Pot_Hist_b_fac_25.png", format='png', transparent=True)
