import os

restaurantes = [{"nome": "Five guys", "categoria": "Hamburger", "ativo": True},
                {"nome": "Subway", "categoria": "Sanduiche", "ativo": False},
                {"nome": "Mangai", "categoria": "Comida Tipica", "ativo": True}]

def exibir_nome_programa():
    print("SABOR EXPRESS\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o programa")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu:")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante desejado para cadastar:")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
    dados_do_restaurante = {"nome" : nome_do_restaurante, "categoria" : categoria, "ativo" : False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("listando restaurantes:")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurente que deseja alternar o estado:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativo com sucesso" if restaurante["ativo"] else f"O restaurante foi desativado com sucesso "
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        ocpcao_escolhida = int(input("Escolha uma opção:"))
        print(f"Você escolheu a opção {ocpcao_escolhida}")

        match ocpcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
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
