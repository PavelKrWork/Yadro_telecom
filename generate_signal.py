import numpy as np

def generate_sin(frequency, duration, fs=100):
    """
    Генератор синусоидального сигнала
    :param frequency: частота сигнала (0..50 Гц)
    :param duration: длительность сигнала в секундах
    :param fs: частота дискретизации (фиксированная 100 Гц)
    :return: массив отсчетов сигнала
    """
    t = np.arange(0, duration, 1/fs)
    return np.sin(2 * np.pi * frequency * t)
