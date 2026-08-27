nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Parabéns! Você foi aprovado!")
elif media < 5: #Acrescentei uma condição para notas menores que 5, indicando reprovação direta
    print("Infelizmente você foi reprovado. Tente novamente!") 
else:
    print("Você está de recuperação!")

print("A média das notas é: " + str(media))