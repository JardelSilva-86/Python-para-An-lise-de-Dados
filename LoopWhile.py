'''
Loop While 

O loop While é utilizado para executar um bloco de instruções até que uma determinada condição seja satisfeita. E quando a condição se torna falsa, a linha imediatamente após o programa é executada. O loop While se enquadra na categoria de iteração indefinida. A iteração indefinida significa que o número de vezes que o loop é executado não é específicada explicitamente com antecedência.

Sintaxe:
While <expressao>
  <Realize o loop>
'''

# Joguinho

while True:

  Eu = randint( 0, 10 )
  vc = randint( 0, 10 )

  print( 'Eu tirei o valor ', Eu)
  print( 'Vc tirou o valor ', vc)

  if Eu > vc:
    print( 'Eu ganhei!!!' )
    break
  
  print('\n')

# Vai continuar executando até que a consição seja falsa
Parar = 0

while Parar <= 10:
  print( Parar )
  Parar += 1
