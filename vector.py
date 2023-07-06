"""Módulo com as funções de manipulação de vetores."""

import math
def norma(x: list[float]) -> float | None:
    """Calcula a norma de um vetor"""
    if not x:
        return None
    soma_quadrados = sum([elem ** 2 for elem in x])
    norma = math.sqrt(soma_quadrados)
    return norma


def soma(x: list[float], y: list[float]) -> list[float] | None:
    """Soma dois vetores"""
    # TODO: implementar
    if len(x) != len(y):
        return None

    resultado = [xi + yi for xi, yi in zip(x, y)]
    return resultado


def multiplicação_por_escalar(vetor: list[float], escalar: float) -> list[float]:
    """Multiplica um vetor por um escalar"""
    # TODO: implementar
    resultado = [elemento * escalar for elemento in vetor]
    return resultado

def produto_interno(x: list[float], y: list[float]) -> float | None:
    """Calcula o produto interno de dois vetores"""
    # TODO: implementar
    if len(x) != len(y):
        return None

    if not x or not y:
        return 0

    resultado = sum([xi * yi for xi, yi in zip(x, y)])
    return resultado


def produto_vetorial(x: list[float], y: list[float]) -> list[float] | None:
    """Calcula o produto vetorial de dois vetores"""
    # TODO: implementar
    if len(x) != 3 or len(y) != 3:
        return None
    resultado = [
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0]
    ]

    return resultado


def produto_diádico(x: list[float], y: list[float]) -> list[list[float]] | None:
    """Calcula o produto diádico de dois vetores"""
    # TODO: implementar
    if len(x) != len(y):
        return None

    produto = [[xi * yj for yj in y] for xi in x]
    return produto
