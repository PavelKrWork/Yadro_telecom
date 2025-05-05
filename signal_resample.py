import numpy as np
from numpy.linalg import solve

# Передискритизатор сигнала (применяем интерполяционный полином Лагранжа)
def signal_resampler(signal: list, sample_count: int, fs_old: float, fs_new: float) -> list:
  koeff = fs_new / fs_old
  x = [i / (koeff * fs_old) for i in range(sample_count)]  # samples of new signal
  s = np.array(signal)
  n = len(signal)
  M = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      M[i][j] = i ** j

  a = solve(M, s)
  new_signal = [0] * sample_count
  for i in range(sample_count):
    res = 0
    for j in range(n):
      res += a[j] * (x[i] ** j)
    new_signal[i] = res

  return new_signal