def somaImposto(valor, taxa):
    return valor + (valor * taxa / 100)

valor = float(input("Digite o valor: "))
taxa = float(input("Digite a taxa de imposto (em %): "))
print(f"O valor com imposto é: {somaImposto(valor, taxa)}")