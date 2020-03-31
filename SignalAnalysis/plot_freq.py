import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    px = np.linspace(0, 500, 1000) * np.pi
    py = np.sin(px) * np.cos(px) * np.tan(px)

    obj = plot2d()
    obj.axs.set_aspect("auto")
    obj.axs.plot(px, py)
    obj.SavePng()
    obj.SavePng_Serial()
