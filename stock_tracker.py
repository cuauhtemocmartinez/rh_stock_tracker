import config
import robin_stocks as rh
import dateime as dt
import time

def login(days):
    time_logged_in = 60*60*24*days
    rh.authentication.login(username=config.USERNAME,
                            password=config.PASSWORD,
                            expiresIn=time_logged_in,
                            scope+'internal',
                            by_sms=True,
                            store_session=True)

def logout();
    rh.authentication.logout()

def get_stocks():
    stocks = list()
    stocks.append('JG')
    return(stocks)

def open_market():
    market = False
    time_now = dt.datetime.now().time()

    market_open = dt.time(6,30,0) #6:30AM
    market_close = dt.time(12,59,0) #12:59PM

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print('### market is closed')

    return(market)