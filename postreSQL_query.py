from re import T
import pandas as pd
import os
from datetime import date
from connect_to_postgre_and_import import engine

engine

# The following codes will connect to PostgreSQL and execute the queries asked in the challenge.

# Procesar los datos conjuntos para poder generar una tabla con la siguiente información:
    # Cantidad de registros totales por categoría
registers_per_categ_query_output='SELECT COUNT (challenge_categ) AS amount_of_registers,challenge_categ AS categ FROM challenge GROUP BY challenge_categ'
first_query_df=pd.read_sql_query(registers_per_categ_query_output,con=engine)
first_query_df.to_csv('registers_per_categ_query_output_'+date.today().strftime('%d-%m-%Y')+'.csv',index=False)

    # Cantidad de registros totales por fuente
registers_per_source='SELECT (fuente),COUNT (challenge_categ) AS bibliotecas_registers_recount FROM bibliotecas GROUP BY fuente; SELECT COUNT (fuente),COUNT (challenge_categ) AS cines_registers_recount FROM cines GROUP BY fuente,challenge_categ; SELECT (fuente),COUNT (challenge_categ) AS museos_registers_recount FROM museos GROUP BY fuente,challenge_categ'
second_query_df=pd.read_sql_query(registers_per_source,con=engine)
second_query_df.to_csv('registers_per_source_query_output_'+date.today().strftime('%d-%m-%Y')+'.csv',index=False)

    # Cantidad de registros por provincia y categoría
registers_per_prov_per_categ_query_output='SELECT  provincia AS prov, challenge_categ AS categ, COUNT (challenge_categ) AS amount_of_registers FROM challenge GROUP BY (provincia), (challenge_categ)'
third_query_df=pd.read_sql_query(registers_per_prov_per_categ_query_output,con=engine)
third_query_df.to_csv('registers_per_prov_per_categ_query_output_'+date.today().strftime('%d-%m-%Y')+'.csv',index=False)

# Procesar la información de cines para poder crear una tabla que contenga:
    # o Provincia
    # o Cantidad de pantallas
    # o Cantidad de butacas
    # o Cantidad de espacios INCAA
registers_per_prov_per_categ_query_output='SELECT  provincia, COUNT (pantallas) as screen_recount, COUNT (butacas) as seats_recount, COUNT (espacio_incaa) as slots_INCAA FROM cines GROUP BY provincia'
fourth_query_df=pd.read_sql_query(registers_per_prov_per_categ_query_output,con=engine)
fourth_query_df.to_csv('total_screens_slots_and_seats_per_prov_query_output_'+date.today().strftime('%d-%m-%Y')+'.csv',index=False)

# The right above query requested by the challenge COULD also be achieved if we had the three last three asked data as columns in the unified .csv file (the first 
# table asked by the challenge), and running a similar query with a few changes like adding a 'WHERE' and selecting to run query on 'challenge' tabla, so it will be like:
# 'SELECT  provincia, COUNT (pantallas) as screen_recount, COUNT (butacas) as seats_recount, COUNT (espacio_incaa) as slots_INCAA FROM challenge WHERE challenge_categ='cines' GROUP BY provincia'
