import requests
import os
from datetime import datetime
from datetime import date
import logging

# This allows to get the date in format "year(number) - month(written)".
def year_month_date_string_spanish(date):
  months = ("enero", "febrero", "marzo", "abri", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
  month = months[date.month - 1]
  year = date.year
  messsage = "{} - {}".format(year, month)

  return messsage

date_now=datetime.now()

diccionario = {'museos':"https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv",
    "bibliotecas":"https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv",
    "cines":"https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"}     

# This will attempt to download the .csv files, locate them in folders and rename them as asked in the Alkemy Challenge If an error occurs, will save the report 
# in the 'download_locate_rename_execution_report.log' file.

logging.basicConfig(filename='download_locate_rename_execution_report.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

try:
  for categ in diccionario:
    path=f"{categ}/{year_month_date_string_spanish(date_now)}/"
    file_path = path + categ + "-" + date.today().strftime('%d-%m-%Y') +".csv"
    os.makedirs(os.path.dirname(path),exist_ok=True)
    response=requests.get(diccionario[categ])
    with open(file_path,'wb') as archivo:
      archivo.write(response.content)
except Exception as ex:
  logging.exception(str(ex))