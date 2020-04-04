import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d


def triang(x, phase=-10, length=30, amplitude=10):
    alpha = (amplitude) / (length / 2)
    return -amplitude / 2 + amplitude * ((x - phase) % length == length / 2) \
        + alpha * ((x - phase) % (length / 2)) * ((x - phase) % length <= length / 2) \
        + (amplitude - alpha * ((x - phase) % (length / 2))) * \
        ((x - phase) % length > length / 2)


if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    phase = -10
    length = 30  # should be positive
    amplitude = 10
    px = np.arange(0, 100, 0.1)

    obj = plot2d(aspect="auto")
    for phs in [-10, -20]:
        tr1 = triang(px, phs, length, amplitude)
        obj.axs.plot(px, tr1, label="phas={:.1f}".format(phs))
    obj.axs.legend()
    obj.SavePng()
