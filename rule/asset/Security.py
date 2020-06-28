import math
import numpy as np
import pandas as pd
import datetime
from api import stock_api


class Security:
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

        self.data = stock_api.getHistory(self.ticker, start_date, end_date)

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
