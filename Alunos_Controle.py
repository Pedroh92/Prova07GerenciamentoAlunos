import Dados_Alunos as ga

def menu():
    """Exibe o menu e gerencia as opções do usuário."""
    while True:
        print("\n=== Menu de Gerenciamento de Alunos ===")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            ga.Adicionar_Aluno()
        elif opcao == '2':
            ga.Remover_Aluno()
        elif opcao == '3':
            ga.Atualizar_Aluno()
        elif opcao == '4':
            ga.Ver_Alunos()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
    

