#cadastro de úsuario e senha 
#menu principal
#DECLARAR FUNÇÃO
def validar_senha ():
    senha_validar = input("Digite sua senha")
    if senha_validar == senha:
        return True #RETORNA VERDADEIRO
    
saldo = 0.0 #variavel que guardará o saldo do usuário
while True:
    print("Bem vindo! \n Digite 1.cadastrar 2.login 3.encerrar")
    #LER A ESCOLHA DO USUÀRIO
    escolha_menu = int(input()) #Lê a escolha com um número 

    #Se usuário escolher cadastro
    if escolha_menu == 1:
        #Cria um usuario
        usuario = input("Crie um nome de usário:")
        senha = input("Crie uma senha:")
    elif escolha_menu == 2: #se usuário escolher login
        #Comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuário:")
        login_senha = input("Digite sua senha:")
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM SUCESSO")
            #Se LOGIN CORRETO, ENTRA NO
            #MENU PRINCIPAL DO APP  
            print("Bem Vindo", usuario)
            while True: #ENQUANTO QUE EXIBIRÁ O MENU PRINCIPAL
                print("1.Deposito 2.Sacar 3.pix 4.extrato 5.Encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: #se suário escolher deposito
                    #LÊ O VALOR A SER DEPOSITADO
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #ATUALIZAR O VALOR
                elif escolha_principal == 2: #SAQUE
                    valor_saque = float(input("Digite o valor do saque:"))
                    senha_saque = input("Digite a seua senha:")
                    if validar_senha(validar_senha): #se se
                        saldo = saldo - valor_saque #SUBTRAI O VALOR DO SALDO
                    else:
                        print("Senha incorreta")
                elif escolha_principal == 3: #SE USUÁRIO ESCOLHER PIX 
                     valor_pix = float(input("Digite o valor pix:"))
                     if validar_senha():
                        saldo = saldo - valor_pix
                     else:
                        print("Senha incorreta")
                elif escolha_principal == 4: #Se usuário 
                    if validar_senha():
                        print("EXtrato:", saldo)
                    else:
                        print("Senha incorreta")
                elif escolha_principal == 5: #encerrar
                    senha_encerrar =  input("Digite a sua senha")
                    if validar_senha():
                        break
                    else: 
                        print("Senha incorreta")
        else: 
            print("USUÁRIOOU SENHA INCORRETOS")