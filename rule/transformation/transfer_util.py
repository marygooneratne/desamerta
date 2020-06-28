import pandas as pd
import math
import numpy as np


def sma(prices, period):
    """[
        Function to calculate the Simple Moving Average 
    for the equity at a given period
    ]

    Arguments:
        prices {[float[]]} -- [description]
        period {[int]} -- [length of closing prices to look at for each equity]

    Returns:
        [float[]] -- [array of SMA values for each day, 0 until 'period']
    """
    simple_ma = np.zeros((len(prices),))
    for i, p in enumerate(prices):
        if i + period - 1 >= len(prices):
            break
        ma = 0
        for j in range(period):
            ma = prices[i + j] + ma
        simple_ma[i] = ma/period
    return simple_ma[:(-1*(period))]


def ema(prices, period, kind=''):
    """
    [
        Function to calculate the Exponential Moving 
    Average for the equity at a given period
    ]

    Arguments:
        prices {[float[]]} -- [Prices to look at]
        period {[int]} -- [length of closing prices to look at for each equity]

    Keyword Arguments:
        kind {str} -- [either reg or ema] (default: {''})

    Returns:
        [float[]] -- [the ema of the prices inputted as a vector]
    """

    exponential_ma = np.zeros((len(prices),))
    simple_ma = sma(prices, period)
    base_sma = simple_ma[-1 * (period - 1)]

    if kind == 'wilder':
        multiplier = (1 / period)
    else:
        multiplier = (2 / (period + 1))
    exponential_ma[-1 * (period - 1)] = calc_ema(base_sma,
                                                 prices[-period], multiplier)
    l = len(prices)
    for i, p in enumerate(prices):
        if l - i - period < 0:
            break
        ma = 0
        exponential_ma[l - i - period] = calc_ema(exponential_ma[l - i - period + 1],
                                                  prices[l -
                                                         i - period],
                                                  multiplier)
    return exponential_ma[:(-1*(period))]


def calc_ema(prev_ema, close, multiplier):
    """[
        Implements the Exponential Moving Average formula
    ]
    @param: prev_ema = .\n
    @param: close = \n
    @param: multiplier = \n
    @return: ema = \n
    Arguments:
        prev_ema {[float]} -- [EMA for the previous day]
        close {[float]} -- [current day's close]
        multiplier {[float]} -- [weight for current data]

    Returns:
        [float -- [the value of the EMA for the given day]
    """
    return (close - prev_ema) * multiplier + prev_ema


def macd(prices, slow_period, fast_period):
    """
    Calculate the Moving Average Compounding Difference\n
    @param: slow_period = number of days for longer period\n
    @param: fast_period = number of days for shorter period\n
    @requirement: slow_period > fast_period\n
    @return: macd = an array of the MACD to the same indexes close for the given period.\n
        For example, if 'fast_period' is 10 and 'slow_period' is 20, the ith 
        index will correspond to the difference between the ith EMA(20) and ith EMA(10). 
        indexes 0-19 will be 0
    """
    assert slow_period > fast_period
    return ema(prices, slow_period) - ema(prices, fast_period)[slow_period-fast_period:]


def calc_moves(prices, period=1):
    """
    Calculate the movement between two periods\n
    @param: period = number of days between closes\n
    @return: moves = an array of the move relative to the same indexes close for the given period.\n
        For example, if  'period' is 10, the ith index will correspond 
        to the difference between the ith close and i - 10th close. 
        indexes 0-9 will be 0
    """
    moves = np.zeros((len(prices),))
    for i, close in enumerate(prices):
        index = i + period
        if index >= len(prices):
            break
        moves[index] = prices[index] - prices[index - period]
    return moves[:(-1*period)]


def rsi(prices, period=20, kind='ema'):
    up, down = calc_up_down(prices=prices)
    if kind == 'sma':
        up_avg = sma(up, period)
        down_avg = sma(down, period)
    elif kind == 'ema':
        up_avg = ema(up, period, '')
        down_avg = ema(down, period, '')
    else:
        up_avg = ema(up, period, 'wilder')
        down_avg = ema(down, period, 'wilder')
    rsi = np.zeros((len(up_avg),))
    for i, num in enumerate(up_avg):
        if down_avg[i] == 0:
            relative_strength = float('inf')
        else:
            relative_strength = up_avg[i] / down_avg[i]
        rsi[i] = 100 - (100 / (1 + relative_strength))
    return rsi


