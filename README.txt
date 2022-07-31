Welcome!

The following job will allow us to download some .csv files from https://www.datos.gob.ar/dataset (specifically about museums, libraries and cinemas in argentina), edit them and import them to Postgresql in order to get some queries output to answer specific requests in Alkemy Challenge.
To work in a virtual environment you should tap Windows Key, write 'CMD', press enter, go to the folter where files are located and type '.\env\Scripts\activate'.

In order to succesfully achieve it, please follow the instructions below.

1- CREATE a notes block (or use the one included alongside with the .py files) and write the following:
DATABASE_USERNAME=XXXX
DATABASE_PASSWORD=XXXX
DATABASE_HOST=XXXX
DATABASE_PORT=XXXX
DATABASE_NAME=XXXX
DATABASE_URL=XXXX

REPLACE the XXXX values for the neccessary data to access to your PostgreSQL database.IMPORTANT: DO NOT LEAVE EMPTY SPACES OR BLANKS, AND DO NOT USE QUOTES.

2-Save the block as '.env'(WITHOUT the quotes) in the same folder where the python files(.py) currently are.

3-Tap Windows Key and write 'CMD', press enter and type one by one the folling comands:
python.exe -m pip install --upgrade pip
pip install pandas
pip install psycopg2
pip install requests
pip install SQLAlchemy
pip install SQLAlchemy-Utils

4-Run the python files(.py) in this order:
download_locate_rename.py
edit_change_unifiedCsv.py
connect_to_postgre_and_import.py
postreSQL_query.py

IMPORTANT: codes work with files with specific-daily-names, this means that if you run the download code to download files at 23:59 and then try to run the next codes at 00:00 or further they will not work, because they will not search for the previous day .csv files but today's ones.

5-The query results will be available as .csv files in the folder where the python files(.py) are located.

That's it!

PD: Still working out in the 'logging' library and .env. (i am just an amateur on this!)