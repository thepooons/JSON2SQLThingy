from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd

from dataHandler2 import df
from SQLCommunication.create_table import Create_table
from SQLCommunication.show_table import Show_table
from SQLCommunication.search_data import Search_data
from SQLCommunication.add_data import Add_data
from SQLCommunication.delete_data import Delete_data


print(df)


Create_table(df)
print(Show_table())
print(Search_data(2))
Add_data(99, "boi", 10)
print(Show_table())
Delete_data(99)

# importing following file will drop the jsondata table in database ¯\_(ツ)_/¯
#from SQLCommunication import drop_table
