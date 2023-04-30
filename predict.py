import requests
import pandas as pd
from fbprophet import Prophet

# Pulling data from CoinGecko API
response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90')
bitcoin_data = response.json()

# Formatting data into a dataframe
bitcoin_df = pd.DataFrame(bitcoin_data['prices'], columns=['timestamps', 'prices'])
bitcoin_df['timestamps'] = pd.to_datetime(bitcoin_df['timestamps'], unit='ms')
bitcoin_df = bitcoin_df.set_index('timestamps')
bitcoin_df = bitcoin_df.resample('D').mean().reset_index()

# Renaming columns for Prophet model
bitcoin_df = bitcoin_df.rename(columns={'prices': 'y', 'timestamps': 'ds'})[['ds', 'y']]

# Creating Prophet model and fitting data
m = Prophet()
m.fit(bitcoin_df)

# Creating future dataframe for predictions
future = m.make_future_dataframe(periods=2, freq='D')

# Making predictions for the next 2 days
forecast = m.predict(future.tail(2))

# Displaying the predicted prices for the next 2 days
print(forecast[['ds', 'yhat']].tail(2))
