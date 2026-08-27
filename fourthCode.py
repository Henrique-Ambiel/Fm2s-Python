eu = float(input("Digite o valor da sua comanda: "))
amigo = float(input("Digite o valor da comanda do seu amigo: "))

total = (eu + amigo) / 2
print('O valor total da comanda é: R$ {:.2f}'.format(total)) #Formatação de casas decimais