#import the useful libraries.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read the Profit and Loss Statements
data = pd.read_csv("SampleSuperstore.csv")

profit = 0
loss = 0
for record in data.Profit:
    if record > 0:
        profit = profit + record
    else:
        loss = loss + abs(record)
        
print("Total Profit: " + str(round(profit, 2)))
print("Total Loss: " + str(round(loss, 2)))

# data.head()

# Plot Bar chart for Statewise Profit and Losses
data.groupby('State')['Profit'].sum().plot.bar()
plt.xticks(rotation=90)
plt.grid()
plt.show()

# Plot Pie chart for Statewise Profit
data[data.Profit > 0].groupby('State')['Profit'].sum().plot.pie()
plt.grid()
plt.show()
