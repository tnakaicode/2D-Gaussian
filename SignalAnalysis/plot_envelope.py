import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
from scipy import fftpack
from optparse import OptionParser

sys.path.append(os.path.join('../'))
from src.base import create_tempdir, plot2d


def fft_ave(data, samplerate, Fs):
    fft = fftpack.fft(data)
    # 振幅成分を計算
    fft_ampl = np.abs(fft / (Fs / 2))
    fft_freq = np.linspace(0, samplerate, Fs)
    return fft, fft_ampl, fft_freq


if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--flag", dest="flag", default=1, type="int")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    # サンプルの時間領域信号を生成
    dt = 0.001
    t = np.arange(0, 1, dt)
    wave = np.cos(2 * np.pi * 50 * t)
    wave *= (1 + 0.1 * np.sin(2 * np.pi * 2.5 * t))
    wave *= (1 + 0.5 * np.sin(2 * np.pi * 7.5 * t))

    fft, fft_amp, fft_axis = fft_ave(wave, 1 / dt, len(wave))

    # 負周波数域（ナイキスト周波数以降）を0にする（実部と虚部の両方）
    zeros = np.zeros(int(len(fft) / 2))
    fft[int(len(fft) / 2):len(fft)] = zeros

    # 正周波数域（ナイキスト周波数まで）を2倍する
    fft *= 2

    # 操作した実部と虚部を持つ周波数波形をIFFTし、絶対値をとる（包絡線を得る）
    ifft_time = np.abs(fftpack.ifft(fft))

    # ここからグラフ描画
    # フォントの種類とサイズを設定する。
    #plt.rcParams['font.size'] = 14
    #plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    #plt.rcParams['xtick.direction'] = 'in'
    #plt.rcParams['ytick.direction'] = 'in'

    obj = plot2d()
    ax1 = obj.add_axs(2, 1, 1, aspect="auto")
    ax2 = obj.add_axs(2, 1, 2, aspect="auto")
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')
    ax1.set_xlabel('Frequency [Hz]')
    ax1.set_ylabel('x(f)')

    ax2.yaxis.set_ticks_position('both')
    ax2.xaxis.set_ticks_position('both')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('x(t)')

    ax1.set_xticks(np.arange(0, 1 / dt, 20))
    ax1.set_xlim(0, 100)
    ax1.plot(fft_axis, fft_amp, label='signal', lw=1)

    ax2.plot(t, wave, label='original', lw=1)
    ax2.plot(t, ifft_time, label='envelope', lw=1)

    ax1.legend()
    ax2.legend()
    obj.SavePng_Serial()
