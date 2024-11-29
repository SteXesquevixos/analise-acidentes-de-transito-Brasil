
import dados
import app
import streamlit as st
import pandas as pd

df = dados.tratamento_df()

from analises import analise

df1,df2,df3 = analise()

from visualizacao import graficos

graficos(df1,df2,df3)

app.myapp(df)