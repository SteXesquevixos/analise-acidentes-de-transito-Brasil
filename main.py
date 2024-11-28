
import dados
import app
import streamlit as st
import pandas as pd


print("entrei")
dados.tratamento_df()
print("entrei")

from analises import analise

df1,df2,df3 = analise()

from visualizacao import graficos

graficos(df1,df2,df3)

# app.myapp()

#Aplicativo no streamlit
#ideias
#   colocar para realizar upload do arquivo necessario para os dashboard.
#   dar a opção de salvar o Dataframe gerado pelo streamlit
