import math
import numpy as np
import pandas as pd
import datetime
from api import stock_api


class Equity:
    """[Class that represents an asset by parsing the inputted data file.
        This class contains a few methods for extracting more information
        about prices and movement.]

    Fields:
        closes {float[]} - Closing prices of the equity
        opens {float[]}
        highs {float[]}
        lows {float[]}
        volumes {int[]}
        dates {String[]}

    Returns:
        {Equity}
    """

    def __init__(self, ticker, start_date, end_date, verbose=False):

        self.ticker = ticker
        self.dates = []
        self.opens = []
        self.closes = []
        self.lows = []
        self.highs = []
        self.volumes = []

        self.init_data(stock_api.get_history(
            self.ticker, start_date, end_date))

    def fill_open(self, day):
        has_open = day[1] is not None
        if has_open:
            return day
        has_low = day[3] is not None
        has_high = day[2] is not None
        has_close = day[4] is not None
        if has_low and has_high:
            day[1] = day[3] + (day[2] - day[3])/2
            return day
        elif has_low:
            day[1] = day[3]
        elif has_high:
            day[1] = day[2]
        elif has_close:
            day[1] = day[4]

        return day

    def fill_close(self, day):
        has_close = day[4] is not None
        if has_close:
            return day
        has_low = day[3] is not None
        has_high = day[2] is not None
        has_open = day[1] is not None
        if has_low and has_high:
            day[4] = day[3] + (day[2] - day[3])/2
            return day
        elif has_low:
            day[4] = day[3]
        elif has_high:
            day[4] = day[2]
        elif has_close:
            day[4] = day[4]

        return day

    def fill_high(self, day):
        has_high = day[2] is not None
        if has_high:
            return day
        has_low = day[3] is not None
        has_open = day[1] is not None
        has_close = day[4] is not None
        if has_low:
            day[2] = day[3]
        elif has_open:
            day[2] = day[1]
        elif has_close:
            day[2] = day[4]

        return day

    def fill_low(self, day):

        has_low = day[3] is not None
        if has_low:
            return day
        has_high = day[2] is not None
        has_open = day[1] is not None
        has_close = day[4] is not None
        if has_close:
            day[3] = day[4]
        elif has_open:
            day[3] = day[1]
        elif has_high:
            day[3] = day[2]

        return day

    def fill_vol(self, day):
        if day[5] is None:
            day[5] = 0
        return day

    def val_row(self, day):
        day = self.fill_open(day)
        day = self.fill_close(day)
        day = self.fill_high(day)
        day = self.fill_low(day)
        day = self.fill_vol(day)
        return day[0], day[1], day[2], day[3], day[4], day[5]

    def init_data(self, yf_df):
        for idx, day in yf_df.iterrows():

            day_arr = []
            day_arr.append(idx)
            day_arr.append(day[0])
            day_arr.append(day[1])
            day_arr.append(day[2])
            day_arr.append(day[3])
            day_arr.append(day[5])
            date, open, high, low, close, volume = self.val_row(day_arr)
            if not open:
                open = self.opens[len(self.opens)-1]
                close = self.closes[len(self.closes)-1]
                high = self.highs[len(self.highs)-1]
                low = self.highs[len(self.lows)-1]
                volume = self.volumes[len(self.volumes)-1]
            self.dates.append(datetime.datetime(
                date.year, date.month, date.day))
            self.opens.append(float(open))
            self.highs.append(float(high))
            self.lows.append(float(low))
            self.closes.append(float(close))
            self.volumes.append(int(volume))
        self.dates = np.array(self.dates)
        self.opens = np.array(self.opens)
        self.highs = np.array(self.highs)
        self.lows = np.array(self.lows)
        self.closes = np.array(self.closes)
        self.volumes = np.array(self.volumes)

    def get_price(self, date, type='c', verbose=False):
        if verbose:
            print(date)
        i = self.get_index_from_date(date)

        if type == 'o':
            if verbose:
                print("Getting Open", self.opens[i])
            return self.opens[i]

        elif type == 'h':
            if verbose:
                print("Getting High", self.highs[i])
            return self.highs[i]

        elif type == 'l':
            if verbose:
                print("Getting Low", self.lows[i])

            return self.lows[i]

        else:
            if verbose:
                print("Getting Close", self.closes[i])
            return self.closes[i]

    def get_index_from_date(self, date, verbose=False):

        if date == 'max':
            return len(self.closes) - 1

        for i, d in enumerate(self.dates):
            diff = d - date
            if diff <= datetime.timedelta(0):
                return i

    def conv_date(self, date, verbose=False):
        ts = pd.Timestamp(date)

        return ts.to_pydatetime()
