import pandas as pd
import numpy
import glob
import os.path
import streamlit as st
from operator import index

def tratamento_df():
    # Ler ou criar arquivo concatenado

    if os.path.isfile("../data/concat_data.csv"):
        df = pd.read_csv("../data/concat_data.csv")
    else:
        df_all = []
        df_all.append(pd.read_csv("../data/2021.csv",encoding="latin1", sep=";"))
        df_all.append(pd.read_csv("../data/2022.csv"))
        df_all.append(pd.read_csv("../data/2023.csv",encoding="latin1", sep=";"))
        df_all.append(pd.read_csv("../data/2024.csv"))
        df = pd.concat(df_all)

    
    # Conversão de dados para os tipos especificos
    df = df.astype(str)
    for column in df:
        df_aux = df[column].str.replace(',', '.', regex=False)
        df_aux= pd.to_numeric(df_aux, errors='coerce')
        if df_aux.any():
            df[column] = df_aux
            
    df['data'] = pd.to_datetime(df['data_inversa'] + ' ' + df['horario'])
    df_sorted = df.sort_values(by='data')

  

    #Tratamentos de valores NaN e duplicatas
    df_sorted = df_sorted.drop_duplicates()
    for column in df_sorted:
        if df_sorted[column].isnull().sum() != 0:
            if type(df_sorted[column][0] == str):
                df_sorted[column].fillna(df[column].mode()[0], inplace=True)
            else:
                df_sorted[column].fillna(df[column].mean(), inplace=True)

    


    # Extração de informação do datatime

    df_sorted['dia_semana'] = df_sorted['data'].dt.day_name()
    df_sorted['mes'] = df_sorted['data'].dt.month 
    df_sorted['ano'] = df_sorted['data'].dt.year  

    def periodo_dia(hora):
        if 0 <= hora <=6:
            return 'Madrugada'
        elif 6 <= hora < 12:
            return 'Manhã'
        elif 12 <= hora < 18:
            return 'Tarde'
        else:
            return 'Noite'

    df_sorted['periodo_dia'] = df_sorted['data'].dt.hour.apply(periodo_dia)

    # Conversão da coluna 'id' de float para int
    df_sorted['id'] = df_sorted['id'].astype('int64')

    # Adição de colunas com as modificações realizadas acima
    df_sorted.to_csv('../data/concat_data.csv', index=False)
    return df_sorted