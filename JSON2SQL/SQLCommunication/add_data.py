from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list
from dataHandler import df

def Add_data(rollToAdd, NameToAdd, classToAdd):
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
    cnx = engine.connect()
    cnx.execute('insert into jsondata(roll, name, class) values(%d, "%s", %d)'%(rollToAdd, str(NameToAdd), classToAdd))

    print('Field added to DB.')
