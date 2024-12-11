##DECLARAR UMA FUNÇÃO
def saudacoes(Hora_do_Dia): #Exibir a saudação correspondente a hora do dia
    #DAR BOM DIA
    if (Hora_do_Dia >= 0) and (Hora_do_Dia <=12):
        print("Bom Dia!")
    elif (Hora_do_Dia >= 13) and (Hora_do_Dia <= 18):
        print("Boa Tarde!")
    elif (Hora_do_Dia >= 19) and (Hora_do_Dia <=23):
        print("Boa Noite!")

#FORA DE FUNÇÃO
#peço para o usuário dizer a hora atual
resposta = int(input("Digite que horas são: \n"))
#chamo a função passando para ela o parametro obrigatorio
saudacoes(resposta)