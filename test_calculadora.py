import pytest

from calculadora import somar, subtrair, multiplicar


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 5) == 5


def test_multiplicar():
    assert multiplicar(4, 2) == 8
