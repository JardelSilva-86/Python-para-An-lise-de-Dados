''' 
Funções 
É um bloco de código que só é executado quando é chamado.
Você pode passar dados conhecidos como parâmetros para uma função.
Uma função pode retornar dados como resultado.
'''

def Boas_Vindas():
  print('Olá! Tudo bem? Seja bem vindo!')

Boas_Vindas()

# Soma
def Somar(a, b):
  Soma = a + b
  print(Soma)
  
x = 60
y = 65
Somar(x, y)

for loop in range (0, 11):
  
  import random

  w = random.randint(0, 11)
  z = random.randint(0, 11)

  print(w, z)
  Somar(w, z)
