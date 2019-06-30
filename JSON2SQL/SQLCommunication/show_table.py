from sqlalchemy import create_engine
import pandas as pd
import sys
sys.path.append(".")
sys.path.append("..")
# Add the ptdraft folder path to the sys.path list

def Show_table():
    engine  = create_engine('mysql://root:hello123@localhost/jsondatastore')
    cnx = engine.connect()
    df = cnx.execute('select * from jsondata')
    #print(df)
    dataset = []
    for i in df:
        dataset.append(i)
        #print(i)
    return pd.DataFrame(dataset)
