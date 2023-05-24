from gerenciador_espaco_tuplas.dominio.excecoes import TamanhoMaximoNomeExcedido


class Nome(str):
    def __new__(cls, nome: str):
        if len(nome) > 20:
            raise TamanhoMaximoNomeExcedido(nome, 20)
        return super().__new__(cls, nome)
