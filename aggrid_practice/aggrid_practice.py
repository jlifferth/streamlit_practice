import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# path = '/Users/jonathanlifferth/data/seaborn-data/flights.csv'
# data = pd.read_csv(path)
# print(data.head())

data = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(data)

