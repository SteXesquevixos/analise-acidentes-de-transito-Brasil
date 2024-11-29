import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt



def myapp(df):
    st.write("""
            # Analise de Acidentes de Transito
            Analise Exploratorio de dados de transito no periodo 2021-2024
            """)
    st.write('---')
    #Dataframe
    st.sidebar.title('Filtros da Tabela')
    coluna_sorted = sorted(df.columns)
    filtro = st.sidebar.multiselect('Escolha as colunas desejadas:', coluna_sorted, key="multiselect_1")
    #Filtro do dataframe
    if filtro:
        df_selected= df[filtro]
    else:
        df_selected = df

    st.write(f"Dimensões: {df_selected.shape[0]} filas e {df_selected.shape[1]} colunas.")
    st.dataframe(df_selected)
    csv = df_selected.to_csv(index=False)
    st.download_button(
    label="Baixar Dataframe filtrado",
    data=csv,
    file_name="dados_dataframe.csv")

    #Graficos de causas e tipos de acidentes
    st.write("### TOP 5")
    opcao = st.radio("Filtrar acidentes por:", ["Causas","Tipos"])
    if opcao == "Causas":
        st.image("../imagens/causa_acidente.png")
    elif opcao == "Tipos":
        st.image("../imagens/tipos_acidente.png")
    
    #Mapa interativo 
    st.write("### Mapa Interativo dos Acidentes")
    df_aux = df
    st.sidebar.title('Filtros do mapa')
    coluna_sorted_map = sorted(df_aux.columns)

    #Filtro aplicado à sidebar
    filtro_map= st.sidebar.multiselect('Escolha as colunas desejadas:', coluna_sorted_map, key="multiselect_2")
    if filtro_map:
        valores_unicos = {coluna: df_aux[coluna].dropna().unique() for coluna in filtro_map}
        #Criação de selectboxes conforme filtros selecionados
        selecoes = {}
        for coluna, valores in valores_unicos.items():
            selecoes[coluna] = st.sidebar.selectbox(
                f"Selecione um valor para {coluna}:",
                options=["Todos"] + list(valores),  
                key=f"selectbox_{coluna}"
            )
        #Aplicado filtros
        df_filtrado = df_aux.copy()
        for coluna, valor_selecionado in selecoes.items():
            if valor_selecionado != "Todos":
                df_filtrado = df_filtrado[df_filtrado[coluna] == valor_selecionado]
    else:
        df_filtrado = df_aux
    #Plot do Mapa
    df_map = df_filtrado[["latitude","longitude"]]
    st.map(data = df_map)
    csv = df_map.to_csv(index=False)
    st.download_button(
    label="Baixar dados do mapa",
    data=csv,
    file_name="dados_map.csv")

    #Graficos de Dispersão
    st.write("### Relação entre Vítimas e Condições Meteorológicas")

    df['total_vitimas'] = df['mortos'] + df['feridos_leves'] + df['feridos_graves']

    # Agrupar por condição meteorológica 
    dados_agrupados = df.groupby('condicao_metereologica', as_index=False)['total_vitimas'].sum()

    # Ordenar os dados por número de vítimas 
    dados_agrupados = dados_agrupados.sort_values(by='total_vitimas', ascending=False)

    # Plot do gráfico de dispersão
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(
        data=dados_agrupados,
        x='condicao_metereologica',
        y='total_vitimas',
        size='total_vitimas',  
        ax=ax,
        legend=False
    )

    # Configurações do gráfico
    ax.set_title('Relação entre Condições Meteorológicas e Número de Vítimas', fontsize=16)
    ax.set_xlabel('Condições Meteorológicas', fontsize=12)
    ax.set_ylabel('Número Total de Vítimas', fontsize=12)
    ax.tick_params(axis='x', rotation=45)

    st.pyplot(fig)

    st.write("### Heatmap Completo do Dataframe")
    st.image("../imagens/heatmap.png")
    

