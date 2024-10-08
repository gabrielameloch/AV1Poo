# 1º passo - definir variaveis das populaçoes, da taxa de crescimento de cada país e os anos 
populationA = 80000  
taxaCrescimentoA = 0.03  # 3% de crescimento em fraçao

populationB = 200000  
taxaCrescimentoB = 0.015  # 1.5% em fraçao

years = 0  # é o contador de anos que começa em zero
#esse contador é pra contar quantos anos se passaram até que a populaçao A ultrapassasse a do pais B

# 2º passo -  usar o loop while 
while populationA < populationB: # o loop continua enquanto a população do pais A for menor que a do pais B
    populationA += populationA * taxaCrescimentoA  # atualiza a população do país A usando a formula do crescimento = (populationA += populationA * taxaCrescimentoA)
    populationB += populationB * taxaCrescimentoB  # atualiza a população B do mesmo jeito
    years += 1  # a cada iteração, adiciona o contador de anos em +1

# 3º passo - exibir o resultado 
print(f"Serao necessarios {years} anos para que a populacao do Pais A ultrapasse ou iguale a populacao do Pais B.")


# as populações vão continuar sendo atualizadas até que a condiçao seja alcançada
# que no caso é ate que a população A seja maior ou igual a populaçao B