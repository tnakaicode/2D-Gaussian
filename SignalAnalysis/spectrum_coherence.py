"""
=====================================
Plotting the coherence of two signals
=====================================

An example showing how to plot the coherence of two signals.
"""
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import os

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d

# Fixing random state for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

obj = plot2d()
ax1 = obj.add_axs(2, 1, 1, aspect="auto")
ax2 = obj.add_axs(2, 1, 2, aspect="auto")

ax1.plot(t, s1, t, s2)
ax1.set_xlim(0, 2)
ax1.set_xlabel('time')
ax1.set_ylabel('s1 and s2')

#cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
ax2.cohere(s1, s2, 256, 1. / dt)
ax2.set_ylabel('coherence')

#obj.fig.tight_layout()
obj.SavePng_Serial()
