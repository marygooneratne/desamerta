from rule.asset import Equity
import datetime as dt
sec = Equity.Equity('AAPL', start_date=dt.datetime(
    2020, 1, 1), end_date=dt.datetime(2020, 4, 1))
print(sec.data)
