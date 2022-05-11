# Python é uma linguagem de programação orientada a objetos.
# Quase tudo em Python é um objeto, com suas propriedades e métodos. 
# Uma classe é como um construtor de objetos, ou um "projeto" para criar objetos.

class Pessoa:

    # Método Construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade
    
    def boas_vindas(self):
        print("Olá seja bem vindo: ", self.Nome)

    def Recusado(self):
        print("Seu acesso foi recusado!")

    # Função
    def maior_idade(self):
        if self.Idade >= 18:
            print("Usuário é maior de idade.")
            self.boas_vindas()
        
        else:
            print("Usuário é menor de idade.")
            self.Recusado()

dados = Pessoa('Jardel', 30)

dados.maior_idade()
# Resultado
Usuário é maior de idade.
Olá seja bem vindo:  Jardel

    
# Criando a classe Car
class Car:
    speed = 0
    started = False
    
    def star(self):
        self.stared = True
        print("Car started, let's ride!")
        
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vroooooooom!')
        else:
            print("You need to start the car first")
    
    def stop(self):
        self.speed = 0
        print('Halting')

# Atribuindo a classe Car() à variável car
car = Car()

# Iniciando o programa com o método increase_speed
car.increase_speed(10)
# retorno 
'You need to start the car first'

# Começando o program corretamente
car.start()
# retorno
"Car started, let's ride!"

# Aumentando a velocidade
car.increase_speed(50)
# retorno
"Vroooooooom!"
