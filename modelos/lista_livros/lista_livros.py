from abc import ABC, abstractmethod

class ListaLivros(ABC):
    def __init__(self, nome: str, preco: float, descricao: str = ""):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    @abstractmethod
    def aplicar_desconto(self):
        pass