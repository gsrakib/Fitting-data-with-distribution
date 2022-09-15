# poissionian distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import factorial
excel_1 = "lab1.xlsx"
df_first = pd.read_excel(excel_1,sheet_name = "Sheet5")
x1 = list(df_first['Count Rate'])
plt.hist(x1, bins = 200, rwidth= 0.7)
# the mean = 815.45, probablity density function is given by:
x = np.arange(10,60,.001)

# Gaussian
y1 = 0.0595*np.exp(-((x-30.506)**2)/89.86)
plt.plot(x,y1*100)
plt.hist(x1, bins = 200, rwidth= 0.7)
plt.xlabel('Count Rate (1/s)')
plt.ylabel('pdf*100')
plt.title("Gaussian Distribution")
plt.show()


# Poisson
mu =30.506
y = np.exp(-mu)*np.power(mu,x)/(factorial(x))
plt.plot(x,y*30)
plt.hist(x1, bins = 200, rwidth= 0.7)
plt.xlabel('Count Rate (1/s)')
plt.ylabel('pdf*30')
plt.title("Poisson Distribution")
plt.show()

# Binomial
p = 0.30506
y3 = ((factorial(100))/((factorial(x))*(factorial(100-x))))*(np.power(p,x))*(np.power(1-p,100-x))
plt.plot(x,y3*30)
plt.hist(x1, bins = 200, rwidth= 0.7)
plt.xlabel('Count Rate (1/s)')
plt.ylabel('pdf*30')
plt.title("Binomial Distribution")
plt.show()