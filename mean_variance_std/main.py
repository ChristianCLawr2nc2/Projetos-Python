import numpy as np


def calculate(list):
    # Verificando se a lista contém exatamente 9 números
    if len(list) != 9:
        raise ValueError("Por Favor insira 9 números.")

    # Transformando a lista em uma matriz 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calculando os valores pedidos

    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), matrix.mean().item()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), matrix.var().item()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), matrix.std().item()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), matrix.max().item()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), matrix.min().item()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), matrix.sum().item()]
    }

    return calculations