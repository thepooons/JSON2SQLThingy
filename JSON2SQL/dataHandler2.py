from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd
import json #derulo ft. drake
import sys
sys.path.append("APIs")
sys.path.append("SQLCommunication")
sys.path.append("APIs")

with open('data.json') as f:
    table = json.load(f)

df = pd.read_json(json.dumps(table), orient='columns')
