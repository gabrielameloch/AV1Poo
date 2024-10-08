#1º passo - input pra que o user diga qual número entre 1 e 10 ele quer
numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))


if 1 <= numero <= 10: #2º passo - como é só de 1 a 10, usar um if/else pra deixar no intervalo certo
    print(f"Tabuada de {numero}:")
    
# 3º passo - usar um loop for pra calcular e dar o resultado da tabuada
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Por favor, insira um número entre 1 e 10.")
# (o else é pra caso o número inserido seja fora do padrão)