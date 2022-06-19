#dependencies
import requests
import matplotlib.pyplot as plot
import json
import numpy as np
import sys
import os
import argparse

from genData import gen_main

#crypto currency price prediction program
#made by: Lachi Balabanski

#wrappers for main
def getUserCoin():
    coin = input('Please enter cryptocurrency abbreviation (btc, eth, etc.): ')

    while True:
        temp = requests.get('https://coinbin.org/' + str(coin))

        if temp.status_code == 200:
            return coin.lower()

        else:
            print('Invalid Coin')
            coin = input('Please enter cryptocurrency abbreviation (btc, eth, etc.): ')

def showGraph(data, coinName, title_mod='History'):
    xList = range(len(data), 0, -1)
    
    yList = data

    plot.plot(xList, yList)
    plot.title('Coin ' + title_mod + ' of ' + str(coinName).upper())
    plot.xlabel('Time')
    plot.ylabel('Price (USD)')
    plot.show()

def getData(coin, time):
    content = requests.get('https://coinbin.org/' + str(coin) + '/history').content
    data = json.loads(content)['history']
    data = data[:time]
    list_data = list(map(lambda x: x['value'], data))
    return list_data

def generate_data(dataArray, seed):
    return gen_main(dataArray, seed)

#main
def main(): 
    # This program has data points from October 22, 2017 and before.
    # All predictions are from data from that point and before.
    # The program cannot factor in data points from 10/22/17 to present day

    #parse arguments
    p = argparse.ArgumentParser()
    p.add_argument('-s', '--seed', help="seed to be used", type=int, default=123)
    args = p.parse_args()
    seed = args.seed

    print("prediction coins by Lachi Balabanski")
    coin = getUserCoin()

    try:
        time = int(input('From how long ago would you like to view data from?(days): '))

    except ValueError:
        print("Error while parsing previous input, will revert to default=31")
        time = 31
    
    print('\nLoading Data. . .', end='   ')
    data = getData(coin, time)
    print('[DONE]')

    print('\nGenerating Data. . .', end='   ')
    gen_data = generate_data(data, seed=seed)
    print('[DONE]')
    
    showGraph(data, coin)

    showGraph(gen_data, coin, title_mod='Prediction')


if __name__ == "__main__":
    main()
