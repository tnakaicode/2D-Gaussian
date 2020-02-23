import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time
from optparse import OptionParser
from scipy.stats import multivariate_normal
sys.path.append(os.path.join('../'))

from src.profile import integrate_simps, gaussian_func, get_covariance, get_wxy
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
    func = gaussian_func(mesh, sxy=[25, -50], wxy=[15, 20], rot=15.0)

    cov = get_covariance(mesh, func)
    wxy, mat = np.linalg.eig(cov)
    wxy = np.sqrt(wxy)
    rot = -np.arcsin(mat[0, 1])
    print(wxy, rot, np.rad2deg(rot))
    print(get_wxy(mesh, func))
    print(cov)
    print(mat)
    print(np.rad2deg(-np.arcsin(mat[0, 1])), np.rad2deg(np.arccos(mat[0, 0])))

    """
    Multivariate normal probability density function.
    Parameters
    ----------
    x : array_like
        Quantiles, with the last axis of `x` denoting the components.
    %(_mvn_doc_default_callparams)s
    Returns
    -------
    pdf : ndarray or scalar
        Probability density function evaluated at `x`
    Notes
    -----
    %(_mvn_doc_callparams_note)s
    """

    fxy1 = multivariate_normal.pdf(np.stack(mesh, -1), mean=[25, -50], cov=cov)

    plot_contour_sub(mesh, func, loc=[25, -50])
    plot_contour_sub(mesh, fxy1, loc=[25, -50],
                     dirname="../temp/contourf_fxy1")
