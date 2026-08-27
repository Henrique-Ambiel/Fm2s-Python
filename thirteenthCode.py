dados = dict()
dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

print("Dados do usuário:", dados)
print("Nome:", dados['nome'])

dados['altura'] = 1.75  # Adiciona uma nova chave 'altura' ao dicionário
print("Dados atualizados do usuário:", dados)

del dados['idade'] # Remove a chave 'idade' do dicionário
print("Dados após remover 'idade':", dados) 

dados.values()  # Retorna uma lista com os valores do dicionário
print("Valores do dicionário:", list(dados.values()))

dados.keys()  # Retorna uma lista com as chaves do dicionário
print("Chaves do dicionário:", list(dados.keys()))

dados.items()  # Retorna uma lista de tuplas (chave, valor) do dicionário
print("Itens do dicionário:", list(dados.items()))

for k, v in dados.items():  # Itera sobre os itens do dicionário
    print(f"Chave: {k}, Valor: {v}")