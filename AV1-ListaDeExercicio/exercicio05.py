# 1º passo - criar variavel com o preço unitario dos produtos 
precoUnitario = 1.99

# 2º passo - mostrar a tabela de preços
print("Lojas Quase Dois - Tabela de preços") #imprimi o cabeçalho da tabela

# 3º passo - usar um loop for pra os valores de 1 a 50
for quantidade in range(1, 51):  
    precoTotal = quantidade * precoUnitario  # calculo do preço total
    print(f"{quantidade} - R$ {precoTotal:.2f}")  # mostra a quantidade e o preço
    #o (:.2f) formata o preço com duas casas decimais, o padrão 

# 4º passo - solicitar a quantidade de itens comprados
quantidadeItens = int(input("\nDigite a quantidade de itens que o cliente comprou: "))
precoFinal = quantidadeItens * precoUnitario  # calculo do preço final

# 5º passo - mostrar o preço final
print(f"Total a pagar: R$ {precoFinal:.2f}")
