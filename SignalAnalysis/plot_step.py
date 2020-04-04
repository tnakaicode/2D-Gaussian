import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import time
import os
import glob
import shutil
import datetime
from optparse import OptionParser

sys.path.append(os.path.join("../"))
from src.base import plot2d, create_tempdir


if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)
    
    x = np.linspace(-1, 1, 10) * np.pi
    y = np.sin(x)

    obj = plot2d()

    obj.axs.step(x, y + 2, label='pre (default)')
    obj.axs.plot(x, y + 2, 'C0o', alpha=0.5)

    obj.axs.step(x, y + 1, where='mid', label='mid')
    obj.axs.plot(x, y + 1, 'C1o', alpha=0.5)

    obj.axs.step(x, y, where='post', label='post')
    obj.axs.plot(x, y, 'C2o', alpha=0.5)

    obj.axs.legend(title='Parameter where:')
    obj.SavePng_Serial("../tmp/plot_step.png")
    obj.SavePng_Serial()
