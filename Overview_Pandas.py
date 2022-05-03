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
