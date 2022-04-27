'''
Instruções de controle - Break ou Continue

O uso de loops no Python automatiza e repete as tarefas de maneira efeciente. Mas, às vezes, pode surgir uma condição em que você deseja sair completmentedo loop, pular uma iteração ou ignorar essa condição. Isso pode ser feito por instruções de controle de loop. As instruções de controle de loop alteram a execução de sua sequência normal. Quando a execução sai de um escopo, todos os objetos automáticos que foram criados nesse escopo são destruídos. Python suporta as seguintes instruções de controle. 
'''

# BREAK - Interrompe o programa quando ele chegar na condição informada.

Lista = ['Morango', 'Pera', 'Uva', 'Abacaxi']

for fruta in Lista:
  print ( fruta )
  if fruta == 'Pera':
    break
    

# CONTINUE - Pula a iteração informada na condição.

for Loop in  range ( 0, 11 ):
  if Loop == 5:
    continue
    print( 'Cheguei aqui mais vou ser ignorado!' )

  print( Loop )
