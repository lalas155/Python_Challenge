import pandas as pd
import os
import download_locate_rename
from datetime import date
from datetime import datetime
import csv


date_now=datetime.now()

# This set the headers of the unified csv file that will be imported to PostgreSQL.
desired_columns = ['cod_loc','idprovincia','iddepartamento','challenge_categ','provincia','localidad','nombre','domicilio','cp','num_de_telefono','mail','web','fecha_de_carga']

# This gets the location of the different files.
museos_csv_path=os.getcwd()+'/'+'museos'+'/'+download_locate_rename.year_month_date_string_spanish(date_now)+'/'+'museos'+"-"+date.today().strftime('%d-%m-%Y')+".csv"
bibliotecas_csv_path=os.getcwd()+'/'+'bibliotecas'+'/'+download_locate_rename.year_month_date_string_spanish(date_now)+'/'+'bibliotecas'+"-"+date.today().strftime('%d-%m-%Y')+".csv"
cines_csv_path=os.getcwd()+'/'+'cines'+'/'+download_locate_rename.year_month_date_string_spanish(date_now)+'/'+'cines'+"-"+date.today().strftime('%d-%m-%Y')+".csv"

# The code below will make some changes to the .csv files so that way we make sure that there will be no issues either when unifying or when interacting with the data 
# stored in PostgreSQL via importing, due to the fact that it is really sensitive when dealing with CAPITAL LETTERS. Wil also add the missing headers and columns 
# with the apropiate data required to achieve fitting query outputs according to the challenge.
df_museos=pd.read_csv(museos_csv_path,dtype={'cod_area': 'str'})
df_bibliotecas=pd.read_csv(bibliotecas_csv_path,dtype={'cod_area': 'str'})
df_cines=pd.read_csv(cines_csv_path,dtype={'cod_area': 'str',})

df_museos_official=pd.DataFrame(df_museos)
df_museos_official.insert(0,'challenge_categ','museos')
df_museos_official.insert(0,'fecha_de_carga',date.today().strftime('%d-%m-%Y'))
df_museos_official.rename({'direccion':'domicilio'}, axis=1, inplace=True)
df_museos_official["num_de_telefono"] = df_museos_official['cod_area'].astype(str) +"-"+ df_museos_official["telefono"].astype(str)

df_bibliotecas_official=pd.DataFrame(df_bibliotecas)
df_bibliotecas_official.insert(0,'challenge_categ', 'bibliotecas')
df_bibliotecas_official.insert(0,'fecha_de_carga',date.today().strftime('%d-%m-%Y'))
df_bibliotecas_official.rename({'Cod_tel':'cod_area'}, axis=1, inplace=True)
df_bibliotecas_official.rename({'Teléfono':'telefono'}, axis=1, inplace=True)
df_bibliotecas_official["num_de_telefono"] = df_bibliotecas_official['cod_area'].astype(str) +"-"+ df_bibliotecas_official["telefono"].astype(str)

df_cines_official=pd.DataFrame(df_cines)
df_cines_official.insert(0,'challenge_categ', 'cines')
df_cines_official.insert(0,'fecha_de_carga',date.today().strftime('%d-%m-%Y'))
df_cines_official.rename({'Dirección':'domicilio'}, axis=1, inplace=True)
df_cines_official.rename({'Teléfono':'telefono'}, axis=1, inplace=True)
df_cines_official["num_de_telefono"] = df_cines_official['cod_area'].astype(str) +"-"+ df_cines_official["telefono"].astype(str)

official_df_list=(df_cines_official,df_bibliotecas_official,df_museos_official)
for df_official in official_df_list:
  df_official_lowers_headers=df_official.rename(columns=str.lower, inplace=True)

# This code will extract from each modified .csv file we got from the code above the columns that are required to get the first challenge table and will also unified 
# them in a single exported .csv ready to import to PostgreSQL.

imported_df_museos_official=df_museos_official[desired_columns].copy()
imported_df_bibliotecas_official=df_bibliotecas_official[desired_columns].copy()
imported_df_cines_official=df_cines_official[desired_columns].copy()
df_merged_list=(imported_df_museos_official,imported_df_bibliotecas_official,imported_df_cines_official)
df_final = pd.concat(df_merged_list,ignore_index=True)
df_final.to_csv('imported_csv_postgreSQL_'+date.today().strftime('%d-%m-%Y')+'.csv', index=False)