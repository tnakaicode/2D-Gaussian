import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from matplotlib.animation import FuncAnimation
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d


class TriangleWaveAni (plot2d):

    def __init__(self, aspect='auto'):
        self.time_leng = 2.5
        self.time_smpl = 100
        self.time_fram = np.linspace(0, 1, self.time_smpl) * self.time_leng

        self.freq = 2.0  # Hz
        self.perd = 1 / self.freq
        self.ampl = 1.0
        self.pos = 0
        self.val = 0

        plot2d.__init__(self, aspect=aspect)
        self.axs.set_xlim(0, self.time_leng)
        self.axs.set_ylim(0, self.ampl * 1.25)
        self.tr_line, = self.axs.plot([], [])
        self.sq_line, = self.axs.plot([], [])

        print(self.ampl * 2 * self.freq / self.time_smpl)
        self.ani = FuncAnimation(
            self.fig, self.animate,
            frames=self.time_fram,
            init_func=self.init, interval=1, blit=False
        )

    def animate(self, t):
        tr_x = self.tr_line.get_xdata()
        tr_y = self.tr_line.get_ydata()
        tr_x.append(t)
        tr_y.append(self.val)
        self.tr_line.set_data(tr_x, tr_y)

        txt = "\r{:.2f}\t".format(t)
        txt += "{:.2f}\t".format(tr_y[-1])
        sys.stdout.write(txt)
        sys.stdout.flush()
        if self.pos > 1.0:
            self.pos = 0
            self.val = 0
        elif self.pos > 0.5:
            self.pos -= 1 / self.time_smpl
            self.val += 1 / self.time_smpl
        else:
            self.pos += 1 / self.time_smpl
            self.val += 1 / self.time_smpl
        return

    def init(self):
        self.tr_line.set_data([0], [1])
        self.sq_line.set_data([0], [1])
        return


if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    obj = TriangleWaveAni()
    obj.ani.save(obj.tmpdir + "TriangleWave.gif", writer='pillow')
    plt.close()
    # plt.show()
