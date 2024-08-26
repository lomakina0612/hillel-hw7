import json
import requests
import openpyxl

from openpyxl import Workbook
from openpyxl.chart import (
    LineChart,
    Reference,
)
from openpyxl.chart.axis import DateAxis
from openpyxl.drawing.image import Image
from datetime import datetime

# rates =[('Date', 'EUR')]
# for year in range(2021, 2022):
#    for month in range(1,13):
#       r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.{month:02}.{year}')
      
#       if r.status_code == 200:
#          response = json.loads(r.text)
#          rate_eur = [item for item in response['exchangeRate'] if item['currency'] == 'EUR']

#          # print(rate_eur) 
#       print(f'01.{month:02}.{year} 1 EUR = {rate_eur[0]['saleRate']:.2f} UAH') 
#       rates.append((f'01.{month:02}.{year}',rate_eur[0]['saleRate']))
#    print(rates)

rates =[('Date', 'EUR'),
        ('01.01.2021', 34.97), 
        ('01.02.2021', 34.2), 
        ('01.03.2021', 33.9), 
        ('01.04.2021', 32.85), 
        ('01.05.2021', 33.75), 
        ('01.06.2021', 33.7), 
        ('01.07.2021', 32.6), 
        ('01.08.2021', 32.2), 
        ('01.09.2021', 32.15), 
        ('01.10.2021', 31.1), 
        ('01.11.2021', 30.7), 
        ('01.12.2021', 31.1)]
   
wb = Workbook()
ws = wb.active
ws.title = "EUR exchange rate"

for idx, rate in enumerate(rates, start=1):
   ws[f'A{idx}'] = rate[0]
   ws[f'B{idx}'] = rate[1]

wb.save("rates.xlsx")

c1 = LineChart()
c1.title = "EUR to UAH exchange rate"
c1.style = 13
c1.x_axis.title = 'Date'
c1.y_axis.title = 'Rate'

c1.y_axis.crossAx = 500
c1.x_axis = DateAxis(crossAx=100)
c1.x_axis.number_format = "dd.mm.yy"
c1.x_axis.majorTimeUnit = "months"

data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(rates))
c1.add_data(data, titles_from_data=True)
dates = Reference(ws, min_col=1, min_row=2, max_row=len(rates))
c1.set_categories(dates)

s1 = c1.series[0]
s1.marker.symbol = "circle"
s1.marker.graphicalProperties.solidFill = "FFFFFF" # Marker filling
s1.marker.graphicalProperties.line.solidFill = "FF0000" # Marker outline
s1.graphicalProperties.line.solidFill = "FF0000"
s1.graphicalProperties.line.width = 40000 # width in EMUs
s1.graphicalProperties.line.noFill = False

c1.width = 20  
c1.height = 10  

ws.add_chart(c1, "D1")
wb.save("rates.xlsx")
