# 1º passo - definir uma variavel p numeros pares e outra p numero impares
numPar= 0
numImpar = 0

# 2º passo - usar um for p pedir os dez numeros ao usuario
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
# 3º passo - usar um if/else pra descobrir se o numero é par ou impar, e usar os operadores aritméticos
    if numero % 2 == 0: # "se o resto da divisão do numero por 2 for igual a 0 = ele é par"
        numPar += 1  # aqui o incremeto de +1 é pra caso o numero for par, ele é add na variavel de numPares e aparece na contagem final
    else:
        numImpar+= 1  # mesma coisa do par

# printa os resultados
print(f"Quantidade de números pares: {numPar}")
print(f"Quantidade de números ímpares: {numImpar}")
