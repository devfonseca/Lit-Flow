from modelos.lista_livros.lista_livros import ListaLivros

class Genero(ListaLivros):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco, descricao)
        self._descricao = descricao
        
    def __str__(self):
        return self._nome