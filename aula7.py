# # Cadastro do usuário
# usuarios = []
# nome = input("Digite seu nome: ")
# email = input("Digite seu email: ")
# usuarios.append({'nome': nome, 'email': email})

# # Produtos disponíveis
# produtos = ["Camiseta - R$ 50,00", "Calça - R$ 80,00", "Tênis - R$ 120,00"]
# precos = [50.0, 80.0, 120.0]
# escolhas_produto = []

# # Exibição dos produtos
# print("Produtos disponíveis:")
# for i in range(3):
#     print(f"{i + 1}. {produtos[i]}")

# # Compra de um produto
# produto_escolhido = int(input("Escolha o número do produto que deseja comprar (1-3): ")) - 1
# quantidade = int(input("Quantas unidades deseja comprar? "))
# escolhas_produto.append(produto_escolhido)

# # Cálculo do valor total
# valor_total = precos[produto_escolhido] * quantidade

# # Exibição do valor total
# print(f"Valor total da compra: R$ {valor_total:.2f}")

# # Pagamento
# forma_pagamento = input("Escolha a forma de pagamento (Cartão, Dinheiro): ")
# if forma_pagamento.lower() == "cartão":
#     print("Pagamento realizado com cartão.")
# elif forma_pagamento.lower() == "dinheiro":
#     print("Pagamento realizado em dinheiro.")
# else:
#     print("Forma de pagamento inválida.")

# # Resumo da compra
# print(f"Cliente: {usuarios[0]['nome']}, Produto: {produtos[produto_escolhido]}, Quantidade: {quantidade}, Valor Total: R$ {valor_total:.2f}")







# Cadastro de Clientes
clientes = []

# Cadastrando até 3 clientes
cliente1_nome = input("Digite o nome do Cliente 1: ")
cliente1_idade = int(input("Digite a idade do Cliente 1: "))
clientes.append((cliente1_nome, cliente1_idade))

cliente2_nome = input("Digite o nome do Cliente 2: ")
cliente2_idade = int(input("Digite a idade do Cliente 2: "))
clientes.append((cliente2_nome, cliente2_idade))

cliente3_nome = input("Digite o nome do Cliente 3: ")
cliente3_idade = int(input("Digite a idade do Cliente 3: "))
clientes.append((cliente3_nome, cliente3_idade))

# Reservas de Quartos
tipos_quarto = ["Simples", "Duplo", "Luxo"]
precos = [100, 150, 250]  # Preço por diária dos quartos

# Escolhendo o tipo de quarto para cada cliente
cliente1_quarto = input(f"Cliente 1: Escolha o tipo de quarto ({tipos_quarto}): ")
cliente2_quarto = input(f"Cliente 2: Escolha o tipo de quarto ({tipos_quarto}): ")
cliente3_quarto = input(f"Cliente 3: Escolha o tipo de quarto ({tipos_quarto}): ")

# Definindo o preço do quarto escolhido
if cliente1_quarto == "Simples":
    cliente1_preco = precos[0]
elif cliente1_quarto == "Duplo":
    cliente1_preco = precos[1]
elif cliente1_quarto == "Luxo":
    cliente1_preco = precos[2]
else:
    cliente1_preco = 0  # Quarto inválido

if cliente2_quarto == "Simples":
    cliente2_preco = precos[0]
elif cliente2_quarto == "Duplo":
    cliente2_preco = precos[1]
elif cliente2_quarto == "Luxo":
    cliente2_preco = precos[2]
else:
    cliente2_preco = 0  # Quarto inválido

if cliente3_quarto == "Simples":
    cliente3_preco = precos[0]
elif cliente3_quarto == "Duplo":
    cliente3_preco = precos[1]
elif cliente3_quarto == "Luxo":
    cliente3_preco = precos[2]
else:
    cliente3_preco = 0  # Quarto inválido

# Dias de Estadia
cliente1_dias = int(input("Quantos dias o Cliente 1 ficará no hotel? "))
cliente2_dias = int(input("Quantos dias o Cliente 2 ficará no hotel? "))
cliente3_dias = int(input("Quantos dias o Cliente 3 ficará no hotel? "))

# Cálculo do valor total da estadia
valor_cliente1 = cliente1_preco * cliente1_dias
valor_cliente2 = cliente2_preco * cliente2_dias
valor_cliente3 = cliente3_preco * cliente3_dias

# Aplicando desconto de 10% para clientes acima de 60 anos
if clientes[0][1] > 60:
    valor_cliente1 *= 0.9

if clientes[1][1] > 60:
    valor_cliente2 *= 0.9

if clientes[2][1] > 60:
    valor_cliente3 *= 0.9

# Exibindo os valores a serem pagos
print(f"\nValor a ser pago pelo Cliente 1 ({clientes[0][0]}): R$ {valor_cliente1:.2f}")
print(f"Valor a ser pago pelo Cliente 2 ({clientes[1][0]}): R$ {valor_cliente2:.2f}")
print(f"Valor a ser pago pelo Cliente 3 ({clientes[2][0]}): R$ {valor_cliente3:.2f}")












