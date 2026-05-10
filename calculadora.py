def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b


def eh_par(numero):
    return numero % 2 == 0


def potencia(base, expoente):
    return base ** expoente
