"""Módulo com as funções de manipulação de matrizes."""

import math
def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Soma duas matrizes"""
    # TODO: implementar
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return None

    resultado = [[xi + yi for xi, yi in zip(xrow, yrow)] for xrow, yrow in zip(x, y)]
    return resultado


def multiplicacao_por_escalar(matriz: list[list[float]], escalar: float) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    # TODO: implementar
    resultado = [[elemento * escalar for elemento in linha] for linha in matriz]
    return resultado


def multiplicacao(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Multiplica duas matrizes"""
    # TODO: implementar
    if len(matriz1[0]) != len(matriz2):
        return None

    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    colunas_matriz2 = len(matriz2[0])

    resultado = [[0] * colunas_matriz2 for _ in range(linhas_matriz1)]

    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    # TODO: implementar
    if not x:
        return 0

    soma_quadrados = sum([elem ** 2 for linha in x for elem in linha])
    norma = math.sqrt(soma_quadrados)
    return norma


def eh_simetrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    # TODO: implementar
    if not x:
        return 0

    soma_quadrados = sum([elem ** 2 for linha in x for elem in linha])
    norma = math.sqrt(soma_quadrados)
    return norma


def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    # TODO: implementar
    if not x:
        return []

    num_linhas = len(x)
    num_colunas = len(x[0])

    transposta = [[x[j][i] for j in range(num_linhas)] for i in range(num_colunas)]
    return transposta
