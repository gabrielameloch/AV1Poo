# 1º pass - pedir o valor da divida ao usuário
dividaInicial = float(input("Informe o valor da dívida: R$ ")) #o float converte o valor da divida pra um valor numerico

# 2º passo - variavel que armazena as porcentagens de juros de acordo com a qtd de parcelas
tabelaJuros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

#3º passo - cabeçalho da tabela 
print(f"{'Dívida':<15}{'Juros (%)':<12}{'Parcelas':<15}{'Valor da Parcela':<20}")
print("-" * 60) 

#esse 3º passo é pra formatar e mostrar a tabela de forma fácil de entender
#o f"{} é uma f-string que formata strings, e dentro das chaves pode ser inserido variaveis
#dívida é o texto que vai ser exibidio e :<15 define que o texto vai ser alinhado a esquerda e vai ocupar 15 espaços de largura
#juros(%) vai ser o titulo da coluna de juros e assim o resto
#o "-" * 60 imprime um separador pra deixar a tabela mais clara


# 4º passo - loop p calcular a dívida com diferentes números de parcelas
for parcelas, juros in tabelaJuros.items():
    valorJuros = (juros / 100) * dividaInicial
    dividaTotal = dividaInicial + valorJuros
    valorParcela = dividaTotal / parcelas
    
    #5º passo - printar os valores na tabela
    print(f"R$ {dividaTotal:<13.2f}{juros:<12}{parcelas:<15}R$ {valorParcela:<.2f}")
