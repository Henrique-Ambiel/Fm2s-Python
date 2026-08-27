alimentos = ["Arroz", "Feijão", "Macarrão", "Carne", "Frango", "Peixe", "Ovo", "Leite", "Queijo", "Pão"]
print("Lista de alimentos:", alimentos)

novoAlimento = input("Digite o nome de um alimento para adicionar à lista: ")
alimentos.append(novoAlimento) # Adiciona o novo alimento à lista
print("Lista atualizada de alimentos:", alimentos)

alimentos.remove("Carne") # Remove "Carne" da lista
print("Lista de alimentos após remover 'Carne':", alimentos)

alimentos.sort() # Ordena a lista em ordem alfabética
print("Lista de alimentos em ordem alfabética:", alimentos)

alimentos.reverse() # Inverte a ordem da lista
print("Lista de alimentos em ordem inversa:", alimentos)

alimentos.pop() # Remove o último alimento da lista
print("Lista de alimentos após remover o último item:", alimentos)