def calc_up_down(prices, period=1):
    """
    Calculates the up-down of the equity for a given period\n @param: period = number of days between closes\n
    @return: up: an array of the move relative to the same indexes close for the given period. With a floor at
    0.\n @return: down: an array of the move relative to the same indexes close for the given period. With a
    cieling at 0.\n For example, if 'period' is 1, the ith index of 'up' will correspond to the difference
    between the ith close and i - 1 th close but negative entries will be 0. 'down' will be all negative entries
    with the positives as 0. index 0 will be 0
    """
    moves = calc_moves(prices, period)
    up = np.zeros((len(prices),))
    down = np.zeros((len(prices),))
    for i, move in enumerate(moves):
        if move > 0:
            up[i] = move
        else:
            down[i] = -1 * move
    return up, down


def macd_indicator(prices, slow_period, fast_period):
    macd_vals = macd(prices, slow_period, fast_period)

    macd_emas = ema(macd_vals, 9)
    macd_ind = np.zeros((len(macd_vals),))
    for i, macd_val in enumerate(macd_vals):

        # print(macd_val, macd_vals[i+1], macd_emas[i], macd_emas[i+1])
        macd_ind[i] = gen_macd_ind_lbl(
            macd_val, macd_vals[i+1], macd_emas[i], macd_emas[i+1])
    macd_ind = np.array([(macd_val - macd_ema)
                         for (macd_val, macd_ema) in zip(macd_vals, macd_emas)])
    return macd_ind


def gen_macd_ind_lbl(macd_val_0, macd_val_1, macd_ema_0, macd_ema_1):
    cross = check_intersection(
        macd_val_0, macd_val_1, macd_ema_0, macd_ema_1)

    if cross is True:
        m = get_slope(0, 1, macd_val_0, macd_val_1)
        if m >= 0:
            return 1
    # For now just generating ones on buy and zeros else... eventually three classes might be good
    return 0


def check_intersection(y_11, y_12, y_21, y_22):
    x11, x12, x21, x22 = 0, 1, 0, 1
    # print(y_11, y_12, y_21, y_22)
    m1 = get_slope(0, 1, y_11, y_12)
    m2 = get_slope(0, 1, y_21, y_22)
    b1 = y_11
    b2 = y_21
    A = np.array([[m1, -1], [m2, -1]]).reshape((2, 2))
    b = np.array([b1, b2]).reshape((2, 1))
    # print(A)
    # print(b)
    X = np.linalg.solve(A, b)
    x = X[0]
    y = X[1]
    cross = False
    if(x >= 0 and x <= 1):
        cross = True

    return cross


def get_slope(x_0, x_1, y_0, y_1):
    m = (y_1 - y_0)/(x_1 - x_0)
    return m


def average_true_range(asset, period=10):
    true_ranges = np.zeros((len(asset.closes),))
    for i, close in enumerate(asset.closes):
        if i + 1 >= len(asset.closes):
            break
        high = asset.highs[i]
        low = asset.lows[i]
        cp = asset.closes[i + 1]
        true_ranges[i] = np.max(
            [high - low, np.abs(high - cp), np.abs(low - cp)])
    avg_tr = calc_average_true_range(true_ranges, period)
    return avg_tr


def calc_average_true_range(true_ranges, period=10):
    atr = np.zeros((len(true_ranges),))
    l = len(true_ranges)
    prevatr = true_ranges[-1]
    for i, tr in enumerate(true_ranges):
        atr[l - i - 1] = (prevatr * (period - 1) +
                          true_ranges[l - i - 1]) / period
        prevatr = atr[l - i - 1]
    return atr[:-1]


def roc(prices):
    roc_vals = np.zeros((len(prices),))
    for i, price in enumerate(prices):
        if i >= len(prices) - 1:
            break
        roc_vals[i] = ((price / prices[i + 1]) - 1) * 100

    return roc_vals[:-1]


