import dados
import app
import streamlit as st
import pandas as pd
df = dados.tratamento_df()
app.myapp(df)

#Aplicativo no streamlit
#ideias
#   colocar para realizar upload do arquivo necessario para os dashboard.
#   dar a opção de salvar o Dataframe gerado pelo streamlit

