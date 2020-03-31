import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from scipy import signal
from optparse import OptionParser
sys.path.append(os.path.join('../'))

from src.base import plot2d

if __name__ == "__main__":
    argvs = sys.argv
    parser = OptionParser()
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    obj = plot2d(aspect="auto")
    t = np.linspace(-1, 1, 2 * 100, endpoint=False)
    i, q, e = signal.gausspulse(t, fc=5, retquad=True, retenv=True)
    obj.axs.plot(t, i, '--', label="fi")
    obj.axs.plot(t, q, '--', label="fq")
    obj.axs.plot(t, e, '--', label="fe")
    obj.axs.legend()
    obj.axs.set_title("GaussPluse")
    obj.SavePng_Serial()

    obj.new_fig(aspect="auto")
    t = np.linspace(0, 1, 500)
    obj.axs.plot(t, signal.sawtooth(2 * np.pi * 5 * t, 1), label="w=1")
    obj.axs.plot(t, signal.sawtooth(2 * np.pi * 2 * t, 2), label="w=2")
    obj.axs.legend()
    obj.axs.set_title("SawTooth")
    obj.SavePng_Serial()

    obj.new_fig(aspect="auto")
    t = np.linspace(0, 1, 500, endpoint=False)
    obj.axs.plot(t, signal.square(2 * np.pi * 5 * t))
    obj.axs.set_ylim(-2, 2)
    obj.axs.set_title("Square")
    obj.SavePng_Serial()

    obj.new_fig(aspect="auto")
    ax1 = obj.add_axs(2, 1, 1)
    ax2 = obj.add_axs(2, 1, 2)
    sig = np.sin(2 * np.pi * t)
    pwm = signal.square(2 * np.pi * 30 * t, duty=(sig + 1) / 2)
    ax1.plot(t, sig)
    ax2.plot(t, pwm)
    obj.axs.set_title("PWM")
    obj.SavePng_Serial()
