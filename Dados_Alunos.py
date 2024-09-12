alunos ={}



# Funcao para adicionar o aluno
def Adicionar_Aluno():
    matricula = input("Digite a Matrícula do Aluno: ")
    nome = input("Digite o nome do Aluno: ")

    if matricula in alunos:
        print("Matrícula já existente. Use outra matrícula.")
    else:
        alunos[matricula] = nome
        print(f"Aluno {nome} com matrícula {matricula} adicionado com sucesso!")

    


#Funcao para remover o aluno
def Remover_Aluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")

    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} com matrícula {matricula} foi removido com sucesso!")
    else:
        print(f"Matrícula {matricula} não encontrada.")
    




# Funcao para atualizar os alunos
def Atualizar_Aluno():
    matricula = input("Digite o número de matrícula do aluno que deseja atualizar: ")
    
    if matricula in alunos:
        novo_nome = input(f"Digite o novo nome do aluno com matrícula {matricula}: ")
        alunos[matricula] = novo_nome
        print(f"O nome do aluno foi atualizado para {novo_nome}.")
    else:
        print(f"Matrícula {matricula} não encontrada.")


def Ver_Alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos cadastrados:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")