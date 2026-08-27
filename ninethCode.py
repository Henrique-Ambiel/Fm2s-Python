status = input("Já chegou ?")

while status != "sim": #Executa o loop enquanto a resposta for diferente de "sim"
    if status == "não":
        print("Então espere mais um pouco")
        break
    elif status == "talvez":
        print("Então espere mais um pouco")
        break
    else:
        print("Não entendi, digite sim, não ou talvez")
    status = input("Já chegou ?")
