''' 
Estrutura Loop For

O loop For do Python é usado para travessia sequencial,ou seja, é usado para iterar sobre um iterável como string, lista, tupla e etc. Ele se enquadra na categoria de iteração definida. Iterações significam que o número de repetições é especificado explicitamente com antecedência.

for <iterável> in <objeto>:
'''

for QualquerCoisaQueVcQuiser in range( 10 ):
    print( QualquerCoisaQueVcQuiser )
    
for QualquerCoisaQueVcQuiser in range( 1, 10 ):
    print( QualquerCoisaQueVcQuiser )
    
for QualquerCoisaQueVcQuiser in range( 1, 10, 5 ):
    print( QualquerCoisaQueVcQuiser )

Lista = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']

for QualquerCoisaQueVcQuiser in Lista:
    print( QualquerCoisaQueVcQuiser )
