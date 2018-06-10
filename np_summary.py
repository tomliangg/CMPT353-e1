import numpy as np

data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

'''
print (totals)
print ('//////')
print (counts)
'''

sum_prep = np.sum(totals, axis=1)  # compute the sum of each row
print (sum_prep)
print (np.argmin(sum_prep))

avg_prep_by_month = np.sum(totals, axis=0) / np.sum(counts, axis=0)
print (avg_prep_by_month)

avg_prep_by_city = np.sum(totals, axis=1) / np.sum(counts, axis=1)
print (avg_prep_by_city)

row = len(totals)
totals_quarter = np.reshape(totals, (4*row, 3))
prep_by_city_quarterly =  np.sum(totals_quarter, axis=1)
prep_by_city_quarterly.shape = (row, 4)
print (prep_by_city_quarterly)