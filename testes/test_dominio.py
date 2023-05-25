import pytest
from gerenciador_espaco_tuplas.dominio.ambiente import Ambiente
from gerenciador_espaco_tuplas.dominio.dispositivo import Dispositivo
from gerenciador_espaco_tuplas.dominio.excecoes import (
    TamanhoMaximoNomeExcedido,
    EntidadeInvalida,
)
from gerenciador_espaco_tuplas.dominio.nome import Nome
from gerenciador_espaco_tuplas.dominio.usuario import Usuario


def test_nao_permite_nome_acima_de_20_caracteres():
    with pytest.raises(TamanhoMaximoNomeExcedido):
        Nome("Red Wacky League Antlez Broke the Stereo Neon")


def test_adicionar_usuario_e_dispositivo_ao_ambiente():
    ambiente = Ambiente(nome=Nome("Foo"))
    usuario = Usuario(nome=Nome("John Doe"))
    dispositivo = Dispositivo(nome=Nome("Bar"))

    ambiente.adicionar(entidade=usuario)
    ambiente.adicionar(entidade=dispositivo)

    assert len(ambiente.usuarios) == 1
    assert len(ambiente.dispositivos) == 1
    assert ambiente.usuarios[0] == usuario
    assert ambiente.dispositivos[0] == dispositivo


def test_adicionar_entidade_invalida_ao_ambiente():
    ambiente = Ambiente(nome=Nome("Foo"))
    entidade = object()

    with pytest.raises(EntidadeInvalida):
        ambiente.adicionar(entidade=entidade)
