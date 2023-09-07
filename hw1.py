import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
import sys
import os
import io
import math
import scipy
from scipy.integrate import quad
plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "dejavuserif"

#integral 0 to z = dz / (Omega (1+z)^3 + (1-Omega)(1+z)^3/2)^1/2

def integrand(z, Omega):
	return 1/np.sqrt(Omega *(1+z)**3 + (1-Omega)*(1+z)**(3./2.))

Omegas = [0., 0.3, 0.7, 1.0]
z = np.linspace(0,1, 100)
colors =['darkslateblue','seagreen', 'orange', 'tomato']
for k in range(len(Omegas)):
	integral_values = np.zeros(len(z))
	Omega = Omegas[k]
	for i in range(len(z)):
		I = quad(integrand, 0, z[i], args=(Omega))
		integral_values[i] = I[0]
	plt.plot(z, integral_values, label=f'$\Omega$={Omegas[k]}', alpha=0.5, color=colors[k])

plt.plot(z, 4*(1+z)**(1/4)-4, label='Analytical $\Omega=0$', color='slateblue', ls='dashed')
plt.plot(z, 2-2*(1+z)**(-1/2), label='Analytical $\Omega=1$', color='red', ls='dashed')
plt.legend()
plt.ylabel('Integral', fontsize=12)
plt.xlabel('$z$', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.yscale('log')
plt.savefig('plot_1.pdf')
plt.show()

