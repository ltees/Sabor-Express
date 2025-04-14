import os

def exibir_nome_programa():
    print("SABOR EXPRESS\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando o programa")

def opcao_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal:")
    main()

def escolher_opcao():
    try:
        ocpcao_escolhida = int(input("Escolha uma opção:"))
        print(f"Você escolheu a opção {ocpcao_escolhida}")

        match ocpcao_escolhida:
            case 1:
                print("Adicionar restaurante")
            case 2:
                print("Listar restaurante")
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case 5:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
