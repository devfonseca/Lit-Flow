from modelos.livro import Livro
from modelos.lista_livros.generos import Genero

livro_classico = Livro("Dom Casmurro", "Clássico")
genero_terro = Genero("Massacre da Serra Eletrica", 29.90, "Livros que causam medo e suspense.")
genero_terro.aplicar_desconto()
genero_espaco = Genero("Ficção Científica", 139.90, "Livros que exploram conceitos científicos e tecnológicos.")
livro_classico.adicionar_na_lista_livro(genero_terro)
livro_classico.adicionar_na_lista_livro(genero_espaco)

def main():
     livro_classico.exibir_lista_livro

if __name__ == "__main__":
    main()
