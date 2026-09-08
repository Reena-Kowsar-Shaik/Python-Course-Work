

import pandas as pd
prices=[2999,15999,52999,4999,1999]
products=["wireless earbuds","smartphone","laptop","smartwatch","bluetooth speker"]
product_prices=pd.Series(prices,index=products)
print(product_prices)

print("Mean:",product_prices.mean())
print("Max:",product_prices.max())
print("Min:",product_prices.min())
print("sum:",product_prices.sum())

print("Head (first 3 elements):\n",product_prices.head(3))
print("Tail (last 2 elements):\n",product_prices.tail(2))

print("Apply (Adding 18% GST):\n", product_prices.apply(lambda x:f'₹{x+(x*0.18)}'))
print("map(formattig as currently):\n",product_prices.map(lambda x:f'₹{x}.00'))

print(product_prices.sort_values())

print(product_prices.sort_index())

print(product_prices.sort_index(ascending=False))

print("value counts:\n", product_prices.value_counts())

