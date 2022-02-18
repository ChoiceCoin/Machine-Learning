from test import algo_prediction
import matplotlib.pyplot as plt

a,b,c = algo_prediction()

plt.figure(figsize=(15, 10))
plt.plot(a, b, color = 'blue', label = 'Real ALGO Prices')
plt.plot(a, c, color = 'red', label = 'Predicted ALGO Prices')
plt.legend(loc='best', fontsize='large')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()