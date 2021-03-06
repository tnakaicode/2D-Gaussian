import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

from src.base import plot2d
from src.profile import integrate_simps, gaussian_func
from src.profile import get_centroid, get_covariance


def gaussian(x, cov=0.1, off=0.25):
    return np.exp(-0.5 * x**2 / cov) * np.random.normal(0.0, cov, x.shape) + off


def gaussian_mat(mesh, sxy=[0, 0], mat=np.zeros([2, 2])):
    x, y = mesh[0] - sxy[0], mesh[1] - sxy[1]
    inv = np.linalg.inv(mat)
    fxx = np.exp(-0.5 * (x**2 * inv[0, 0]))
    fyy = np.exp(-0.5 * (y**2 * inv[1, 1]))
    fxy = np.exp(-0.5 * (x * y * (inv[0, 1] + inv[1, 0])))
    return fxx * fyy * fxy


class GaussianCalc (plot2d):

    def __init__(self, aspect='equal'):
        plot2d.__init__(self, aspect=aspect)
        px = np.linspace(-1, 1, 100) * 200 - 50
        py = np.linspace(-1, 1, 200) * 250 + 100
        self.mesh = np.meshgrid(py, px)
        self.func = gaussian_func(self.mesh)
        #self.nois = np.random.normal(0.0, 0.05, self.func.shape)
        self.snr = 0.05
        self.nois = gaussian(self.func)

    def SetGaussian(self, sxy=[0, 0], wxy=[50, 50], rot=0.0):
        self.func = gaussian_func(self.mesh, sxy=sxy, wxy=wxy, rot=rot)
        self.nois = gaussian(self.func, cov=self.snr)
        self.func += self.nois

    def SetGaussianMat(self, sxy=[0, 0], wxy=[50, 50], rot=0.0):
        #rho = np.cos(np.deg2rad(rot)) / (wxy[1] / wxy[0])
        rho = 0.0 / (wxy[1] / wxy[0])
        mat = np.matrix([
            [wxy[0]**2, rho * wxy[0] * wxy[1]],
            [rho * wxy[0] * wxy[1], wxy[1]**2]
        ])
        print(mat)
        self.func = gaussian_mat(self.mesh, sxy=sxy, mat=mat)
        self.nois = gaussian(self.func, cov=self.snr)
        self.func += self.nois

    def PlotGauss(self):
        self.create_tempdir(-1)
        self.contourf_sub(self.mesh, self.func, pngname=self.tempname + ".png")

        dat = []
        sxy = get_centroid(self.mesh, self.func)
        cov = get_covariance(self.mesh, self.func)
        wxy, mat = np.linalg.eig(cov)
        wxy = np.sqrt(wxy)
        rot = -np.arcsin(mat[0, 1])
        g_func = gaussian_func(self.mesh, sxy, wxy, rot)
        gcf = integrate_simps(self.mesh, g_func * self.func)
        dat.append(np.array([*wxy, gcf]))

        x, y = self.mesh[0] - sxy[0], self.mesh[1] - sxy[1]
        px = x * np.cos(rot) - y * np.sin(rot)
        py = y * np.cos(rot) + x * np.sin(rot)
        g_mesh = [px, py]
        for i in range(20):
            wx = np.sqrt(2) * np.sqrt(
                integrate_simps(g_mesh, g_mesh[0]**2 * g_func * self.func) /
                integrate_simps(g_mesh, g_func * self.func)
            )
            wy = np.sqrt(2) * np.sqrt(
                integrate_simps(g_mesh, g_mesh[1]**2 * g_func * self.func) /
                integrate_simps(g_mesh, g_func * self.func)
            )
            wxy = [wx, wy]
            g_func = gaussian_func(self.mesh, sxy, wxy, rot)
            self.contourf_sub(self.mesh, g_func)
            plt.close()
            gcf = integrate_simps(self.mesh, g_func * self.func)
            dat.append(np.array([wx, wy, gcf]))
        dat = np.array(dat)
        print(dat.shape)

        self.new_2Dfig(aspect="auto")
        self.axs.plot(dat[:, 0])
        self.axs.plot(dat[:, 1])
        self.SavePng(obj.tempname + "-wxy.png")

        self.new_2Dfig(aspect="auto")
        self.axs.plot(dat[:, 2])
        self.SavePng(obj.tempname + "-gcf.png")

    def PlotGaussMat(self):
        self.create_tempdir(-1)
        self.contourf_sub(self.mesh, self.func, pngname=self.tempname + ".png")

        dat = []
        sxy = get_centroid(self.mesh, self.func)
        cov = get_covariance(self.mesh, self.func)
        g_func = gaussian_mat(self.mesh, sxy, cov)
        gcf = integrate_simps(self.mesh, g_func * self.func)
        wxy = [np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1])]
        dat.append(np.array([*wxy, gcf]))

        x, y = self.mesh[0] - sxy[0], self.mesh[1] - sxy[1]
        g_mesh = [x, y]
        for i in range(20):
            g_func = gaussian_mat(self.mesh, sxy, cov)
            self.contourf_sub(self.mesh, g_func)
            plt.close()
            gcf = integrate_simps(self.mesh, g_func * self.func)
            wxy = [np.sqrt(cov[0, 0]), np.sqrt(cov[1, 1])]
            dat.append(np.array([*wxy, gcf]))
        dat = np.array(dat)
        print(dat.shape)

        self.new_2Dfig(aspect="auto")
        self.axs.plot(dat[:, 0])
        self.axs.plot(dat[:, 1])
        self.SavePng(obj.tempname + "-wxy.png")

        self.new_2Dfig(aspect="auto")
        self.axs.plot(dat[:, 2])
        self.SavePng(obj.tempname + "-gcf.png")


if __name__ == '__main__':
    obj = GaussianCalc()
    obj.SetGaussian(wxy=[50.0, 25.0], rot=0.0)
    print(get_covariance(obj.mesh, obj.func))
    obj.SetGaussianMat(wxy=[50.0, 25.0], rot=0.0)
    print(get_covariance(obj.mesh, obj.func))
    obj.PlotGauss()
    obj.PlotGaussMat()

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
