import yfinance as yf
from stocksymbol import StockSymbol
# get stock info

def get_ticker_info(ticker):

    msft = yf.Ticker(ticker)
    msft.financials