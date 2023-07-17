import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full = pd.read_csv('../cleaned_amazon.csv')

# examing age catagory
"""
# check no abnormal ages
plt.bar(full['age'].value_counts().index, full['age'].value_counts().values)

plt.savefig('age_bar.png')
plt.clf()

# looking at distribution of ages
plt.hist(full['age'], bins=10)

plt.savefig('age_hist.png')
"""
