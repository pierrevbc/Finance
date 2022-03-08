import yfinance as yf
from stocksymbol import StockSymbol

def get_ticker_info(ticker):

    tick = yf.Ticker(ticker)

    return tick.dividends