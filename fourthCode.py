eu = float(input("Digite o valor da sua comanda: "))
amigo = float(input("Digite o valor da comanda do seu amigo: "))

total = (eu + amigo) / 2
print('O valor total da comanda é: R$ {:.2f}'.format(total)) #Formatação de casas decimais

#Operadores de comparação
print (eu == amigo) #Verifica se os valores são iguais
print (eu != amigo) #Verifica se os valores são diferentes
print (eu > amigo) #Verifica se o valor da comanda do usuário é maior que a do amigo
print (eu < amigo) #Verifica se o valor da comanda do usuário é menor que a do amigo
print (eu >= amigo) #Verifica se o valor da comanda do usuário é maior ou igual que a do amigo
print (eu <= amigo) #Verifica se o valor da comanda do usuário é menor ou igual que a do amigo

#Operadores lógicos
print (eu > 50 and amigo > 50) #Verifica se ambos os valores
print (eu > 50 or amigo > 50) #Verifica se pelo menos um dos valores é maior que 50