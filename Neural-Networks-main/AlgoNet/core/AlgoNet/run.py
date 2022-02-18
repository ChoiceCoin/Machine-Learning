from ALGO_Prediction import algo_prediction
import matplotlib.pyplot as plt

a,b,c = algo_prediction()


plt.figure(figsize=(15, 10))
plt.plot(a, b, color = 'blue', label = 'Real ALGO Prices')
plt.plot(a, c, color = 'red', label = 'Predicted ALGO Prices')
plt.legend(loc='best', fontsize='xx-large')
plt.xticks(fontsize=18)
plt.yticks(fontsize=16)
plt.show()
