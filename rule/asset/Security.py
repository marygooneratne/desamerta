import math
import numpy as np
import pandas as pd
import datetime
from api import stock_api
import Asset
import datetime as dt


class Security(Asset):
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
        super().__init__()

    def execute(self, date=None):
        start_date = date - dt.timedelta(days=100)
        return Equity(self.params['ticker'], start_date=start_date, end_date=date)
