import streamlit as st


def myapp(df):
    st.set_page_config(
        page_title="Analise de Acidentes de Transito",
        layout='wide',
        initial_sidebar_state='expanded',
    )
    st.write("""
            # Analise de Acidentes de Transito
            Analise Exploratorio de dados de transito no periodo 2021-2024
            """)
    st.write('---')

    st.sidebar.title('Filtros')
    coluna_sorted = sorted(df.columns)
    filtro = st.sidebar.multiselect('Escolha as colunas desejadas:', coluna_sorted)

    if filtro:
        df_selected= df[filtro]
    else:
        df_selected = df

    st.write(f"Dimensões: {df_selected.shape[0]} filas e {df_selected.shape[1]} colunas.")
    st.dataframe(df_selected)