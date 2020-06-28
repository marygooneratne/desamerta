import yfinance as yf
import requests
from ftplib import FTP
import numpy as np
import datetime as dt
# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max


def getHistory(ticker, start_date=None, end_date=None):
    tickerObj = yf.Ticker(ticker.upper())
    history = tickerObj.history(
        start=start_date, end=end_date, auto_adjust=False)

    return history


def getTickers():
    tickers = []

    def processTicker(ticker):
        if(ticker[:6] == 'Symbol'):
            return
        else:
            tickers.append(ticker.split('|')[0])

    with FTP('ftp.nasdaqtrader.com') as ftp:
        ftp.login()
        ftp.cwd('SymbolDirectory')
        # ftp.retrlines('LIST')
        test = ftp.retrlines('RETR nasdaqlisted.txt', processTicker)

    return tickers
