"""
========
CSD Demo
========

Compute the cross spectral density of two signals
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import plot2d
from src.SignalAnalysis import PlotSignal

if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)

    # white noise
    nse1 = np.random.randn(len(t))
    nse2 = np.random.randn(len(t))
    r = np.exp(-t / 0.05)

    # colored noise
    cnse1 = np.convolve(nse1, r, mode='same') * dt
    cnse2 = np.convolve(nse2, r, mode='same') * dt

    # two signals with a coherent part and a random part
    s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
    s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

    obj = PlotSignal(aspect="auto")
    obj.axs.plot(t, s1)
    obj.axs.plot(t, s2)
    obj.axs.set_xlabel('time')
    obj.axs.set_ylabel('s1 and s2')
    obj.SavePng()

    obj.new_fig(aspect="auto")
    obj.axs.set_xlim(0, 5.0)
    obj.axs.plot(t, s1)
    obj.axs.plot(t, s2)
    obj.axs.set_xlabel('time')
    obj.axs.set_ylabel('s1 and s2')
    obj.SavePng(obj.tempname + "-Sig.png")

    obj.new_fig(aspect="auto")
    obj.axs.csd(s1, s2, 256, 1. / dt)
    obj.axs.set_ylabel('CSD (db)')
    obj.SavePng(obj.tempname + "-CSD.png")
