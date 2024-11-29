def calcularmedia(notas): #calcular a média dos aluno
    return sum(notas) / len(notas) #receber uma lista de notas e retorna a média,
def situacaoaluno(media,faltas) :
    if faltas > 20: #se o aluno tiver mais de 20 faltas ele será reprovado
        return "Reprovado pro falta"
    elif media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação" 
    else:
        return "Reprovado"
def gerarrelatorio (num_alunos):
    alunos =[]
    for i in range(num_alunos):
        print(f"\nAluno {i+1}:")
        nome = input("Digite o nome do aluno: ")
        faltas = int(input("Digite o número de faltas: "))
        notas = []
        for j in range(4):
            nota = float(input(f"Digite a nota do {j+1}º bimestre:"))
            notas.append(nota)
            media = calcularmedia(notas)
            situacao = situacaoaluno(media,faltas)
            aluno = { 
                 "nome": nome,
                 "faltas": faltas,
                 "notas": notas,
                 "media": media,
                 "situacao": situacao,
             }
            alunos.append(aluno)
        print("\nRelatório final:")
        print(f"{'nome'} :<20 {'faltas' :<7} {'media' :<6} {'situacao'}")
        print("-" * 50)
        for aluno in alunos:
            print(f"{aluno['nome']:<20} {aluno['faltas']:<7} {aluno['media']:<6.2f} {aluno['situacao']}")
def main():
    