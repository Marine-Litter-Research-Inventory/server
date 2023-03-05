# Full Name [N] Author(s)
# Scholar profile
# Publication title [L] Title
# Research topics [BK] Research Topics
# Methodology Used [AM] Methodologies Used
# RRI ID [C] ID

import pandas as pd
import sqlite3

key = '1yRLGaQk3-9UlopftPr5e8F-X3pKkjwLlZWcTwai6_Ds'
name = 'RRI+2.0+-+Masterlist'
url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(key, name)

def create():
  df = pd.read_csv(url)
  df.drop('Number of filled cells', axis=1, inplace=True)
  df.drop('Progress', axis=1, inplace=True)
  df.drop(df.shape[0]-1, inplace=True)
  df.drop(df.shape[0]-1, inplace=True)
  df["Microplastic Sizes"] = pd.to_numeric(df["Microplastic Sizes"], errors="coerce")
  df["Year Published"] = pd.to_numeric(df["Year Published"], errors="coerce")
  # df.to_json("data.json", orient='records')

  connection = sqlite3.connect("database/data.db")
  df.to_sql("masterlist", connection, if_exists='replace', index=True)
  cur = connection.cursor()
  res = cur.execute("SELECT * FROM masterlist LIMIT 1")
  if res is not None:
    print("Database init successfully")
  else:
    print("Something went wrong with initing database")
  connection.close()