def kst(prices):
    tenp_roc = np.zeros((len(prices),))
    fifteenp_roc = np.zeros((len(prices),))
    twentyp_roc = np.zeros((len(prices),))
    thirtyp_roc = np.zeros((len(prices),))
    for i in range(len(prices)):
        if i + 10 >= len(prices):
            continue
        tenp_roc[i] = (prices[i] - prices[i+10])/prices[i+10]
        if i + 15 >= len(prices):
            continue
        fifteenp_roc[i] = (prices[i] - prices[i+15])/prices[i+15]
        if i + 20 >= len(prices):
            continue
        twentyp_roc[i] = (prices[i] - prices[i+20])/prices[i+20]
        if i + 30 >= len(prices):
            continue
        thirtyp_roc[i] = (prices[i] - prices[i+30])/prices[i+30]
    rcma_1 = sma(tenp_roc, 10)
    rcma_2 = sma(fifteenp_roc, 10)
    rcma_3 = sma(twentyp_roc, 10)
    rcma_4 = sma(thirtyp_roc, 15)

    kst_vals = np.zeros((len(rcma_4),))
    for i, p in enumerate(rcma_4):
        kst_vals[i] = rcma_1[i] + rcma_2[i] * 2 + rcma_3[i] * 3 + rcma_4[i] * 4
    return kst_vals


def kst_trix_indicator(prices):
    kst_vals = kst(prices)[:-94]
    d_kst = d_(kst_vals)

    trix_vals = trix(prices)
    d_trix = d_(trix_vals)

    assert len(kst_vals) == len(trix_vals)

    ind = np.zeros((len(d_kst),))

    for i in range(len(ind)):
        ind[i] = np.sign(d_kst[i] * d_trix[i])

    return ind[:-1]


def d_(prices):
    d_p = np.zeros((len(prices),))

    for i in range(len(d_p)):
        if i + 1 >= len(d_p):
            continue
        d_p[i] = prices[i] - prices[i + 1]

    return d_p


def calc_pivot_points(high, low, close):
    pivot = (high + low + close) / 3

    r1 = (pivot * 2) - low
    r2 = pivot + (high - low)
    s1 = (pivot * 2) - high
    s2 = pivot - (high - low)

    return pivot, r1, r2, s1, s2


def get_r(curr_high, curr_low, prev_close, prev_open):
    one = curr_high - prev_close
    two = curr_low - prev_close
    three = curr_high - curr_low

    if one >= two and one >= three:
        r = curr_high - prev_close - \
            (0.5 * (curr_low - prev_close)) + (0.25 * (prev_close - prev_open))
    if two >= one and two >= three:
        r = curr_low - prev_close - \
            (0.5 * (curr_high - prev_close)) + \
            (0.25 * (prev_close - prev_open))
    if three >= one and three >= two:
        r = curr_high - curr_low + (0.25 * (prev_close - prev_open))

    return r


def calc_std(prices, period):
    stds = np.zeros((len(prices),))

    for i in range(len(prices)):
        if i + period >= len(prices):
            continue
        stds[i] = np.std(prices[i:i+period])

    return stds[:(-1*(period))]


def rainbow_ma(prices, periods=(1, 3, 5, 7, 9)):

    return [sma(prices, period).T for period in periods]


def trix(prices):
    single_smoothed_ema = ema(prices, 18)
    double_smoothed_ema = ema(single_smoothed_ema, 18)
    triple_smoothed_ema = ema(double_smoothed_ema, 18)

    trix_vals = np.zeros((len(triple_smoothed_ema),))

    for i in range(len(trix_vals)):
        if i + 1 >= len(trix_vals):
            continue
        if triple_smoothed_ema[i + 1] == 0:
            trix_vals[i] = 0
            continue

        trix_vals[i] = (triple_smoothed_ema[i] -
                        triple_smoothed_ema[i + 1]) / triple_smoothed_ema[i + 1]

    return trix_vals[:-55]


def trix_indicator(prices):
    trix_vals = trix(prices)[:-9]
    t_ma = ema(trix_vals, 9)
    assert len(trix_vals) == len(t_ma)
    return np.array([trix_vals[i] - t_ma[i] for i in range(len(trix_vals))])


def prings_know_sure_thing(prices):
    kst_vec = kst(prices)
    kst_sma = sma(kst_vec, 9)
    kst_vec = kst_vec[:-9]
    assert len(kst_vec) == len(kst_sma)
    return np.array([kst_vec[i] - kst_sma[i] for i in range(len(kst_sma))])


def ohlc(security, verbose=False):
    """The average of the open low high close

    Returns:
        [float[]] -- [A vector of the averages]
    """

    avg = (security.opens + security.highs +
           security.lows + security.closes) / 4
    return avg


def typical_prices(security, verbose=False):
    """The 'Typical Prices' of the equity, or the average of the high,low, and close

    Returns:
        [float[]] -- [Vector of the averages]
    """
    tps = (security.highs + security.lows + security.closes) / 3
    return tps


