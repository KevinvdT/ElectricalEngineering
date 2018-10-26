# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:33:34 2018
@author: Kevin van der Toorn
"""

import numpy as np
import matplotlib.pyplot as plt

# Process and device parameters
W = 15e-6
L = 1e-6 # channel length
mu_n = 1 #
C_ox = 1 # [farad / meter^2]

k_n = mu_n * C_ox # process transconductance parameter
k = (W / L) * k_n # gain factor of device (different per transistor in a chip)

V_ds = np.linspace(0, 2.5, 2000) # DC voltage sweep for drain potential
V_t = 0.45 # threshold voltage for the drain

# Function V_ds -> I_d
def calc_I_d(V_ds):
    if V_ds < V_gs - V_t:
        return mu_n * C_ox * (W / L) * ((V_gs - V_t) * V_ds - 0.5 * V_ds**2)
    else:
        return 0.5 * k * (V_gs - V_t)**2
calc_I_d = np.vectorize(calc_I_d)

# Generate I_d graphs for multiple values of V_gs (multiple gate potentials)
for V_gs in [1, 1.5, 2, 2.5]:
    I_d = calc_I_d(V_ds)
    plt.plot(V_ds, I_d, label='V_gs = ' + str(V_gs) + ' V')

plt.title('1st Order MOSFET Model')
plt.ylabel('I_d [A]')
plt.xlabel('V_ds [V]')

plt.grid()
plt.show()