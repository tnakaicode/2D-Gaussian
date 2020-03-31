# Signal Generation
# matplotlib inline
# https://stackoverflow.com/questions/14058340/adding-noise-to-a-signal-in-python

import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d


class PlotSignal(plot2d):

    def __init__(self, aspect='equal'):
        plot2d.__init__(self, aspect=aspect)

    def plot_signal(self, pt, sg, pngname=None):
        self.new_fig()
        ax1 = self.add_axs(2, 1, 1, aspect="auto")
        ax2 = self.add_axs(2, 1, 2, aspect="auto")

        # Plot signal wave [V]
        ax1.plot(pt, sg)
        ax1.set_title('Signal with noise')
        ax1.set_ylabel('Voltage (V)')

        # Plot in Power [dB]
        ax2.plot(pt, 10 * np.log10(sg**2))
        ax2.set_ylabel('Power (dB)')
        ax2.set_xlabel('Time (s)')
        self.SavePng_Serial(pngname)


if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    obj = PlotSignal()

    t = np.linspace(1, 100, 1000)
    x_volts = 10 * np.sin(t / (2 * np.pi))
    x_watts = x_volts ** 2
    x_db = 10 * np.log10(x_watts)

    obj.plot_signal(t, x_watts, obj.tempname + "_smooth.png")

    # Adding noise using target SNR
    # Set a target SNR
    target_snr_db = 20
    # Calculate signal power and convert to dB
    sig_avg_watts = np.mean(x_watts)
    sig_avg_db = 10 * np.log10(sig_avg_watts)
    # Calculate noise according to [2] then convert to watts
    noise_avg_db = sig_avg_db - target_snr_db
    noise_avg_watts = 10 ** (noise_avg_db / 10)
    # Generate an sample of white noise
    mean_noise = 0
    noise_volts = np.random.normal(
        mean_noise, np.sqrt(noise_avg_watts), len(x_watts))
    # Noise up the original signal
    y_volts = x_volts + noise_volts

    obj.plot_signal(t, y_volts, obj.tempname + "_noisy.png")

    # Adding noise using a target noise power
    # Set a target channel noise power to something very noisy
    target_noise_db = 10
    # Convert to linear Watt units
    target_noise_watts = 10 ** (target_noise_db / 10)

    # Generate noise samples
    mean_noise = 0
    noise_volts = np.random.normal(
        mean_noise, np.sqrt(target_noise_watts), len(x_watts))

    # Noise up the original signal (again) and plot
    y_volts = x_volts + noise_volts

    obj.plot_signal(t, y_volts, obj.tempname + "_noisy.png")
