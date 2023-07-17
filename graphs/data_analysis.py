import pandas as pd

full = pd.read_csv('/workspaces/amazon_analysis/cleaned_amazon.csv')

young = full[full['age'] < 18]

full['age'].replace(3, 30)

full = full[full['age'] >= 18]

full.to_csv('/workspaces/amazon_analysis/cleaned_amazon.csv')