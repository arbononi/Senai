from minhas_funcoes import *
import pytest

def test_soma_positiva():
    assert somar(5, 3) == 8

def test_soma_com_negativa():
    assert somar(10, -2) == 8

def test_subtracao():
    assert subtrair(10, 5) == 5

def test_multiplicacao():
    assert multiplicar(10, 2) == 20

def test_multiplicao_negativa():
    assert multiplicar(10, -2) == -20

def test_divisao():
    assert dividir(10, 2) == 5

def teste_divisao_negatica():
    assert dividir(10, -2) == (10/-2)

def test_divisao0():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_soma_tipo_invalido():
    with pytest.raises(TypeError):
        somar(5, 'texto')

def test_subtracao_tipo_invalido():
    with pytest.raises(TypeError):
        somar(10, 'texto')

def test_divisao_tipo_invalido():
    with pytest.raises(TypeError):
        dividir(5, 'texto')

def test_multiplicacao_tipo_invalido():
    with pytest.raises(TypeError):
        somar(5, 'texto')
