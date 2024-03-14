import numpy as np
import scipy as sp
import sympy as sym
from scipy.fft import fft2
from scipy.fft import ifft2
from scipy.fft import fftfreq
from scipy.fft import fftshift
import imageio
import cv2

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import animation
from matplotlib.animation import PillowWriter
import pint

u = pint.UnitRegistry()

x = np.array([1,2])*u.mm
print(x)

D = 0.1 * u.mm 
lam = 660 * u.mm 

x = np.linspace(-2,2,1600) * u.mm 
xv, yv = np.meshgrid(x, x)

U0 = (np.abs(xv) < D/2) * (np.abs(yv) < 0.5*u.mm)
U0 = U0.astype(float)
print(U0)


plt.figure(figsize=(5,5))
plt.pcolormesh(xv, yv, U0)
plt.xlabel('X-Position [mm]')
plt.ylabel('Y-Position [mm]')
plt.show() 

fftfreq(len(x), np.diff(x)[0]) * 2 * np.pi

from signal import siginterrupt


A = fft2(U0)
kx = fftfreq(len(x), np.diff(x)[0]) * 2 *np.pi
kxv, kyv = np.meshgrid(kx,kx)

plt.figure(figsize=(5,5))
plt.pcolormesh(fftshift(kxv.magnitude), fftshift(kyv.magnitude), np.abs(fftshift(A)))
plt.xlabel('$k_x$ [mm$^{-1}$]')
plt.ylabel('$k_y$ [mm$^{-1}$]')
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.show()

def get_U(z, k):
    return ifft2(A*np.exp(1j*z * np.sqrt(k**2 - kxv**2 - kyv**2)))

k = 2*np.pi / (lam)
d = 3*u.cm 

U = get_U(d,k)

print(U)

plt.figure(figsize=(5,5))
plt.pcolormesh(xv, yv, np.abs(U), cmap='inferno')
plt.xlabel('$x$ [mm]')
plt.xlabel('$y$ [mm]')
plt.show()