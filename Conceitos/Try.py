# O try permite testar um bloco de código quanto a erros.
# O except permite que você lide com o erro.
# O else permite executar o código quando não há erro.
# o finally permite que você execute código, independentemente do resultado dos blocos try e except.

try:
    0 / 0
    print("Deu certo meu script")

except:
    print("Não deu certo!")

finally:
    print("Vou ser executado da mesma forma.")