def balance_of_power(security, verbose=False):
    """The balance of the power is a metric for
     determining the variability in the opens/closes versus
     highs/lows

    Returns:
        [float[]] -- [Vector of the index]
    """
    bop = (security.closes - security.opens) / (security.highs - security.lows)
    return bop


def bollinger_bands(security, period=20, stds=2, verbose=False):
    """[The Bolinger Bands is essentially a confidence interval of 
    stds Deviations where the price should be based on the last 
    period periods of prices]

    Keyword Arguments:
        period {int} -- [The period over which to look over the 
        prices] (default: {20})
        stds {int} -- [The number of standard deviations the bands 
        should take up] (default: {2})

    Returns:
        [float[], float[]] -- [Upper Bolinger Band, Lower Bolinger Band vectors respectively]
    """
    tp = typical_prices(security)
    ma = sma(prices=tp, period=period)
    std = calc_std(prices=tp, period=period)
    bolu = np.array([ma[i] + stds * std[i] for i in range(len(ma))])
    bold = np.array([ma[i] + stds * std[i] for i in range(len(ma))])
    return bolu, bold


def accumulative_swing_index(security, verbose=False):
    """[ASI is a way of looking at the prices of the equity
    in order to get information regarding momentum and market
    conditions]

    Returns:
        [float[]] -- [ASI values in a vector]
    """
    asi = np.zeros((len(security.closes),))
    for i in range(len(security.closes)):
        if i + 1 >= len(security.closes):
            break
        curr_close = security.closes[i]
        prev_close = security.closes[i + 1]
        curr_open = security.opens[i]
        prev_open = security.opens[i + 1]
        curr_high = security.highs[i]
        prev_high = security.highs[i + 1]
        curr_low = security.lows[i]
        prev_low = security.lows[i + 1]
        k = np.max([(prev_high - curr_close), (prev_low - curr_close)])
        t = curr_high - curr_low
        kt = k / t
        num = (prev_close - curr_close + (0.5 * (prev_close - prev_open)
                                          ) + (0.25 * (curr_close - curr_open)))
        r = get_r(curr_high, curr_low, prev_close, prev_open)
        body = num / r
        asi[i] = 50 * body * kt
    return asi[:-1]


def gop_range_index(security, period=10, verbose=False):
    """The GOP looks at the largest swing in prices over the
    last period periods.

    Keyword Arguments:
        period {int} -- [Period over which to calculate GOP] 
        (default: {10})

    Returns:
        [float[]] -- [A vector of the GOP values]
    """
    gop = np.zeros((len(security.closes),))
    for i in range(len(security.closes)):
        if i + period >= len(security.closes):
            continue
        highest = np.max(security.highs[i:i+period])
        lowest = np.min(security.lows[i:i + period])
        price_range = highest - lowest
        gop[i] = math.log(price_range) / math.log(period)
    return gop


def pivot_points(verbose=False):
    """[Pivot poits are the centers of recent price movement]

    Returns:
        [float[],float[],float[],float[],float[]] -- [The pivot
        points, restiance one band, resistance 2 band, support 1
        band and support 2 band respectively as vectors.]
    """
    closes = closes
    highs = highs
    lows = lows
    pivots = np.zeros((len(closes),))
    r1s = np.zeros((len(closes),))
    r2s = np.zeros((len(closes),))
    s1s = np.zeros((len(closes),))
    s2s = np.zeros((len(closes),))
    for i in range(len(closes)):
        pivot, r1, r2, s1, s2 = calc_pivot_points(highs[i], lows[i], closes[i])
        pivots[i] = pivot
        r1s[i] = r1
        r2s[i] = r2
        s1s[i] = s1
        s2s[i] = s2
    return pivots, r1s, r2s, s1s, s2s


def pivot_indicator(security, verbose=False):
    """[Gets the spread between closing prices and the pivot points
    for a given day]

    Returns:
        [float[]] -- [Vector of the differences]
    """
    pivots, *_ = pivot_points()
    ind = np.zeros((len(pivots),))
    for i in range(len(pivots)):
        ind[i] = security.closes[i] - pivots[i]
    return ind


def get_deltas(self):
    values = delta_values()
    len = len(values)
    return self


def delta_values(self):
    values = []
    for i, value in enumerate(values):
        if(i+1 >= len(values)):
            continue
        values.append((values[i+1]-value)/value)

    return values
