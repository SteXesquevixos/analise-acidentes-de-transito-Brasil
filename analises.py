import pandas as pd
import numpy as np

from sklearn.preprocessing  import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def analise():
    pd.set_option('display.max_columns', None)
    acidentes_transito_df = pd.DataFrame(pd.read_csv('../data/concat_data.csv'))


    shape = acidentes_transito_df.shape
    info = acidentes_transito_df.info()
    descricao = acidentes_transito_df.describe()
    valores_unicos_por_coluna = acidentes_transito_df.nunique()

    '''
        Conversão de variáveis categóricas em numéricas
    '''
    acidentes_transito_df_copy = acidentes_transito_df.copy()

    conversao = LabelEncoder()

    def conversao_colunas_categoricas_em_numericas():

        colunas_para_conversao = acidentes_transito_df_copy[['dia_semana', 'uf', 'municipio', 'causa_acidente',
                                                            'tipo_acidente', 'classificacao_acidente', 'fase_dia',
                                                            'sentido_via', 'condicao_metereologica', 'tipo_pista',
                                                            'tracado_via', 'uso_solo', 'regional', 'delegacia', 'uop',
                                                            'periodo_dia']]
        for coluna in colunas_para_conversao:
            acidentes_transito_df_copy[coluna] = conversao.fit_transform(acidentes_transito_df_copy[coluna])

        return acidentes_transito_df_copy.head()

    conversao_colunas_categoricas_em_numericas()

    # Seleção de colunas numericas, excluindo as latitude e longitude
    acidentes_transito_df_numericos_apenas = acidentes_transito_df_copy.select_dtypes(include=['int64','float64'])
    acidentes_transito_df_numericos_apenas = acidentes_transito_df_numericos_apenas.drop(['latitude','longitude'], axis=1)


    '''
        Padronização dos dados com StandarScaler
    '''

    escala_standard = StandardScaler()

    acidentes_transito_df_padronizado = escala_standard.fit_transform(acidentes_transito_df_numericos_apenas.values)
    acidentes_transito_df_padronizado = pd.DataFrame(acidentes_transito_df_padronizado, columns=acidentes_transito_df_numericos_apenas.columns)

    '''
        Normalização dos dados com MinMaxScaler
    '''
    escala_min_max = MinMaxScaler()
    acidentes_transito_df_normalizado = escala_min_max.fit_transform(acidentes_transito_df_numericos_apenas.values)
    acidentes_transito_df_normalizado = pd.DataFrame(acidentes_transito_df_normalizado, columns=acidentes_transito_df_numericos_apenas.columns)

    return acidentes_transito_df_normalizado, acidentes_transito_df, acidentes_transito_df_copy