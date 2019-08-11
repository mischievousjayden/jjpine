import quandl 


class QuandlStockData(object):
    def __init__(self, api_key):
        quandl.ApiConfig.api_key = api_key

    def get_stock_data(self, ticker, start_date, end_date, collapse="daily", columns=None):
        quote = "WIKI/{}".format(ticker) 
        data = quandl.get(quote, start_date=start_date, end_date=end_date, collapse=collapse)
        return data[columns] if columns else data
