import logging
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import os
from edit_change_unifiedCsv import df_bibliotecas_official,df_cines_official,df_museos_official
from datetime import date
from dotenv import load_dotenv

# This method import the data stored in the .env file which contains sensitive information such as the database username and password.
load_dotenv('.env')
DATABASE_USERNAME=os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
DATABASE_HOST=os.getenv('DATABASE_HOST')
DATABASE_PORT=os.getenv('DATABASE_PORT')
DATABASE_NAME=os.getenv('DATABASE_NAME')

# This allows us to stablish a connection to PostgreSQL and create, if not exists, the database.
def get_engine(user, password, host, port, db):
    url=f'postgresql://{user}:{password}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)
    engine=create_engine(url, echo=False)
    return engine

# The code below will read and import the unified .csv file to PostgreSQL defined above, according to the data stored in the .env file.
# Will also import the individual .csv file of each categ. in order to get correct outputs for specific queries asked in the challenge.
df = pd.read_csv('imported_csv_postgreSQL_'+date.today().strftime('%d-%m-%Y')+'.csv')

engine=get_engine(DATABASE_USERNAME,DATABASE_PASSWORD,DATABASE_HOST,DATABASE_PORT,DATABASE_NAME)

df.to_sql('challenge',engine,if_exists='replace')
df_bibliotecas_official.to_sql('bibliotecas',engine,if_exists='replace')
df_cines_official.to_sql('cines',engine,if_exists='replace')
df_museos_official.to_sql('museos',engine,if_exists='replace')
