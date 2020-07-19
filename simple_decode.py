"""Display the WAV file data.

Taken from https://gist.github.com/nya3jp/5094571c5905783327f35e8df207c8ad#file-spectrogram-ipynb
"""
import sys

from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

_DEFAULT_WAV_FILE = 'data/radio-transmission-recording.wav'


def read_file(file_name=None):
  """Returns a tuple of the "simple rate" and the ndarray of the wav file."""
  file_name = file_name or _DEFAULT_WAV_FILE
  # tuple of (44110, ndarray size 2725380)
  return wavfile.read(file_name)


def plot_wav(rate, data):
  # nperseg is the length of each segment
  f, t, sxx = signal.spectrogram(data, fs=rate, nperseg=1024, window='hann')
  # f "array of sample frequencies" ndarray size 513
  # t "array of segment times" ndarray size 3041
  # sxx "spectrogram of the data" ndarry size (513, 3041)
  plt.figure(figsize=(100, 2))
  plt.pcolormesh(t, f[:20], sxx[:20, :], shading='gouraud')
  plt.show()


def main():
  wav_file = sys.argv[1] if len(sys.argv) > 1 else None
  plot_wav(*read_file(wav_file))


if __name__ == '__main__':
  sys.exit(main())
