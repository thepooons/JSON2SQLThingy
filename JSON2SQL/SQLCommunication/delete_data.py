from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list

def Delete_data(removeDisRoll):
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
    cnx = engine.connect()
    cnx.execute('DELETE FROM jsondata WHERE roll = %d'%removeDisRoll)

    print('Deleted field from DB.')
