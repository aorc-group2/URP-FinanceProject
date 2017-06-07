# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import pandas as pd
import pandas.io.data as web


stock_code = 'AMZN'
Data_source = 'google'
start_date ="2015/01/01"
end_date ="2015/05/01"

price = web.DataReader(stock_code, data_source = Data_source, start = start_date, end= end_date)
price.tail()

price[['Close']].plot(color='blue', title= stock_code)



# BIDU: baidu
# AMZN: Amazon
# FB: Facebook
#TWTR: Twitter
#MSFT: Microsoft




