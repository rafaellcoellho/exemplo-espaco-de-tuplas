import uuid

from gerenciador_espaco_tuplas.dominio.nome import Nome


class Usuario:
    def __init__(self, nome: Nome):
        self.id: uuid.UUID = uuid.uuid4()
        self.nome: Nome = nome
