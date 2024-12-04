#ler entradas do usuário
alunos = []
cont = 0
escolha_usuario = int(input("Deseja calcular a média de quantos alunos?")) #variavel que guarda quantas vezes o codigo vai rodar
while cont < escolha_usuario:
    nome = (input("Digite o nome do aluno")) #ARMAZENAR o nome do aluno
    
    nota1 = float(input("Digite a nota 1:")) #4 notas do aluno
    nota2 = float(input("Digite a nota 2:"))
    nota3 = float(input("Digite a nota 3:"))
    nota4 = float(input("Digite a nota 4:"))

    faltas = int(input("Digite a quantidade das faltas:"))
    #calculo da média
    media = (nota1+nota2+nota3+nota4)/4

    #logica da situação
    if faltas > 31:
        situacao = "Rprovado por falta"
    elif media >= 8:
        situacao = "Aprovado"
    elif media >= 5: #Recuperação
        recuperacao = float (input("Digite a nota recuperacao")) #Ler a nota da prova de recuperação
        if recuperacao >=(10-media):
            situacao = "Aprovado na recuperação"
        else:
            situacao = "Reprovado na recuperação "
    else:
        situacao = "Reprovado por média"
        #enviar os dados do aluno para a lista alunos 
    alunos.append([nome , faltas , media , situacao])
        #Relatorio
       # print("Nome:", nome)
       # print("Notas:", nota1, nota2, nota3, nota4)
        #print("Faltas:", faltas)
        #print("Média:", media)
        #print("Situação:", situacao)
    cont = cont + 1
print(alunos)