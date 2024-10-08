# 1º passo - pedir um numero ao usuario
numero = int(input("Digite um número inteiro: ")) #int = inteiro

# 2º passo - testar se o numero é primo
if numero > 1: # se o numero foir maior que 1, ele segue. se for menor, não, pq numeros menores ou = a 1 não são primos 

    primo = True
    
# 3º passo - loop for pra testar se o numero inserido tem algum divisor entre 2 e o numero inserido -1, pq se encontrar algum divisor, ele não é primo e o for é interrompido no break
    for i in range(2, numero): # o range gera uma sequencia de - 2 até o numero escolhido. tipo, o num escolhido é 6 = range(2, 6) = [2, 3, 4, 5, 6]
        if numero % i == 0: 
            primo = False # se encontrar um divisor (i), a variavel primo vira falsa, pra dizer que não é primo, já que tem um divisor além de 1 e ele mesmo
            break  # não continua pq já encontrou um divisor e descobriu que não é primo

# 4º passo - exibe o resultado com um if/els
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print(f"{numero} não é um número primo.")  # pra numeros menores ou iguais a 1 pq não são primos
