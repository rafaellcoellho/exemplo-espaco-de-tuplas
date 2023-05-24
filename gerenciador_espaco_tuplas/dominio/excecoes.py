from dataclasses import dataclass


@dataclass
class TamanhoMaximoNomeExcedido(Exception):
    nome: str
    tamanho_maximo: int

    def __str__(self):
        return f"Nome {self.nome} deve ser menor ou igual a {self.tamanho_maximo} caracteres"


@dataclass
class ItemInvalido(Exception):
    item: object

    def __str__(self):
        return f"Item {self.item} inválido"
