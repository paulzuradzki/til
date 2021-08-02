Demonstration of API usage with Python `requests` module using a foreign exchange rates data provider. 

```python

import requests
import pandas as pd

# get response from foreign exchange rate API
# Provide key. Free limited API account available for EUR rates.
ACCESS_KEY = ''
resp = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}&base=EUR')

# convert to Python dict and strip out base and rates sections into variables
data = resp.json()
base = data['base']    # ex: "EUR", "USD"
rates = data['rates']  # ex: {"USD: 1.18685, "PLN": 4.556448}

# store `rates` as dataframe/table
df = pd.DataFrame(rates, index=[f'rate_x_per_{base}']).T 
df[f'rate_{base}_per_x'] = 1/df[f'rate_x_per_{base}']

# display conversion rates to user
# remove .loc[['USD']] selector to show all rates
print(f"Conversion from {base} to:")
print(df.loc[['USD']].to_markdown())

```

Conversion from EUR to:
|     |   rate_x_per_EUR |   rate_EUR_per_x |
|:----|-----------------:|-----------------:|
| USD |          1.18735 |         0.842212 |
