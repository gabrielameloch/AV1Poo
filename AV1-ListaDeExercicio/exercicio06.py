#lembra a resolução da questão 04 

# 1º passo - definir as variaveis 
salarioInicial = 1000.0  
anoDeContratacao = 1995 
anoFinal = 2025  
percentualDeAumento = 1.5 / 100  #1,5% convertido p fraçao

#2º passo - calcular o salário ano a ano
salarioAtual = salarioInicial

# 3º passo - usar um loop for para calcular o salario de 1996 até 2025
for ano in range(anoDeContratacao + 1, anoFinal + 1): #esse loop ve os anos de 1996 ate 2025 e a cada iteraçao, o salario é atualizado de acordo com o percentual do ano
    salarioAtual += salarioAtual * percentualDeAumento  #pra cada ano, o salario atual é aumnetado com o valor do aumento e o aumento é calculado multiplicando o salario atual pelo percentual de aumento daquele ano 
    print(f"Salário em {ano}: R$ {salarioAtual:.2f}")  # exibe o salário do ano
    percentualDeAumento *= 2  #já que a partir de 1997 o percentual dobra a cada ano, esse operador multiplica o percentual por 2 p o proximo ano e assim por diante

#4º passo - printar o salario final
print(f"\nO salário do funcionário em {anoFinal} será: R$ {salarioAtual:.2f}") #lembra que 2f serve p formatar com duas casas decimais 
