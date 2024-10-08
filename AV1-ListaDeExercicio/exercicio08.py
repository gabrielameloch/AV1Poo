# 1º passo - criar uma variavel p armazenar o gabarito da prova
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

# 2º passo - criar variaveis pra aramzenar os resultaod 
notas = []
totalAlunos = 0 # vai ser um contador que começa no 0

#3º passo - loop infinito que vai continuar executando o bloco de codigo embaixo dele até que uma interrupçao aconteça, como um break
while True: 
    totalAcertos = 0 #essa variavel vai ter uma iteração a cada acerto
    print(f"\n--- Aluno {totalAlunos + 1} ---") #mensagem indicando que o programa ta recebendo as respostas 
    #o totalAlunos+1 é icrementado junto com cada aluno novo que responde 
    
    # 4º passo - um loop p coletar respostas do aluno
    for i in range(10): #10 é a qtd de questoes da prova
        resposta = input(f"Digite a resposta da questão {i + 1} (A/B/C/D/E): ").upper() #o input exibe uma mensagem e espera pela resposta do usuário e o upper converte a resposta p letras maiusculas
        if resposta == gabarito[i]: #if pra verificar se a resposta do aluno ta igual ao gabarito
            totalAcertos += 1  #se o aluno acertar, ele incrementa a variavel de acerto com +1

    #5º passo - armazenar as notas do aluno
    notas.append(totalAcertos) #adiciona o numero total de acertos do aluno a uma lista de notas e a funçao append permite adicionar um novo elemento ao final de uma lista
    totalAlunos += 1  #conta quantos alunos utilizaram o sistema ate aquele momento e incrementa na variavel totalAlunos

    # 6º passo - pergunta se outro aluno vai utilizar o sistema
    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").lower() #lower converte a resposta do usuario p minusculas
    if continuar != 's': #if pra se a resposta for sim, continuar, se nao, o break pra terminar o loop
        break  


# 7º passo -  Cálculo das estatísticas
maiorAcerto = max(notas) #max e min encontra os valores maximos e minimos da lista notas
menorAcerto = min(notas)
mediaNotas = sum(notas) / totalAlunos if totalAlunos > 0 else 0 #sum é uma funçao que soma todos os elementos de um iteravel, a lista notas nesse caso, entao ele cacula a soma de todos os acertos registrados na lista


# 8º passo - printa os resultados
print("\n--- Resultados ---")
print(f"Maior Acerto: {maiorAcerto}")
print(f"Menor Acerto: {menorAcerto}")
print(f"Total de Alunos: {totalAlunos}")
print(f"Média das Notas: {mediaNotas:.2f}")
