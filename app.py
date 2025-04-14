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

def escolher_opcao():
    ocpcao_escolhida = int(input("Escolha uma opção:"))
    print(f"Você escolheu a opção {ocpcao_escolhida}")

    if ocpcao_escolhida == 1:
        print("cadastrar restaurante")
    elif ocpcao_escolhida == 2:
        print("Listar restaurante")
    elif ocpcao_escolhida == 3:
        print("Ativar restaurante")
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
  
