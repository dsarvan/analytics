#!/usr/bin/env python3
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt
plt.style.use('seaborn-ticks')

def tx(F, Fs, alpha, tx_time, time):
    """ transmitted signal """
    freq = F + alpha * tx_time
    signal = np.sin(2*np.pi*freq*time)
    return freq, signal

def rx(F, Fs, alpha, rx_time, time, tau):
    """ reflected signal """
    freq = 0 if time < tau else F + alpha * (rx_time - tau)
    signal = np.sin(2*np.pi*freq*time)
    return freq, signal

F = 77.e9
B = 4.e9
T = 40.e-6
alpha = B/T

R = 300
c = 3.e8
tau = 2.*R/c
Fb = alpha*tau
Fs = 2*B
Ts = 1./Fs
N = round(T/Ts)

initial, final = 0, T
tx_time, rx_time = 0, tau

for n in range(3):
    for time in np.linspace(initial, final, N):
        tx_freq, tx_signal = tx(F, Fs, alpha, tx_time, time)
        rx_freq, rx_signal = rx(F, Fs, alpha, rx_time, time, tau)
        IF_signal = [tx_signal*rx_signal]
