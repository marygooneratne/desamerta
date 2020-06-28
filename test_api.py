from rule.asset import Security
import datetime as dt
sec = Security.Security('AAPL', start_date=dt.datetime(
    2020, 1, 1), end_date=dt.datetime(2020, 4, 1))
print(sec.data)
