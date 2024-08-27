import pandas as pd
import os
import matplotlib.pyplot as plt

# merging data
df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')
files = [file for file in os.listdir('./Sales_Data')]
all_month_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('./Sales_Data/' + file)
    all_month_data = pd.concat([all_month_data,df])
all_month_data.to_csv('all_data.csv', index=False)
#print(all_month_data)
all_data = pd.read_csv('all_data.csv')
#print(all_data.head())


# drop rows with nan
nan_df = all_data[all_data.isna().any(axis=1)]
#print(nan_df.head())
all_data = all_data.dropna(how='any')
#print(all_data.head())

#drop or 
temp_df = all_data[all_data['Order Date' ].str[0:2] == 'Or']
#print(temp_df.head())
all_data = all_data[all_data['Order Date' ].str[0:2] != 'Or']
#print(all_data.head())

# converting coloums to the correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# adding sales coloum 
all_data['Sales'] = all_data['Quantity Ordered']* all_data['Price Each']
#print(all_data.head())

#augument data with additional coloums
all_data['month'] = all_data['Order Date'].str[0:2]
#print(all_data.head())
all_data['month'] = all_data['month'].astype('int')
#print(all_data.head())

# What was the best month for sales? what was the earning?
result = all_data.groupby('month').sum()['Sales']

# visiual representations
# months = range(1,13)
# plt.bar(months,result)
# plt.xticks(months)
# plt.xlabel('month number')
# plt.ylabel('usd ($)')
# plt.show()

# what city has the highest number of sales?
all_data['cities'] = all_data['Purchase Address'].apply(lambda x : x.split(',')[1])
#print(all_data.head())
# result = all_data.groupby('cities').sum()['Sales']
# cities = [cities for cities , df in all_data.groupby('cities')]
# plt.bar(cities,result)
# plt.xticks(cities,rotation = 'vertical', size = 8)
# plt.ylabel('sales in usd ($)')
# plt.xlabel('city names')
# plt.show()

# what time should we advertise for max benifit
# all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
# all_data['hour'] = all_data['Order Date'].dt.hour
# all_data['minute'] = all_data['Order Date'].dt.minute
# #print(all_data.head())
# hours = [hour for hour, df in all_data.groupby('hour')]
# plt.plot(hours,all_data.groupby(['hour']).count())
# plt.xticks(hours)
# plt.grid()
# plt.xlabel('hours')
# plt.ylabel('sales')
# plt.show()

# what products are most often sold together
# df = all_data[all_data['Order ID'].duplicated(keep=False)]
# df['grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
# #print(df.head())
# df = df[['Order ID', 'grouped']].drop_duplicates()
# #print(df.head())
# # imports
# from itertools import combinations
# from collections import Counter
# count = Counter()
# for row in df['grouped']:
#     row_list = row.split(',')
#     count.update(Counter(combinations(row_list,2)))
# print(count.most_common(3))


# what products sold the most? why?
product_grp = all_data.groupby('Product')
quantity_ordered = product_grp.sum()['Quantity Ordered']
products = [product for product, df in product_grp]
plt.bar(products,quantity_ordered)
plt.xticks(products,rotation='vertical')
plt.xlabel('Products')
plt.ylabel('quantity sold')
plt.show()
