import pytest

from calculadora import somar, subtrair, multiplicar, dividir, eh_par, potencia


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 5) == 5


def test_multiplicar():
    assert multiplicar(4, 2) == 8


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero_lanca_erro():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_eh_par():
    assert eh_par(4) is True


def test_eh_impar():
    assert eh_par(5) is False


def test_potencia():
    assert potencia(2, 3) == 8
