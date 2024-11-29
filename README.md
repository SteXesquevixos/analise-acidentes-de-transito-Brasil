# Análise de acidentes de trânsito no Brasil

Este projeto visa desenvolver a análise exploratória dos dados fornecidos abertamente pela PRF sobre ocorrências de acidentes de trânsito no Brasil.

### Informações sobre a base de dados

- Base de dados disponibilizado como “Documento CSV de Acidentes 202X (Agrupados por ocorrência)” pelo governo brasileiro (fonte: [Dados Abertos de Ocorrências de Acidentes de Trânsito no Brasil](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf))
- Registros de 2021 a 2024.
- O agrupamento dos dados resultou em 250889 registros de acidentes.

| Nome da variável       | Descrição                                                                                      | Tipo   | Exemplo                                                 | Obeservação                                                                                                                       |
|------------------------|------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------| 
| id                     | identificador do acidente                                                                      | float  |                                                         |                                                                                                                                   |
| data_inversa           | data da ocorrência no formato dd/mm/aaa                                                        | string |                                                         |                                                                                                                                   |
| dia_semana             | dia da semana da ocorrência                                                                    | string | Segunda, Terça, etc.                                    |                                                                                                                                   |
| horario                | horário da ocorrência no formato hh:mm:ss                                                      | string |                                                         |                                                                                                                                   |
| uf                     | unidade da federação                                                                           | string | MG, PE, DF, etc.                                        |                                                                                                                                   |
| br                     | identificador da BR do acidente                                                                | int    |                                                         |                                                                                                                                   |
| km                     | identificação do km onde ocorreu o acidente                                                    | string |                                                         | mínimo de 0,1km e com a casa decimal separada por ponto                                                                           |
| municipio              | nome do município de ocorrência do acidente                                                    | string |                                                         |                                                                                                                                   |
| causa_acidente         | identificação da causa presumível do acidente                                                  | string | Falta de atenção, Velocidade incompatível, etc.         |                                                                                                                                   |
| tipo_acidente          | identificação do tipo de acidente                                                              | string | Colisão frontal, Saída de pista, etc.                   |                                                                                                                                   |
| classificacao_acidente | classificação quanto à gravidade do acidente                                                   | string | Sem Vítimas, Com Vítimas, Com Vítimas Fatais e Ignorado |                                                                                                                                   |
| fase_dia               | fase do dia no momento do acidente                                                             | string | Amanhecer, Pleno dia, etc.                              |                                                                                                                                   |
| sentido_via            | sentido da via considerando o ponto de colisão                                                 | string | Crescente e decrescente                                 |                                                                                                                                   |
| condicao_metereologica | condição meteorológica no momento do acidente                                                  | string | Céu claro, chuva, vento, etc.                           | 
| tipo_pista             | tipo da pista considerando a quantidade de faixa                                               | string | Dupla, simples ou múltipla                              |                                                                                                                                   |
| tracado_via            | descrição do traçado da via                                                                    | string |                                                         |                                                                                                                                   |
| uso_solo               | descrição sobre as características do local do acidente                                        | string | Reta, curva ou cruzamento                               |                                                                                                                                   |
| pessoas                | total de pessoas envolvidas na ocorrência                                                      | int    | Urbano ou rural                                         |                                                                                                                                   |
| mortos                 | total de pessoas mortas envolvidas na ocorrência                                               | int    |                                                         |                                                                                                                                   |
| feridos_leves          | total de pessoas com ferimentos leves envolvidas na ocorrência                                 | int    |                                                         |                                                                                                                                   |
| feridos_graves         | total de pessoas com ferimentos graves envolvidas na ocorrência                                | int    |                                                         |                                                                                                                                   |
| ilesos                 | total de pessoas ilesas envolvidas na ocorrência                                               | int    |                                                         |                                                                                                                                   |
| ignorados              | total de pessoas envolvidas na ocorrência e que não se soube o estado físico                   | int    |                                                         |                                                                                                                                   |
| feridos                | total de pessoas feridas envolvidas na ocorrência                                              | int    |                                                         | soma dos feridos leves com os graves                                                                                              |
| veiculos               | total de veículos envolvidos na ocorrência                                                     | int    |                                                         |                                                                                                                                   |
| latitude               | latitude do local do acidente em formato geodésico decimal                                     | string |                                                         |                                                                                                                                   |
| longitude              | longitude do local do acidente em formato geodésico decimal                                    | string |                                                         |                                                                                                                                   |
| regional               | superintendência regional da PRF cujo acidente ocorreu dentro dos limites de sua circunscrição | string |                                                         | nem sempre a UF da regional coincide com a UF do acidente, ex.:a circunscrição da SPRF-DF grande parte está localizada na UF "GO" |
| delegacia              | delegacia da PRF cujo acidente ocorreu dentro dos limites de sua circunscrição                 | string |                                                         |                                                                                                                                   |
| uop                    | unidade operacional da PRF cujo acidente ocorreu dentro dos limites de sua circunscrição       | string |                                                         | UOP = unidade operacional                                                                                                         |

Fonte: [Dicionário de variáveis de ocorrências de acidentes de trânsito no Brasil](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dicionario-acidentes) 


## Análises exploratórias

1. Top 5 causas mais comuns dos acidentes
2. Top 5 tipos mais comuns de acidentes
3. Distribuição geográfica dos acidentes
4. Relação entre número de vítimas e condições do tempo

### *Insights*

A principal causa dos acidentes está relacionada com a reação tardia ou ineficiente do condutor, e em seguida, a ausência de reação do condutor. 
Enquanto ao tipo mais comum dos acidentes é a colisão traseira. A relação que podemos deduzir entre ambos é a falta de atenção do motorista, ou também o uso de celular durante a condução.

Com relação ao mapa, podemos observar que grande parte dos acidentes se concentram na região do sul e litoral do país. 
Observação: no mapa, aparece um ponto fora da divisão entre o continente sul-americano e o oceano, isso pode ser um indicativo da presença de um dado que precisava ser tratado ou removido da base de dados.


E, por fim, a correlação linear positiva entre os dados é baixa, sendo mais perceptível entre o número de pessoas envolvidas no acidente e a quantidade de indivíduos ilesos, ou seja, quanto maior o número de pessoas presentem no acidente, maior o número de pessoas ilesas.
Também observa-se uma relação negativa entre o número de indivíduos mortos e a classificação dos acidentes.

## Instalação

Para utilizar o código com as versões de cada biblioteca utilizada para o desenvolvimento deste projeto, deve-se:
1. Criar um ambiente virtual usando:

    **conda create -n nome_ambiente python=3.x**

    ou
    
    **python -m venv venv**

    **source venv/bin/activate** (para ativação)
2. Instalar as dependências do projeto:

    **pip install -r requirements.txt**
3. Após trabalhar no projeto, usa-se o **deactivate** para desativar o ambiente virtual.