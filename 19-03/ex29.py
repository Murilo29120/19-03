def exibir_menu():
        print("Bem vindo ao menu de cadastro")
        print("1- Novo Cadastro")
        print("2- Ver Cadastro")
        print("3- Sair")
        print("-------------------------------------------")

def cadastrar_pessoa (cadastrado):
        nome= input("nome:")
        idade= input("idade:")
        curso= input("curso:")
        cadastros.append({"nome": nome, "Idade": idade,"Turma":turma, "Curso": curso})
        print("Cadastro realizado com sucesso!")


        def ver_cadastros(cadastros):
            if not cadastros:
                print("Nenhum cadastro no sistema.")
            else:
                print("\n------ LISTA DE CADASTROS------")
                for i, pessoa in enumerate (cadastros, 1):
                    print(F"{i}. Nome:{pessoa['Nome']}, Idade:
{pessoa ['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']})


def main():
    cadastros= []
    while True:
        exibir_menu ()
        opção= input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa(cadastros)
        elif opção == "2":
            ver_cadastros(cadastros)
        elif opção == "3":
            print("Obrigado por utilizar nosso sistemas!")      
            break      
        