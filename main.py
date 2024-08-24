import json
import requests

r = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014')

if r.status_code == 200:
   response = json.loads(r.text)
   print (response)

# response = {'date': '01.12.2014', 
#             'bank': 'PB', 
#             'baseCurrency': 980, 
#             'baseCurrencyLit': 'UAH', 
#             'exchangeRate': [
#                {'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 12.831925, 'purchaseRateNB': 12.831925}, 
#                {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 13.21074, 'purchaseRateNB': 13.21074, 'saleRate': 15.0, 'purchaseRate': 13.0}, 
#                {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 0.679695, 'purchaseRateNB': 0.679695, 'saleRate': 0.8, 'purchaseRate': 0.6}, 
#                {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 2.525893, 'purchaseRateNB': 2.525893}, 
#                {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.0612592, 'purchaseRateNB': 0.0612592}, 
#                {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 3.862738, 'purchaseRateNB': 3.862738, 'saleRate': 4.5, 'purchaseRate': 3.7}, 
#                {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.1272593, 'purchaseRateNB': 0.1272593, 'saleRate': 0.15, 'purchaseRate': 0.12}, 
#                {'baseCurrency': 'UAH', 'currency': 'LVL', 'saleRateNB': 0.1272593, 'purchaseRateNB': 0.1272593}, 
#                {'baseCurrency': 'UAH', 'currency': 'LTL', 'saleRateNB': 5.443385, 'purchaseRateNB': 5.443385}, 
#                {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 2.160957, 'purchaseRateNB': 2.160957, 'saleRate': 2.6, 'purchaseRate': 2.1}, 
#                {'baseCurrency': 'UAH', 'currency': 'SKK', 'saleRateNB': 2.160957, 'purchaseRateNB': 2.160957}, 
#                {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 2.028375, 'purchaseRateNB': 2.028375}, 
#                {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 15.638975, 'purchaseRateNB': 15.638975, 'saleRate': 17.0, 'purchaseRate': 15.5}, 
#                {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 23.632491, 'purchaseRateNB': 23.632491, 'saleRate': 25.8, 'purchaseRate': 24.0}, 
#                {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 15.056413, 'purchaseRateNB': 15.056413, 'saleRate': 15.7, 'purchaseRate': 15.35}, 
#                {'baseCurrency': 'UAH', 'currency': 'BYR', 'saleRateNB': 0.00139, 'purchaseRateNB': 0.00139}, 
#                {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 18.79492, 'purchaseRateNB': 18.79492, 'saleRate': 20.0, 'purchaseRate': 19.2}, 
#                {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 8.150089, 'purchaseRateNB': 8.150089}, 
#                {'baseCurrency': 'UAH', 'currency': 'PLZ', 'saleRateNB': 4.492201, 'purchaseRateNB': 4.492201, 'saleRate': 5.0, 'purchaseRate': 4.2}
#              ]}

rate_eur = [item for item in response['exchangeRate'] if item['currency'] == 'EUR']

print(rate_eur) 
# [{'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 18.79492, 'purchaseRateNB': 18.79492, 'saleRate': 20.0, 'purchaseRate': 19.2}]
print(rate_eur[0]['saleRate']) 
# 20.0
