from scipy import signal

def filter_data(data):
    return _filter_data_butterworth_lowpass(data)

def _filter_data_butterworth_lowpass(data):
    db_passband = 1
    db_stopband = 80
    (order, natural_frequency) = signal.buttord(db_passband, db_stopband, 0.1333, 0.1477)
    (a, b) =  signal.butter(order, natural_frequency)
    filtered = signal.lfilter(a, b, data)
    return filtered

def _filter_data_chebyshev_type1_lowpass(data, order = 3):
    pass

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    import numpy as np
    from numpy import dot
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')