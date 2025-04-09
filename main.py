def funcao1():
    pass

def funcao2():
    pass

def funcao3():
    pass

def sair():
    print("Saindo...")
    exit()

def menu():
    opcoes = {
        "1": funcao1,
        "2": funcao2,
        "3": funcao3,
        "4": sair
    }

    while True:
        print("\n==== MENU ====")
        print("1. funcao1")
        print("2. funcao2")
        print("3. funcao3")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")