import uuid
from typing import List, Union

from gerenciador_espaco_tuplas.dominio.dispositivo import Dispositivo
from gerenciador_espaco_tuplas.dominio.excecoes import ItemInvalido
from gerenciador_espaco_tuplas.dominio.nome import Nome
from gerenciador_espaco_tuplas.dominio.usuario import Usuario


class Ambiente:
    def __init__(self, nome: Nome):
        self.id: uuid.UUID = uuid.uuid4()
        self.nome: Nome = nome
        self.usuarios: List[Usuario] = []
        self.dispositivos: List[Dispositivo] = []

    def adicionar(self, item: Union[Usuario, Dispositivo]):
        if isinstance(item, Usuario):
            self.usuarios.append(item)
        elif isinstance(item, Dispositivo):
            self.dispositivos.append(item)
        else:
            raise ItemInvalido(item)
