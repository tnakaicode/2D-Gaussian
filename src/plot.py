import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable

import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)


def plot_contour_sub(mesh, func, loc=[0, 0], txt="", title="name", dirname="../temp/contour", level=None):
    """
    plot 2d data
    """
    sx, sy = loc
    nx, ny = func.shape
    xs, ys = mesh[0][0, 0], mesh[1][0, 0]
    xe, ye = mesh[0][0, -1], mesh[1][-1, 0]
    dx, dy = mesh[0][0, 1] - mesh[0][0, 0], mesh[1][1, 0] - mesh[1][0, 0]
    mx, my = int((sy - ys) / dy), int((sx - xs) / dx)
    
    fig, axs = plt.subplots()
    divider = make_axes_locatable(axs)
    axs.set_aspect('equal')

    axs_x = divider.append_axes("bottom", 1.0, pad=0.5, sharex=axs)
    axs_x.plot(mesh[0][mx, :], func[mx, :])
    axs_x.set_title("y = {:.2f}".format(sy))
    axs_x.xaxis.grid(True, zorder=0)
    axs_x.yaxis.grid(True, zorder=0)

    axs_y = divider.append_axes("right", 1.0, pad=0.5, sharey=axs)
    axs_y.plot(func[:, my], mesh[1][:, my])
    axs_y.set_title("x = {:.2f}".format(sx))
    axs_y.xaxis.grid(True, zorder=0)
    axs_y.yaxis.grid(True, zorder=0)

    tx, ty = 1.1, 0.0
    plt.text(tx, ty, txt, transform=axs_x.transAxes)

    img = axs.contourf(*mesh, func, cmap="jet", levels=level)
    axs.set_title(title)
    axs.xaxis.grid(True, zorder=0)
    axs.yaxis.grid(True, zorder=0)
    plt.colorbar(img, ax=axs, shrink=0.9)
    plt.tight_layout()
    plt.savefig(dirname + ".png")
    plt.close()
