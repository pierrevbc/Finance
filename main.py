from yahoo_data import *
from logger import *
import os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    log = Logger(os.getcwd())
    get_ticker_info('msft')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
