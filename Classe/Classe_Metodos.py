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
