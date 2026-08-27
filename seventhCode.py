temperatura = float(input("Digite a temperatura em Celsius: "))

#Verifica a temperatura e exibe uma mensagem correspondente
if temperatura < 0:
    print("Está muito frio!")
elif temperatura < 15:
    print("Está frio!")
elif temperatura < 25:
    print("Está agradável!")
else:
    print("Está quente!")
