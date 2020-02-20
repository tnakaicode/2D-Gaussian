import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from optparse import OptionParser

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    nx, ny = 100, 100
    lx, ly = 100, 100
    sx, sy = 0.0, 0.0
    px = np.linspace(-1, 1, nx) * lx - sx
    py = np.linspace(-1, 1, ny) * ly - sy
    mesh = np.meshgrid(px, py)
