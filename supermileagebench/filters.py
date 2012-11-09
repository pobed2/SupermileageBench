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
#
#    # Check the input
#    try:
#        window_size = np.abs(np.int(window_size))
#        order = np.abs(np.int(order))
#    except ValueError:
#        raise ValueError("window_size and order have to be of type int")
#    if window_size > len(x):
#        raise TypeError("Not enough data points!")
#    if window_size % 2 != 1 or window_size < 1:
#        raise TypeError("window_size size must be a positive odd number")
#    if window_size < order + 1:
#        raise TypeError("window_size is too small for the polynomials order")
#    if order <= deriv:
#        raise TypeError("The 'deriv' of the polynomial is too high.")
#
#    # Calculate some required parameters
#    order_range = range(order+1)
#    half_window = (window_size -1) // 2
#    num_data = len(x)
#
#    # Construct Vandermonde matrix, its inverse, and the Savitzky-Golay
#    #coefficients
#    a = [[ii**jj for jj in order_range] for ii in range(-half_window,
#        half_window+1)]
#    pa = np.linalg.pinv(a)
#    sg_coeff = pa[deriv] * rate**deriv * factorial(deriv)
#
#    # Get the coefficients for the fits at the beginning and at the end
#    # of the data
#    coefs = np.array(order_range)**np.sign(deriv)
#    coef_mat = np.zeros((order+1, order+1))
#    row = 0
#    for ii in range(deriv,order+1):
#        coef = coefs[ii]
#        for jj in range(1,deriv):
#            coef *= (coefs[ii]-jj)
#        coef_mat[row,row+deriv]=coef
#        row += 1
#    coef_mat *= rate**deriv
#
#    # Add the first and last point half_window times
#    firstvals = np.ones(half_window) * x[0]
#    lastvals  = np.ones(half_window) * x[-1]
#    x_calc = np.concatenate((firstvals, x, lastvals))
#
#    y = np.convolve( sg_coeff[::-1], x_calc, mode='full')
#
#    # chop away intermediate data
#    y = y[window_size-1:window_size+num_data-1]
#
#    # filtering for the first and last few datapoints
#    y[0:half_window] = dot(dot(dot(a[0:half_window], coef_mat),
#        np.mat(pa)),x[0:window_size])
#    y[len(y)-half_window:len(y)] = dot(dot(dot(a[half_window+1:window_size],
#        coef_mat), pa), x[len(x)-window_size:len(x)])
#
#    return y