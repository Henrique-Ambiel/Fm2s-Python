altura = input("Qual é a sua altura? ")
peso = float(input("Qual é o seu peso? "))
imc = peso / (float(altura) ** 2)

print("A sua altura é " + altura + " e o seu peso é " + str(peso) + " kg.")
print("O seu IMC é: " + str(imc))