import streamlit as st
import pandas as pd
import urllib
from sqlalchemy import create_engine




    #pages.append(st.Page('pages/01_home.py', title='page load from page dir'))


def access_engine(access_db):
    #pages/01_home.py
    cnnstr = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=" + access_db
    )
    cnnurl = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(cnnstr)}"
    acc_engine = create_engine(cnnurl)
    return acc_engine

#db_path = (r"C:\DEV\access_streamlit_webreport\mydatabase.accdb")
st.header("Muhammad is the Best ")
db_path = (r"mdn/mydatabase.accdb")
st.header("===========================================Muhammad is the Best ")
st.header("Muhammad is the Best ")
engine = access_engine(db_path)
sql = "Select Distinct [Country name] From CLIMATE_CHANGE_DATA Order By [Country name];"
df_country = pd.read_sql(sql, engine)
sql = "Select Distinct [Series name] From CLIMATE_CHANGE_DATA Order By [Series name];"
df_series = pd.read_sql(sql, engine)
col1, col2 = st.columns(2)
with col1:
    country = st.selectbox("Country", df_country)
    chk_allcountry = st.checkbox('All countries')
with col2:
    series = st.selectbox("Series", df_series)
    chk_allseries = st.checkbox('All series')
sql = ("Select [Country code], [Series code], [Series name], [2000]" 
       " From CLIMATE_CHANGE_DATA Where ID Is Not Null")
if chk_allcountry == False:
    sql += " And [Country name] = '" + country + "'"
if chk_allseries == False:
    sql += " And [Series name] = '" + series + "'"
df = pd.read_sql(sql, engine)
st.table(df)



