import matplotlib.pyplot as plt
import seaborn as sns
import plotly

from analises import acidentes_transito_df_normalizado, acidentes_transito_df

''' ------------------------------ Matriz de Correlação ---------------------------------------'''

plt.figure(figsize=(30,15))
sns.heatmap(acidentes_transito_df_normalizado.corr(method='pearson'),annot=True)
plt.tight_layout()
plt.savefig('imagens/heatmap.png')
plt.clf()


''' ------------------ Histograma: Top 5 causas mais comuns dos acidentes ------------------- '''

dict_acidentes = acidentes_transito_df['causa_acidente'].value_counts().to_dict()
dict_acidentes = dict(sorted(dict_acidentes.items(), key=lambda item: item[1], reverse=True))
top_5_causa_acidentes = dict(list(dict_acidentes.items())[:5])

fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data=top_5_causa_acidentes,
                 hue=top_5_causa_acidentes.keys(),
                 x=list(top_5_causa_acidentes.keys()),
                 y=list(top_5_causa_acidentes.values()),
                 palette='rocket',
                 width=.5,
                 legend=True)

# Adiciona os valores acima das barras
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                fontsize=12, color='black',
                xytext=(0, 5), textcoords='offset points')

ax.set_title(label='Top-5 causas mais comuns dos acidentes', fontsize=14)

plt.xlabel('Causa do acidente', fontsize=12)
plt.ylabel('N° de ocorrências', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Remove os rótulos do eixo x
ax.set_xticks([])

# Ajusta a legenda para não sobrepor as barras
ax.legend(title='Legenda', loc='upper left', bbox_to_anchor=(.54, 1))

plt.tight_layout()
plt.savefig('imagens/causa_acidente.png')
plt.clf()


''' ------------------ Histograma: Top 5 tipos mais comuns de acidentes ------------------- '''

dict_tipos_acidentes = acidentes_transito_df['tipo_acidente'].value_counts().to_dict()
dict_tipos_acidentes = dict(sorted(dict_tipos_acidentes.items(), key=lambda item: item[1], reverse=True))
top_5_tipos_acidentes = dict(list(dict_tipos_acidentes.items())[:5])

fig, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data=top_5_tipos_acidentes,
                 hue=top_5_tipos_acidentes.keys(),
                 x=list(top_5_tipos_acidentes.keys()),
                 y=list(top_5_tipos_acidentes.values()),
                 palette='rocket',
                 width=.5,
                 legend=True)

# Adiciona os valores acima das barras
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                fontsize=12, color='black',
                xytext=(0, 5), textcoords='offset points')

ax.set_title(label='Top-5 tipos mais comuns dos acidentes', fontsize=14)

plt.xlabel('Tipo de acidente', fontsize=12)
plt.ylabel('N° de ocorrências', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Remove os rótulos do eixo x
ax.set_xticks([])

# Ajusta a legenda para não sobrepor as barras
ax.legend(title='Legenda', loc='upper left', bbox_to_anchor=(.73, 1))

plt.tight_layout()
plt.savefig('imagens/tipos_acidente.png')
plt.clf()


''' ---------------------- Distribuição geográfica dos acidentes --------------------------- '''

''' ------------------Relação entre número de vítimas e condições do tempo ----------------- '''

