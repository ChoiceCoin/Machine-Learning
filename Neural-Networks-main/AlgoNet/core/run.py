from ALGO_Prediction import algo_prediction
from BTC_Prediction import btc_prediction
from ETH_Prediction import eth_prediction
import matplotlib.pyplot as plt

a,b,c = algo_prediction()
d,e,f = btc_prediction()
g,h,i = eth_prediction()



plt.figure(figsize=(15, 10))
plt.plot(a, b, color = 'blue', label = 'Real ALGO Prices')
plt.plot(a, c, color = 'red', label = 'Predicted ALGO Prices')
plt.legend(loc='best', fontsize='xx-large')
plt.xticks(fontsize=18)
plt.yticks(fontsize=16)
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(d, e, color = 'blue', label = 'Real BTC Prices')
plt.plot(d, f, color = 'red', label = 'Predicted BTC Prices')
plt.legend(loc='best', fontsize='xx-large')
plt.xticks(fontsize=18)
plt.yticks(fontsize=16)
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(g, h, color = 'blue', label = 'Real ETH Prices')
plt.plot(g, i, color = 'red', label = 'Predicted ETH Prices')
plt.legend(loc='best', fontsize='xx-large')
plt.xticks(fontsize=18)
plt.yticks(fontsize=16)
plt.show()
