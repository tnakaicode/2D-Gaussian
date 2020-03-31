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


class PlotSignal(plot2d):

    def __init__(self, aspect='equal'):
        plot2d.__init__(self, aspect=aspect)

    def plot_signal_each(self, pt, sg, pngname=None):
        Ft = pt[1] - pt[0]

        self.new_fig(aspect="auto")
        self.axs.set_title("Signal")
        self.axs.plot(pt, sg, color='C0')
        self.axs.set_xlabel("Time")
        self.axs.set_ylabel("Amplitude")
        self.SavePng(self.tempname + "-Signal.png")

        self.new_fig(aspect="auto")
        self.axs.set_title("Magnitude Spectrum")
        self.axs.magnitude_spectrum(sg, Fs=Ft, color='C1')
        self.SavePng(self.tempname + "-Spec.png")

        self.new_fig(aspect="auto")
        self.axs.set_title("Log. Magnitude Spectrum")
        self.axs.magnitude_spectrum(sg, Fs=Ft, scale='dB', color='C1')
        self.SavePng(self.tempname + "-Specdb10.png")

        self.new_fig(aspect="auto")
        self.axs.set_title("Phase Spectrum ")
        self.axs.phase_spectrum(sg, Fs=Ft, color='C2')
        self.SavePng(self.tempname + "-SpecPhas.png")

        self.new_fig(aspect="auto")
        self.axs.set_title("Angle Spectrum")
        self.axs.angle_spectrum(sg, Fs=Ft, color='C2')
        self.SavePng(self.tempname + "-SpecAngl.png")

    def plot_signal(self, pt, sg, pngname=None):
        self.new_fig()
        ax1 = self.add_axs(3, 2, 1, aspect="auto")
        ax2 = self.add_axs(3, 2, 2, aspect="auto")
        ax3 = self.add_axs(3, 2, 3, aspect="auto")
        ax4 = self.add_axs(3, 2, 4, aspect="auto")
        ax5 = self.add_axs(3, 2, 5, aspect="auto")
        ax6 = self.add_axs(3, 2, 6, aspect="auto")
        Ft = pt[1] - pt[0]

        ax1.set_title("Signal")
        ax1.plot(pt, sg, color='C0')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Amplitude")

        ax2.remove()

        # plot different spectrum types:
        ax3.set_title("Magnitude Spectrum")
        ax3.magnitude_spectrum(sg, Fs=Ft, color='C1')

        ax4.set_title("Log. Magnitude Spectrum")
        ax4.magnitude_spectrum(sg, Fs=Ft, scale='dB', color='C1')

        ax5.set_title("Phase Spectrum ")
        ax5.phase_spectrum(sg, Fs=Ft, color='C2')

        ax6.set_title("Angle Spectrum")
        ax6.angle_spectrum(sg, Fs=Ft, color='C2')

        self.fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
        self.SavePng_Serial()


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
