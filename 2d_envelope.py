# https://stackoverflow.com/questions/33069295/envelope-of-signal-how-to-generate-nice-smooth-2d-lines-animation

from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import obspy.signal


def init():
    im.set_data([], [])
    im2.set_data([], [])
    im3.set_data([], [])
    return im, im2,


def filter_sinc(x=None, n=None):
    print(n)
    f = 1 / n
    nf = 2 * np.fix(2 / f)
    nf0 = int(nf/2)
    nf1 = int(nf)-nf0
    o = (np.arange(1, nf + 1)) - nf / 2
    filt = 0 * o + 2 * f
    o0 = o[:nf0]
    o1 = o[nf1:]
    temp = np.sin([2 * np.pi * f * np.concatenate((o[:nf0], o[nf1:]), 0)])
    temp /= np.concatenate((o[:nf0], o[nf1:]), 0)
    temp /= np.pi
    filt[0:nf0-1] = temp[0, 0:nf0-1]
    filt[nf1+1:] = temp[0, nf1+1:]
    hamm = 0.54 - 0.46 * np.cos(2 * np.pi * (np.arange(1, nf + 1)) / nf)
    filt = filt * hamm
    xf = np.convolve(x, filt, mode='same')
    return xf


fig = plt.figure()
ax2 = fig.add_subplot(1, 1, 1)

filtre_x = []
filtre_y = []
mesure = []
temps = []
hilb = []

i = 0
n = 30
zoom = 100

fichier_dat = np.genfromtxt("./2d_envelope.dat", usecols=(
    0, 1, 2, 3, 4, 5, 6), comments="#")
mesure = fichier_dat[:, 6]
temps = fichier_dat[:, 2] * 86400 + fichier_dat[:, 3] * \
    3600 + fichier_dat[:, 4] * 60 + fichier_dat[:, 5]

#hilb = obspy.signal.filter.envelope(mesure)

while i < np.size(temps, 0) - 1200:
    filtre_x = np.hstack([filtre_x, temps[np.arange(i + n, i + (1200 - n))]])
    filtre_y = np.hstack([filtre_y, filter_sinc(
        mesure[np.arange(i, i + 1200)], n * 2)[np.arange(n, 1200 - n)]])
    i = i + 1200

filtre_x = filtre_x / 20
temps = temps / 20

ax2.set_xlim([filtre_x[0], filtre_x[0] + zoom])
ax2.set_ylim([0, 6])

im, = ax2.plot([], [], color=(1, 0, 0))
im2, = ax2.plot([], [], color=(0, 0, 1))
im3, = ax2.plot([], [], color=(0, 1, 0))


def animate(k):

    im.set_xdata(temps)
    im.set_ydata(mesure)

    im2.set_xdata(filtre_x)
    im2.set_ydata(filtre_y)

    im3.set_xdata(temps)
    # im3.set_ydata(hilb)

    #ax2.set_xlim(k + filtre_x, k + filtre_x + zoom)


ani = anim.FuncAnimation(fig, animate, init_func=init,
                         frames=np.size(filtre_x), interval=30, blit=False)
plt.show()
