import pandas as pd

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])
sum_totals_city = totals.sum(axis=1)
print (sum_totals_city.idxmin(axis=0))

sum_counts_month = counts.sum(axis=0)
sum_totals_month = totals.sum(axis=0)
print (sum_totals_month / sum_counts_month)

sum_counts_city = counts.sum(axis=1)
print (sum_totals_city / sum_counts_city)