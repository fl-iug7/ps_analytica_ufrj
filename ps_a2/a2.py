# -*- coding: utf-8 -*-
"""a2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xt62MJX-4sGof1hZKPyGzi7143xGrKIp

#Bibliotecas
"""

!pip install basedosdados
import basedosdados as bd
import pandas as pd

"""#INEP - educação - 2006 à 2022"""

df_inep = bd.read_table(dataset_id='br_inep_indicadores_educacionais',
table_id='municipio',
billing_project_id="ps-a2-ufrjanalytica")

# Limitando a região do rio de janeiro
rj_df_inep = df_inep[df_inep['id_municipio'] == '3304557']

# Limitando a região total, excluindo dados específicos a áreas rurais e urbanas
rj_df_inep = rj_df_inep[rj_df_inep['localizacao'] == 'total']

useful_columns = ['ano', 'id_municipio', 'localizacao', 'rede', 'atu_ei', 'atu_ef', 'atu_em', 'had_ei', 'had_ef', 'had_em', 'tdi_ef', 'tdi_em',
                  'taxa_aprovacao_ef', 'taxa_aprovacao_em', 'taxa_reprovacao_ef', 'taxa_reprovacao_em', 'taxa_abandono_ef', 'taxa_abandono_em', 'dsu_ei', 'dsu_ef', 'dsu_em']

rj_df_inep = rj_df_inep[useful_columns]

rj_df_inep

"""##baixando dataset"""

from google.colab import files

rj_df_inep.to_csv('rj_df_inep.csv', index=False)
files.download('rj_df_inep.csv')

"""#IBGE - econômico - 2002 à 2021"""

df_ibge = bd.read_table(dataset_id='br_ibge_pib',
table_id='municipio',
billing_project_id="ps-a2-ufrjanalytica")

# Limitando a região do rio de janeiro
rj_df_ibge = df_ibge[df_ibge['id_municipio'] == '3304557']
rj_df_ibge

"""##baixando dataset"""

from google.colab import files

rj_df_ibge.to_csv('rj_df_ibge.csv', index=False)
files.download('rj_df_ibge.csv')

from google.colab import drive
drive.mount('/content/drive')

"""#IPS - social - 2016, 2018, 2020"""

df_ips = bd.read_table(dataset_id='br_rj_rio_de_janeiro_ipp_ips',
table_id='dimensoes_componentes',
billing_project_id="ps-a2-ufrjanalytica")

# Limitando a região do rio de janeiro
rj_df_ips = df_ips[df_ips['regiao_administrativa'] == 'Rio De Janeiro']

rj_df_ips

"""##baixando dataset"""

from google.colab import files

rj_df_ips.to_csv('rj_df_ips.csv', index=False)
files.download('rj_df_ips.csv')

"""#Análise

##bibliotecas
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

"""##datasets"""

rj_df_ibge = pd.read_csv('rj_df_ibge.csv')
rj_df_ibge.head()

rj_df_inep = pd.read_csv('rj_df_inep.csv')
rj_df_inep.sort_values(by='ano', inplace=True)
rj_df_inep.head()

rj_df_ips = pd.read_csv('rj_df_ips.csv')
rj_df_ips.head()

"""##obj1 : Compreender como o crescimento econômico do município do Rio de Janeiro evoluiu ao longo do tempo, e determinar qual é a relação dessa evolução com os indicadores sociais no mesmo período.

###Crescimento Econômico do Rio de Janeiro (2002 - 2021)
"""

# Plotando o crescimento do PIB ao longo do tempo
plt.plot(rj_df_ibge['ano'], rj_df_ibge['pib'], marker='o')
plt.xlabel('Ano')
plt.ylabel('PIB Municipal')
plt.title('Crescimento Econômico do Rio de Janeiro (2002 - 2021)')
plt.xticks(range(2002, 2022, 2), rotation=45)
plt.grid(True)
plt.show()

"""###Crescimento Econômico vs Componentes do IPS"""

