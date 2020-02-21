import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from optparse import OptionParser
sys.path.append(os.path.join('../'))

from src.profile import integrate_simps, gaussian_func
from src.plot import plot_contour_sub

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
    func = gaussian_func(mesh, sxy=[25, -50], wxy=[20, 15], rot=30)

    plot_contour_sub(mesh, func, loc=[25, -50])
