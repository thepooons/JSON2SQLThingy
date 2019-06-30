from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list

def Drop_table():
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
    cnx = engine.connect()
    cnx.execute('DROP TABLE jsondata')

    print('Deleted da whole table from DB.')


Drop_table()
