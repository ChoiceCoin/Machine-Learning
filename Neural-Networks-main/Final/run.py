from ALGO_Prediction import algo_prediction
from BTC_Prediction import btc_prediction
from ETH_Prediction import eth_prediction
import matplotlib.pyplot as plt

main,a,b,c = algo_prediction()
main_1,d,e,f = btc_prediction()
main_2,g,h,i = eth_prediction()



plt.figure(figsize=(15, 10))
plt.plot(a, b, color = 'blue', label = 'Real ALGO Prices')
plt.plot(a, c, color = 'red', label = 'Predicted ALGO Prices')
plt.legend(loc='best', fontsize='large')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(d, e, color = 'blue', label = 'Real BTC Prices')
plt.plot(d, f, color = 'red', label = 'Predicted BTC Prices')
plt.legend(loc='best', fontsize='large')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(g, h, color = 'blue', label = 'Real ETH Prices')
plt.plot(g, i, color = 'red', label = 'Predicted ETH Prices')
plt.legend(loc='best', fontsize='large')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

if main > 30:
    print("The current relative strength index of ALGO is greater than 30, suggesting growth:", main)
else:
    print("The current relative strength index of ALGO is less than 30, suggestng a future downward trend:", main)
if main_1 > 30:
    print("The current relative strength index of BTC is greater than 30, suggesting growth:", main_1)
else:
    print("The current relative strength index of BTC is less than 30, suggestng a future downward trend:", main_1)
if main_2 > 30:
    print("The current relative strength index of ETH is greater than 30, suggesting growth:", main_2)
else:
    print("The current relative strength index of ETH is less than 30, suggestng a future downward trend:", main_2)
