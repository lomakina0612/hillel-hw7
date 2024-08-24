import json
import requests
import openpyxl

from openpyxl import Workbook


rates =[]
for year in range(2021, 2022):
   for month in range(1,5):
      r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
      
      if r.status_code == 200:
         response = json.loads(r.text)
         rate_eur = [item for item in response['exchangeRate'] if item['currency'] == 'EUR']

         # print(rate_eur) 
      print(f'01.{month:02}.{year} 1 EUR = {rate_eur[0]['saleRate']:.2f} UAH') 
      rates.append((f'01.{month:02}.{year}',rate_eur[0]['saleRate']))
   print(rates)
   
wb = Workbook()
ws = wb.active
ws.title = "EUR exchange rate"
ws['A1'] = 'Date'
ws['B1'] = 'EUR'

for idx, rate in enumerate(rates):
   ws[f'A{idx+2}'] = rate[0]
   ws[f'B{idx+2}'] = rate[1]

wb.save("rates.xlsx")
