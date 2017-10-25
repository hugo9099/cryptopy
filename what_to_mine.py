#!/usr/bin/env python

"""
Install on your environment

pip install requests==2.18.4
pip install beautifulsoup4==4.6.0

"""

import requests
from bs4 import BeautifulSoup
from config import *


# Get URL from config.py file
url = COINWARZ_PROFITS_URL

r = requests.get(url)
html_content = BeautifulSoup(r.content, "html.parser")

# data_table = html_content.find_all("table", {"id": "tblCoins"})
coin_links = html_content.find_all("a", {"class": "link"})

coins = []

# Variable width for table
WIDTH = 40


def get_profits():
    for link in coin_links:
        if "cryptocurrency/coins/" in link.get("href"):
            coin = link.text
            coin = coin.replace(" ", "")
            coin = coin.replace("\r\n", " ")
            coins.append(coin)
            coin_symbol = coin[-4:-1]
            profit_span_name = "spanProfit_" + coin_symbol

            profit_span = html_content.find_all("span", {"id": profit_span_name})
            is_profit = 1
            if not profit_span:
                profit_span = html_content.find_all("span", {"class": "red"})
                is_profit = 0

            profit = ""
            for this_profit in profit_span:
                profit = this_profit.text
            # profit = profit_span.text
            if not is_profit:
                profit = profit[1:-1]
                profit = "- " + profit

            space = WIDTH - len(profit) - len(coin) - 5
            print "| {}:{}{} |".format(coin, " "*space, profit)


def main():
    print "-"*WIDTH
    print "| Coin" + " "*(WIDTH-14) + "Profit |"
    print "-"*WIDTH
    get_profits()
    print "-"*WIDTH


if __name__ == '__main__':
    main()
