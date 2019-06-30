from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list
from dataHandler import df

def Search_data(requiredRoll):
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
    cnx = engine.connect()
    df = cnx.execute('select * from jsondata')
    dataset = []
    for i in df:
        dataset.append(i)
    dataset = pd.DataFrame(dataset, columns=['roll', 'name', 'class'])
    demandedRow = dataset[dataset['roll'] == requiredRoll]
    return ( demandedRow)
