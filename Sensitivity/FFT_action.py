from DPendulum import Pendulum
import matplotlib.pyplot as plt
import numpy as np
from scipy import pi

# FFT plot for small angle osillations
y0 = [pi/12, 0, pi/12, 0]
pendulum = Pendulum(theta1=y0[0], z1=y0[1], theta2=y0[2], z2=y0[3], tmax=200, dt=0.05, y0=y0)
pendulum.fft_plot()

# FFT plot for a periodic case
y0 = [pi/12, 0, np.sqrt(2)*pi/12, 0]
pendulum = Pendulum(theta1=y0[0], z1=y0[1], theta2=y0[2], z2=y0[3], tmax=100, dt=0.05, y0=y0)
pendulum.fft_plot()

# Reproduce theta plots for a periodic case
t = pendulum.t
theta1, z1, theta2, z2 = pendulum.sol()
omega1_pval, omega1_pind, omega2_pval, omega2_pind = pendulum.find_peaks()

plt.figure(figsize = (15, 6))
plt.subplot(121)
plt.plot(t, theta1)
plt.plot(t, np.cos(omega1_pval[0]*t)/4, alpha=0.6)
plt.subplot(122)
plt.plot(t, theta2)
plt.plot(t, np.cos(omega2_pval[0]*t)/3, alpha=0.6)
plt.show()
