import numpy as np

from src.base import plot2d
from src.profile import integrate_simps, get_covariance, gaussian_func


class GaussianCalc (plot2d):

    def __init__(self, aspect='equal'):
        plot2d.__init__(self, aspect=aspect)
        px = np.linspace(-1, 1, 100) * 200
        py = np.linspace(-1, 1, 200) * 200
        self.mesh = np.meshgrid(px, py)
        self.func = gaussian_func(self.mesh)

    def SetGaussian(self, sxy=[0, 0], wxy=[50, 50], rot=0.0):
        self.func = gaussian_func(self.mesh, sxy=sxy, wxy=wxy, rot=rot)

    def PlotGauss(self):
        self.contourf_sub(self.mesh, self.func, pngname=self.tempname + ".png")


if __name__ == '__main__':
    obj = GaussianCalc()
    obj.SetGaussian(wxy=[50.0, 25.0], rot=30.0)
    obj.PlotGauss()

    rho = 0.5
    sxy = [10.0, 20.0]
    wxy = [10.0, 20.0]

    mu = np.matrix(sxy)
    sg = np.matrix([
        [wxy[0]**2, rho * wxy[0] * wxy[1]],
        [rho * wxy[0] * wxy[1], wxy[1]**2]
    ])

    #
    # sg
    # Return the standard deviation of the array elements along the given axis.
    # Returns the variance of the matrix elements, along the given axis.
    # Return the product of the array elements over the given axis.
    #
    print(sg)
    print(sg.std())
    print(np.linalg.inv(sg))
    print(np.linalg.det(sg))

    xy = np.array(obj.mesh)
    sg.dot(mu.T)

    for i in range(2):
        print(xy[i])
        print(sg[i])
        print(mu[:, i])
