''' 
Estrutura Loop For

O loop For do Python é usado para travessia sequencial,ou seja, é usado para iterar sobre um iterável como string, lista, tupla e etc. Ele se enquadra na categoria de iteração definida. Iterações significam que o número de repetições é especificado explicitamente com antecedência.

for <iterável> in <objeto>:
'''

# Itera os números em um range de 0 a 9 
for QualquerCoisaQueVcQuiser in range( 10 ):
    print( QualquerCoisaQueVcQuiser )

# Itera os números em um range de 1 a 9
for QualquerCoisaQueVcQuiser in range( 1, 10 ):
    print( QualquerCoisaQueVcQuiser )
   
# Itera os números em um range de 1 a 100 pulando de 5 em 5
for QualquerCoisaQueVcQuiser in range( 1, 100, 5 ):
    print( QualquerCoisaQueVcQuiser )

# Criando uma lista de países
Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'Colômbia', 'Equador', 'Bolívia']

# Itera todos os elementos da lista
for QualquerCoisaQueVcQuiser in Lista:
    print( QualquerCoisaQueVcQuiser )

# Deixar todos os elementos da lista em maiúsculas
for QualquerCoisaQueVcQuiser in Lista:
    print( QualquerCoisaQueVcQuiser.upper() )

# Abrevia os elementos somente nas 3 primeiras letras
for QualquerCoisaQueVcQuiser in Lista:
    print( QualquerCoisaQueVcQuiser.upper()[0:3] )

# Criando uma condição if e percorrendo a lista
for Pais in Lista:
    
    if Pais == 'Brasil':
      print( Pais, 'é Penta Campeão mundial!!' )
    
    elif Pais == 'Argentina': 
      print( Pais, 'é Bi campeã mundial!!' )

    elif Pais == 'Uruguai':
      print( Pais, 'é Bi campeão mundial!!')
    
    else:
      print( Pais, 'não tem título mundial!')
        
        
        
        
        
        
        
        
        
        
