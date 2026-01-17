import os

livros = [
    {"titulo": "Dom Casmurro", "genero": "Clássico", "disponivel": False},
    {"titulo": "Neuromancer", "genero": "Ficção Científica", "disponivel": False},
    {"titulo": "O Hobbit", "genero": "Fantasia", "disponivel": True},
]

def nome_app():
    print("""
        ＬｉｔＦｌｏｗ
        """)

def opcoes_app():
    print("Escolha uma das opções abaixo:\n")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Alterar disponibilidade do livro")
    print("4. Sair\n")

def finalizando_app():
    os.system("cls")
    exibir_subtitulo("Finalizando o LitFlow...")

def volta_menu():
    input("Pressione Enter para voltar ao menu ")
    main()

def opcao_invalida():
    os.system("cls")
    print("Opção inválida. Por favor, escolha uma opção válida.\n")
    volta_menu()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_livro():
    exibir_subtitulo("Cadastro de novos livros")
    titulo_livro = input("Digite o título do livro: ")
    genero_livro = input("Digite o gênero do livro: ")
    livros.append({"titulo": titulo_livro, "genero": genero_livro, "disponivel": False})
    print(f"Livro '{titulo_livro}' cadastrado com sucesso!\n")
    volta_menu()

def listar_livros():
    exibir_subtitulo("Listando livros")
    print(f"{'Título do livro'.ljust(25)} {'Gênero'.ljust(20)} {'Status'}")
    for livro in livros:
        titulo = livro["titulo"]
        genero = livro["genero"]
        status = "disponível" if livro["disponivel"] else "indisponível"
        print(f"- {titulo.ljust(25)} {genero.ljust(20)} {status}")
    volta_menu()

def alterar_disponibilidade():
    exibir_subtitulo("Alterar disponibilidade do livro")
    titulo_livro = input("Digite o título do livro que deseja alterar a disponibilidade: ")
    livro_encontrado = False

    for livro in livros:
        if titulo_livro == livro["titulo"]:
            livro_encontrado = True
            livro["disponivel"] = not livro["disponivel"]
            mensagem = (
                f"O livro '{titulo_livro}' foi marcado como disponível com sucesso."
                if livro["disponivel"]
                else f"O livro '{titulo_livro}' foi marcado como indisponível com sucesso."
            )
            print(mensagem)

    if not livro_encontrado:
        print("O livro não foi encontrado.")

    volta_menu()

def escolha_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            alterar_disponibilidade()
        elif opcao == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except ValueError:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        volta_menu()

def main():
    os.system("cls")
    nome_app()
    opcoes_app()
    escolha_opcao()

if __name__ == "__main__":
    main()
