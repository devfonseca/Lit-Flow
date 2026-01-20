from modelos.avaliacao import Avaliacao


class Livro:
    livros = []

    def __init__(self, titulo: str, genero: str):
        self._titulo = titulo.title()
        self._genero = genero.title()
        self._disponivel = False
        self._avaliacoes = []
        Livro.livros.append(self)

    def __str__(self):
        return f"{self._titulo} | {self._genero}"

    @classmethod
    def listar_livros(cls):
        cabecalho = (
            f"{'Título do livro'.ljust(30)} | "
            f"{'Gênero'.ljust(20)} | "
            f"{'Avaliação'.ljust(10)} | "
            f"Status"
        )
        print(cabecalho)
        print("-" * len(cabecalho))

        for livro in cls.livros:
            print(
                f"{livro._titulo.ljust(30)} | "
                f"{livro._genero.ljust(20)} | "
                f"{str(livro.media_avaliacoes).ljust(10)} | "
                f"{livro.disponivel}"
            )

    @property
    def disponivel(self):
        return "☑" if self._disponivel else "☐"

    def alternar_disponibilidade(self):
        self._disponivel = not self._disponivel

    def receber_avaliacao(self, leitor: str, nota: float):
        # padrão “estrelas”: 0 a 5
        if 0 < nota <= 5:
            self._avaliacoes.append(Avaliacao(leitor, nota))

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "-"
        soma = sum(av._nota for av in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)
