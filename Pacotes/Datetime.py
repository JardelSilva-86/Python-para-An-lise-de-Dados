# Pacote Datetime

type( '01/01/2022')
str

type( 01/01/2022 )


import datetime

dia_hoje = datetime.datetime.today()
print( dia_hoje )

type( dia_hoje )

2022-04-26 17:41:33.638956
datetime.datetime

print( datetime.datetime.today().date() )
2022-04-26

data = datetime.datetime.today().date()

ano = data.year
mes = data.month
dia = data.day

print( ano, mes, dia )
2022 4 26

data_antiga = datetime.date(2022, 1, 22)
data_antiga
datetime.date(2022, 1, 22)

# Diferença entre as datas
data - data_antiga

datetime.timedelta(days=94)

data.strftime( '%d/%m/%y' )
26/04/22

# Somando datas
data + datetime.timedelta(days=100)
datetime.date(2022, 8, 4)
