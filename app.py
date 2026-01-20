from modelos.livro import Livro
from modelos.lista_livros.generos import Genero

livro1 = Livro("Dom Casmurro", "Clássico")
genero_terro = Genero("Massacre da Serra Eletrica", 29.90, "Livros que causam medo e suspense.")

def main():
    print(genero_terro)

if __name__ == "__main__":
    main()