# Selecionando features relevantes
specific_ips_data = rj_df_ips[['ano', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']]
economic_data = rj_df_ibge[['ano', 'pib']]


# Juntando os dataframes
merged_data = pd.merge(specific_ips_data, economic_data, on='ano')

# Normalizando os valores
scaler = MinMaxScaler()
merged_data[['pib', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']] = scaler.fit_transform(merged_data[['pib', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(merged_data['ano'], merged_data['pib'], label='PIB', marker='o', color='black')
plt.plot(merged_data['ano'], merged_data['necessidades_humanas_basicas_nota_dimensao'], marker='o', label='Necessidades Humanas Básicas')
plt.plot(merged_data['ano'], merged_data['fundamentos_bem_estar_nota_dimensao'], marker='o', label='Fundamentos de Bem-Estar')
plt.plot(merged_data['ano'], merged_data['oportunidades_nota_dimensao'], marker='o', label='Oportunidades')
plt.xlabel('Ano')
plt.ylabel('Valores Normalizados')
plt.title('Crescimento Econômico vs Componentes do IPS (Normalizado)')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Dimensão Necessidades Humanas Básicas
necessidades_humanas_basicas_features = ['ano', 'nutricao_cuidados_medicos_basicos', 'agua_saneamento', 'moradia', 'seguranca_pessoal']
df_necessidades_humanas_basicas = rj_df_ips[necessidades_humanas_basicas_features]


# Normalizando os dados
scaler = MinMaxScaler()
df_merged_pib_nhb = pd.merge(rj_df_ibge, df_necessidades_humanas_basicas, on='ano')
df_merged_pib_nhb[['pib'] + necessidades_humanas_basicas_features[1:]] = scaler.fit_transform(df_merged_pib_nhb[['pib'] + necessidades_humanas_basicas_features[1:]])


# Plot
plt.figure(figsize=(10, 6))
plt.plot(df_merged_pib_nhb['ano'], df_merged_pib_nhb['pib'], marker='o', label='PIB', color='black')

for feature in necessidades_humanas_basicas_features[1:]:
    plt.plot(df_merged_pib_nhb['ano'], df_merged_pib_nhb[feature], marker='o', label=feature)

plt.title('Crescimento Econômico vs Necessidades Humanas Básicas (IPS)')
plt.xlabel('Ano')
plt.ylabel('Valores Normalizados')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Dimensão Fundamentos de Bem-Estar
fundamentos_bem_estar_features = ['ano', 'acesso_conhecimento_basico', 'acesso_informacao', 'saude_bem_estar', 'qualidade_meio_ambiente']
df_fundamentos_bem_estar = rj_df_ips[fundamentos_bem_estar_features]


# Normalizando os dados
scaler = MinMaxScaler()
df_merged_pib_fbe = pd.merge(rj_df_ibge, df_fundamentos_bem_estar, on='ano')
df_merged_pib_fbe[['pib'] + fundamentos_bem_estar_features[1:]] = scaler.fit_transform(df_merged_pib_fbe[['pib'] + fundamentos_bem_estar_features[1:]])


# Plot
plt.figure(figsize=(10, 6))
plt.plot(df_merged_pib_fbe['ano'], df_merged_pib_fbe['pib'], label='PIB', marker='o', color='black')

for feature in fundamentos_bem_estar_features[1:]:
    plt.plot(df_merged_pib_fbe['ano'], df_merged_pib_fbe[feature], marker='o', label=feature)

plt.title('Crescimento Econômico vs Fundamentos de Bem-Estar (IPS)')
plt.xlabel('Ano')
plt.ylabel('Valores Normalizados')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Dimensão Oportunidades
oportunidades_features = ['ano', 'direitos_individuais', 'liberdades_individuais', 'tolerancia_inclusao', 'acesso_educacao_superior']
df_oportunidades = rj_df_ips[oportunidades_features]


# Normalizando os dados
scaler = MinMaxScaler()
df_merged_pib_opp = pd.merge(rj_df_ibge, df_oportunidades, on='ano')
df_merged_pib_opp[['pib'] + oportunidades_features[1:]] = scaler.fit_transform(df_merged_pib_opp[['pib'] + oportunidades_features[1:]])


# Plot
plt.figure(figsize=(10, 6))
plt.plot(df_merged_pib_opp['ano'], df_merged_pib_opp['pib'], label='PIB', marker='o', color='black')

for feature in oportunidades_features[1:]:
    plt.plot(df_merged_pib_opp['ano'], df_merged_pib_opp[feature], marker='o', label=feature)

plt.title('Crescimento Econômico vs Oportunidades (IPS)')
plt.xlabel('Ano')
plt.ylabel('Valores Normalizados')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

"""##obj2 : Determinar as disparidades na qualidade da educação entre diferentes tipos de redes de ensino (municipal, estadual, federal, privada) do município do Rio de Janeiro ao longo dos anos."""

# Inicialização o dataframe
matriz_df = pd.DataFrame(columns=['ano', 'rede', 'idis', 'iat', 'idcs', 'iqe'])


# Calculan e adicionan os resultados ao dataframe
for rede in ['estadual', 'federal', 'publica', 'privada', 'total']:
    subset = rj_df_inep[rj_df_inep['rede'] == rede]

    idis = ((subset['tdi_ef'] * subset['atu_ef'] + subset['tdi_em'] * subset['atu_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    iat = (((subset['atu_ef']) * subset['taxa_aprovacao_ef'] + (subset['atu_em']) * subset['taxa_aprovacao_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    idcs = ((subset['dsu_ef'] * subset['atu_ef'] + subset['dsu_em'] * subset['atu_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    iqe = [(-0.3*idis[i] + 0.6*iat[i] + 0.1*idcs[i]) / (0.3 + 0.6 + 0.1) for i in range(len(idis))]

    temp_df = pd.DataFrame({'ano': subset['ano'], 'rede': rede, 'idis': idis, 'iat': iat, 'idcs': idcs, 'iqe': iqe})
    matriz_df = pd.concat([matriz_df, temp_df], ignore_index=True)


# Ordenando em ordem cronológica
matriz_df.sort_values(by='ano', inplace=True)

# Plot
plt.figure(figsize=(10, 6))

for rede in matriz_df['rede'].unique():
    subset = matriz_df[matriz_df['rede'] == rede]
    plt.plot(subset['ano'], subset['idis'], marker='o', label=f'{rede} - IDIS')

plt.title('Índice de Distorção Idade-Série (IDIS) por tipo de rede escolar ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('IDIS')
plt.xticks(range(2007, 2023), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Plot
plt.figure(figsize=(10, 6))

for rede in matriz_df['rede'].unique():
    subset = matriz_df[matriz_df['rede'] == rede]
    subset['iat'] = subset['iat'].interpolate(method='linear')
    plt.plot(subset['ano'], subset['iat'], marker='o', label=f'{rede} - IAT')

plt.title('Índice de Aproveitamento Total (IAT) por tipo de rede escolar ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('IAT')
plt.xticks(range(2007, 2023), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Plot
plt.figure(figsize=(10, 6))

for rede in matriz_df['rede'].unique():
    subset = matriz_df[matriz_df['rede'] == rede]
    plt.plot(subset['ano'], subset['idcs'], marker='o', label=f'{rede} - IDCS')

plt.title('Índice de Docentes com Curso Superior (IDCS) por tipo de rede escolar ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('IDCS')
plt.xticks(range(2011, 2023), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Plot
plt.figure(figsize=(10, 6))

for rede in matriz_df['rede'].unique():
    subset = matriz_df[matriz_df['rede'] == rede]
    subset['iqe'] = subset['iqe'].interpolate(method='linear')
    plt.plot(subset['ano'], subset['iqe'], marker='o', label=f'{rede} - IQE')

plt.title('Índice de Qualidade do Ensino (IQE) por tipo de rede escolar ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('IQE')
plt.xticks(range(2011, 2023), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

"""##obj3 : Correlacionar os índices de progresso social com os indicadores educacionais no município do Rio de Janeiro nos últimos anos."""

# Inicialização o dataframe
matriz_df = pd.DataFrame(columns=['ano', 'rede', 'idis', 'iat', 'idcs', 'iqe'])


# Calculan e adicionan os resultados ao dataframe
for rede in ['estadual', 'federal', 'publica', 'privada', 'total']:
    subset = rj_df_inep[rj_df_inep['rede'] == rede]

    idis = ((subset['tdi_ef'] * subset['atu_ef'] + subset['tdi_em'] * subset['atu_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    iat = (((subset['atu_ef']) * subset['taxa_aprovacao_ef'] + (subset['atu_em']) * subset['taxa_aprovacao_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    idcs = ((subset['dsu_ef'] * subset['atu_ef'] + subset['dsu_em'] * subset['atu_em']) / (subset['atu_ef'] + subset['atu_em'])).tolist()
    iqe = [(-0.3*idis[i] + 0.6*iat[i] + 0.1*idcs[i]) / (0.3 + 0.6 + 0.1) for i in range(len(idis))]

    temp_df = pd.DataFrame({'ano': subset['ano'], 'rede': rede, 'idis': idis, 'iat': iat, 'idcs': idcs, 'iqe': iqe})
    matriz_df = pd.concat([matriz_df, temp_df], ignore_index=True)


# Ordenando em ordem cronológica
matriz_df.sort_values(by='ano', inplace=True)

features_IDIS = ['ano', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']


# Juntando os dataframes
rj_df_ips_scaled = pd.merge(rj_df_ips[features_IDIS], matriz_df[matriz_df['rede'] == 'total'],  on='ano')


# Corrigindo a lista de features
features_IDIS[0] = 'idis'


# Normalizando os dados
scaler = MinMaxScaler()
rj_df_ips_scaled[features_IDIS] = scaler.fit_transform(rj_df_ips_scaled[features_IDIS])


# Plot
plt.figure(figsize=(10, 6))

for feature in features_IDIS:
    plt.plot(rj_df_ips_scaled['ano'], rj_df_ips_scaled[feature], marker='o', label=feature)

plt.title('Índice de Distorção Idade-Série (IDIS)')
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

features_IAT = ['ano', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']


# Interpolando os valores faltantes
x = matriz_df[matriz_df['rede'] == 'total']
x.loc[:, 'iat'] = x['iat'].interpolate(method='linear')


# Juntando os dataframes
rj_df_ips_scaled = pd.merge(rj_df_ips[features_IAT], x,  on='ano')


# Corrigindo a lista de features
features_IAT[0] = 'iat'


# Normalizando os dados
scaler = MinMaxScaler()
rj_df_ips_scaled[features_IAT] = scaler.fit_transform(rj_df_ips_scaled[features_IAT])


# Plotando as séries temporais para cada índice educacional
plt.figure(figsize=(10, 6))

for feature in features_IAT:
    plt.plot(rj_df_ips_scaled['ano'], rj_df_ips_scaled[feature], marker='o', label=feature)

plt.title('Índice de Aproveitamento Total (IAT)')
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

features_IDCS = ['ano', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']


# Juntando os dataframes
rj_df_ips_scaled = pd.merge(rj_df_ips[features_IDCS], matriz_df[matriz_df['rede'] == 'total'],  on='ano')


# Corrigindo a lista de features
features_IDCS[0] = 'idcs'


# Normalizando os dados
scaler = MinMaxScaler()
rj_df_ips_scaled[features_IDCS] = scaler.fit_transform(rj_df_ips_scaled[features_IDCS])


# Plotando as séries temporais para cada índice educacional
plt.figure(figsize=(10, 6))

for feature in features_IDCS:
    plt.plot(rj_df_ips_scaled['ano'], rj_df_ips_scaled[feature], marker='o', label=feature)

plt.title('Índice de Docentes com Curso Superior (IDCS)')
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()

features_IQE = ['ano', 'necessidades_humanas_basicas_nota_dimensao', 'fundamentos_bem_estar_nota_dimensao', 'oportunidades_nota_dimensao']


# Interpolando os valores faltantes
x.loc[:, 'iqe'] = x['iqe'].interpolate(method='linear')


# Juntando os dataframes
rj_df_ips_scaled = pd.merge(rj_df_ips[features_IQE], x,  on='ano')


# Corrigindo a lista de features
features_IQE[0] = 'iqe'


# Normalizando os dados
scaler = MinMaxScaler()
rj_df_ips_scaled[features_IQE] = scaler.fit_transform(rj_df_ips_scaled[features_IQE])


# Plotando as séries temporais para cada índice educacional
plt.figure(figsize=(10, 6))

for feature in features_IQE:
    plt.plot(rj_df_ips_scaled['ano'], rj_df_ips_scaled[feature], marker='o', label=feature)

plt.title('Índice de Qualidade do Ensino (IQE)')
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.xticks(range(2016, 2021), rotation=45)
plt.grid(True)
plt.legend()
plt.show()