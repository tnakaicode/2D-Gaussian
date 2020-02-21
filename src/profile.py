import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
import glob
import shutil
import datetime
import scipy.constants as cnt
from linecache import getline, clearcache
from scipy.integrate import simps


def gaussian_func(mesh, sxy=[0, 0], wxy=[10, 10], rot=0.0):
    x, y = mesh[0] - sxy[0], mesh[1] - sxy[1]
    px = x * np.cos(rot) - y * np.sin(rot)
    py = y * np.cos(rot) + x * np.sin(rot)
    fx = np.exp(-0.5 * (px / wxy[0])**2)
    fy = np.exp(-0.5 * (py / wxy[1])**2)
    return fx * fy


def integrate_simps(mesh, func):
    nx, ny = func.shape
    px, py = mesh[0][int(nx / 2), :], mesh[1][:, int(ny / 2)]
    val = simps(simps(func, px), py)
    return val


def normalize_integrate(mesh, func):
    return func / integrate_simps(mesh, func)


def normalize_max(mesh, func):
    return func / func.max()


def moment(mesh, func, index):
    ix, iy = index[0], index[1]
    g_func = normalize_integrate(mesh, func)
    fxy = g_func * mesh[0]**ix * mesh[1]**iy
    val = integrate_simps(mesh, fxy)
    return val


def moment_seq(mesh, func, num):
    seq = np.empty([num, num])
    for ix in range(num):
        for iy in range(num):
            seq[ix, iy] = moment(mesh, func, [ix, iy])
    return seq


def get_cov(mesh, func, dxy):
    g_mesh = [mesh[0] - dxy[0], mesh[1] - dxy[1]]
    Mxx = moment(g_mesh, func, (2, 0))
    Myy = moment(g_mesh, func, (0, 2))
    Mxy = moment(g_mesh, func, (1, 1))
    mat = np.array([
        [Mxx, Mxy],
        [Mxy, Myy],
    ])
    return mat


def get_centroid(mesh, func):
    dx = moment(mesh, func, (1, 0))
    dy = moment(mesh, func, (0, 1))
    return dx, dy


def get_weight(mesh, func, dxy):
    g_mesh = np.array((mesh[0] - dxy[0], mesh[1] - dxy[1]))
    lx = moment(g_mesh, func, (2, 0))
    ly = moment(g_mesh, func, (0, 2))
    return np.sqrt(lx) * np.sqrt(2), np.sqrt(ly) * np.sqrt(2)


def get_covariance(mesh, func):
    dxy = get_centroid(mesh, func)
    g_mesh = [mesh[0] - dxy[0], mesh[1] - dxy[1]]
    Mxx = moment(g_mesh, func, (2, 0))
    Myy = moment(g_mesh, func, (0, 2))
    Mxy = moment(g_mesh, func, (1, 1))
    return np.array([[Mxx, Mxy], [Mxy, Myy]])


def get_wxy(mesh, func):
    sxy = get_centroid(mesh, func)
    cov = get_cov(mesh, func, sxy)
    wxy, mat = np.linalg.eig(cov)
    wxy = np.sqrt(wxy)
    rot = -np.arcsin(mat[0, 1])
    #print (wxy, np.rad2deg(-np.arcsin(mat[0, 1])), np.rad2deg(np.arccos(mat[0, 0])))
    """if wxy[0] > wxy[1]:
        rot = np.pi/2 - (-np.arcsin(mat[0, 1]))
        wxy = wxy[1], wxy[0]
    else:
        rot = -np.arcsin(mat[0, 1]) 
        wxy = wxy[0], wxy[1]"""
    g_func = gaussian_func(mesh, sxy, wxy, rot)
    x, y = mesh[0] - sxy[0], mesh[1] - sxy[1]
    px = x * np.cos(rot) - y * np.sin(rot)
    py = y * np.cos(rot) + x * np.sin(rot)
    g_mesh = [px, py]
    for i in range(20):
        wx = np.sqrt(2) * np.sqrt(integrate_simps(g_mesh,
                                                  g_mesh[0]**2 * g_func * func) / integrate_simps(g_mesh, g_func * func))
        wy = np.sqrt(2) * np.sqrt(integrate_simps(g_mesh,
                                                  g_mesh[1]**2 * g_func * func) / integrate_simps(g_mesh, g_func * func))
        wxy = [wx, wy]
        #print (wxy, gcf_calc(mesh, func, g_func))
        g_func = gaussian_func(mesh, sxy, wxy, rot)
    #print (wxy, np.rad2deg(rot))
    return wxy, rot
