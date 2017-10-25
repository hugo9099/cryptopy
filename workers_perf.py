#!/usr/bin/env python

import requests
from config import *


WIDTH = 56


def get_global_performance(wallet):
    miner_url = 'https://api.ethermine.org/miner/{}/currentStats'.format(wallet)
    miner_request = requests.get(miner_url)
    miner_data = miner_request.json()

    averageHashrate = round(miner_data['data']['averageHashrate'] / 1000000.0, 2)
    usdPerMin = miner_data['data']['usdPerMin']
    unpaid = miner_data['data']['usdPerMin']
    activeWorkers = miner_data['data']['activeWorkers']
    reportedHashrate = round(miner_data['data']['reportedHashrate'] / 1000000.0, 2)
    currentHashrate = round(miner_data['data']['currentHashrate'] / 1000000.0, 2)
    global_performance = round(averageHashrate * 100 / reportedHashrate, 2)

    print "  Reported Hashrate:    " + "{:.2f}".format(reportedHashrate)
    print "  Average  Hashrate:    " + "{:.2f}".format(averageHashrate)
    print "  Current  Hashrate:    " + "{:.2f}".format(currentHashrate)
    print "  Active Workers:       " + str(activeWorkers)
    print "  Global Performance:   " + "{:.2f}".format(global_performance) + " %"


def get_worker_performance(wallet):
    workers_url = 'https://api.ethermine.org/miner/{}/workers'.format(wallet)
    workers_request = requests.get(workers_url)
    workers_data = workers_request.json()

    for rig in workers_data['data']:
        worker = rig['worker']
        reported = round(rig['reportedHashrate']/1000000.0, 2)
        average = round(rig['averageHashrate']/1000000.0, 2)
        current = round(rig['currentHashrate']/1000000.0, 2)
        performance = round(average*100/reported, 2)
        sp = (14 - len(worker)) / 2
        row = ""
        row += " " * sp
        row += worker + " " * sp
        row += " " * 5
        row += "{:.2f}".format(reported) + " " * 8
        row += "{:.2f}".format(average) + " " * 8
        row += "{:.2f}".format(performance) + " %"
        print row


def main():
    wallet = ETH_WALLET

    print ""
    print "-" * WIDTH
    get_global_performance(wallet)
    print "-" * WIDTH
    print "|   Worker   |   Reported   |   Average   |   % Perf   |"
    print "-" * WIDTH
    get_worker_performance(wallet)
    print "-" * WIDTH
    print ""


if __name__ == '__main__':
    main()
