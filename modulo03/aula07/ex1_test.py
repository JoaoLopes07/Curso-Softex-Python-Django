from ex1lista import rotacionar_lista
import pytest

def test_rotacao_simples():
    assert rotacionar_lista([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotacao_zero():
    assert rotacionar_lista([1, 2, 3], 0) == [1, 2, 3]

def test_rotacao_tamanho_lista():
    assert rotacionar_lista([1, 2, 3], 3) == [1, 2, 3]

def test_rotacao_maior_que_tamanho():
    assert rotacionar_lista([1, 2, 3], 5) == [2, 3, 1]

def test_lista_vazia():
    assert rotacionar_lista([], 3) == []
