import mplfinance as mpf
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import DBSelecter

mk = DBSelecter.MarketDB()
df = mk.get_daily_price('8306')
print(df)
df.index = pd.to_datetime(df.date)
df = df[['open', 'high', 'low', 'close', 'volume']]
kwargs = dict(title='Celltrion candle chart', type='candle',
              mav=(2, 4, 6), volume=True, ylabel='ohlc candles')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, **kwargs, style=s)

