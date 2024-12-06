#ler entradas do usuário
alunos = []
while True:
    
    escolha_menu = int(input("Escolha um menu:")) #variavel que guarda a escolha do usuario
    if escolha_menu == 1: #se a escolha for para realizar u
        
        cont = 0
        escolha_usuario = int(input("Deseja calcular a média de quantos alunos?")) #variavel que guarda quantas vezes o codigo vai rodar
        while cont < escolha_usuario:
            nome = (input("Digite o nome do aluno:")) #ARMAZENAR o nome do aluno
            
            nota1 = float(input("Digite a nota 1 do aluno:")) #4 notas do aluno
            nota2 = float(input("Digite a nota 2 do aluno:"))
            nota3 = float(input("Digite a nota 3 do aluno:"))
            nota4 = float(input("Digite a nota 4 do aluno:"))

            faltas = int(input("Digite a quantidade das faltas:"))
            #calculo da média
            media = (nota1+nota2+nota3+nota4)/4
            print(media)

            #logica da situação
            if faltas > 31:
                situacao = "Rprovado por falta"
            elif media >= 8:
                situacao = "Aprovado"
            elif media >= 5: #Recuperação
                recuperacao = float (input("Digite a nota recuperacao:")) #Ler a nota da prova de recuperação
                if recuperacao >=(10-media):
                    situacao = "Aprovado na recuperação"
                else:
                    situacao = "Reprovado na recuperação "
            else:
                situacao = "Reprovado por média"
                #enviar os dados do aluno para a lista alunos 
            alunos.append([nome , faltas , media , situacao])
            cont += 1
    elif escolha_menu == 2: #Relatorio
        print(alunos)
    elif escolha_menu == 3: #se o usúario escolheu encerrar
        break #Quebra a execução enquanto