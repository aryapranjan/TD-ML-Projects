#import the useful libraries.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read the Global Terrorism Dataset
data= pd.read_csv("globalterrorismdb_0718dist.csv", encoding='iso-8859-1', low_memory=False)

data.country_txt.value_counts(normalize=False).head(10).plot.bar()
plt.show()
