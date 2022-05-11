# Overview do Pandas

# Vamos anaçisar a performance de estudantes usando o Pandas.

import pandas as pd
import numpy as np

# Utilizando o Google Colab
df = pd.read_csv('/content/StudentsPerformance.csv')

# Tipo da variável
type( df )

# As 5 primeiras linhas
df.head()

# As 5 últimas linhas
df.tail()

# Quantidade de linhas e colunas
df.shape

# Retornar um array com o nome das colunas
df.columns

# Verificar linhas duplicadas e somá-las
df.duplicated().sum()

# Retornar informações genéricas sobre o df
df.info()

# Retornar a quantidade de valores missing/Not a Number(NaN) e somá-los
df.isna().sum()

# Retornar um sumário estatístico
df.describe()

# Retornar um sumário estatístico para variáveis categóricas
df.describe(include = 'all')

# Quantidade de valores únicos em cada coluna
df.nunique()

# Valores únicos da coluna nível de educação do pais
df['parental level of education'].unique()

# Valores únicos da coluna raça/etnia
df['race/ethnicity'].unique

# Frequência entre a coluna parenthal level of education
df['parenthal level of education'].values_counts()

# Criando uma lista das notas
notas = ['math score', 'reading score', 'writing score']

# Organizando o dataset pela coluna 'math score' e reiniciando o índice
df.sort_values(['math score']).reset_index(drop = True)

# Organizando por todas as notas pela maior nota.
df = df.sort_values(by = notas, ascending = False)\.reset_index(drop = True)

# Exibindo o data frame
df

# Criando a coluna 'mean' com os valores médios das notas
df['mean'] = df[notas].mean(axis = 1)

# Exibindo as 5 primeiras linhas
df.head()

Criando um consulta (query)
# Preciso de alunos que sejam Masculinos, que não fizeram o teste preparatório e tiveram nota >= 70
df.query('(gender == "male") & (`test preparation course` == "none") & (`math score` >= 70)')

# Essa query retorna o mesmo resultado que anterior
df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)

# Essa query retorna o mesmo resultado que as anteriores
df.loc[(df.gender == 'male') & (df['test preparation course' == 'none']) & (df['math score'] >= 70)]   

 # Agrupamento - agrupa os dados por gênero e obtém estatíticas descritivas
df.groupby(by = 'gender')[notas].agg([np.mean, np.median]).T # .T é para transport o resultado
   
   
