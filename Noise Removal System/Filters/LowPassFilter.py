###################################################################################################
#
# Author: Yash Agrawal
# Project: Speech Verification and Spoofing
#
# This is the implementation of a low pass filter which can be used in the noise removal block 
###################################################################################################

import scipy.io.wavfile
import numpy as np
from random import randint
from numpy import cos, sin, pi, absolute, arange
from scipy.signal import kaiserord, lfilter, firwin, freqz
import wave
import matplotlib.pyplot as plt

#taking inputs of the required files to work and test with
rate, x = scipy.io.wavfile.read('sample.wav')
rate_n, n = scipy.io.wavfile.read('noise.wav')


n = n[0:len(x)]
nyq_rate = 2*rate
t = arange(len(x))

#plotting the original input signal
plt.figure(1)
plt.plot(t, x)

#adding noise to the original signal
x = x + (n/10)
x = np.array(x)


# The desired width of the transition from pass to stop,
# relative to the Nyquist rate.
width = 80.0/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 80.0

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_hz = 4000.0

# Use firwin with a Kaiser window to create a lowpass FIR filter.
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

# Use lfilter to filter x with the FIR filter.
filtered_x = lfilter(taps, 1.0, x)


#plotting the signal with added noise
plt.figure(2)
plt.plot(t, x)

#plotting the filtered signal with removed noise
plt.figure(3)
plt.plot(t, filtered_x)
plt.show()



