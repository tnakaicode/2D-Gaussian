"""
========================
Spectrum Representations
========================

The plots show different spectrum representations of a sine signal with
additive noise. A (frequency) spectrum of a discrete-time signal is calculated
by utilizing the fast Fourier transform (FFT).
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
    np.random.seed(0)

    dt = 0.01  # sampling interval
    Fs = 1 / dt  # sampling frequency
    t = np.arange(0, 10, dt)

    # generate noise:
    nse = np.random.randn(len(t))
    r = np.exp(-t / 0.05)
    cnse = np.convolve(nse, r) * dt
    cnse = cnse[:len(t)]

    s = 0.1 * np.sin(4 * np.pi * t) + cnse  # the signal

    obj = PlotSignal()
    obj.plot_signal_each(t, s)
