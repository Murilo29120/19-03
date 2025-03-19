def exibir_menu():
        print("Bem-vindo ao menu de cadastro")
        print("1- Novo Cadastro")
        print("2- Ver Cadastro")
        print("3- Sair")
        print("-------------------------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    turma = input("Turma: ")  
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("Nenhum cadastro no sistema.")
    else:
        print("\n------ LISTA DE CADASTROS ------")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print("Obrigado por utilizar nosso sistema!")      
            break      
        else:
            print("Opção incorreta! Tente novamente.")

if __name__ == "__main__":
    main()

        