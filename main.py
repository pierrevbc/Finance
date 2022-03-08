from yahoo_data import *
from logger import *
import os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    logger = Logger(os.getcwd())

    df = get_ticker_info('msft')

    logger.log_message(df.tail())