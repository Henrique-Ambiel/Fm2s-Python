nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Parabéns! Você foi aprovado!")
else:
    print("Infelizmente você foi reprovado. Tente novamente!")

print("A média das notas é: " + str(media))
