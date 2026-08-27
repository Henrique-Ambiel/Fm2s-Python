import random # Importa o módulo random

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite outro nome: "))
n3 = str(input("Digite mais um nome: "))

aleatorio = (n1, n2, n3) # Cria uma tupla com os nomes digitados
escolhido = random.choice(aleatorio) # Escolhe um nome aleatoriamente da tupla
print("O nome escolhido foi: " + escolhido)