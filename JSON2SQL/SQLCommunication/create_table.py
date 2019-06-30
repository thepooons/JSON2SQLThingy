from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list
from dataHandler import DataFrameReturner

df = DataFrameReturner()

def Create_table(df):
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
#    cnx.execute('DROP TABLE jsondata1')
    cnx = engine.connect()
    df.to_sql('jsondata', cnx, index = False)
    print('Table created in DB')
