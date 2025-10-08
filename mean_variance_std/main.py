import numpy as np

def calculate(list):


    # 1. Validação da entrada

    # Verifica se a lista contém exatamente 9 números
    # Caso contrário, lança um erro informando ao usuário
    if len(list) != 9:
        raise ValueError("Por Favor insira 9 números.")


    # 2. Transformação em matriz 3x3

    # Converte a lista em um array NumPy e reorganiza em uma matriz 3x3
    # Exemplo: [1,2,3,4,5,6,7,8,9] vira
    # [[1,2,3],
    #  [4,5,6],
    #  [7,8,9]]
    matrix = np.array(list).reshape(3, 3)


    # 3. Cálculos estatísticos

    # O dicionário 'calculations' guarda, para cada métrica (média, variância, etc.),
    # três valores:
    #   [0] → resultado por coluna (axis=0)
    #   [1] → resultado por linha (axis=1)
    #   [2] → resultado total (toda a matriz)
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),  # Média por coluna
            np.mean(matrix, axis=1).tolist(),  # Média por linha
            matrix.mean().item()               # Média total
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),   # Variância por coluna
            np.var(matrix, axis=1).tolist(),   # Variância por linha
            matrix.var().item()                # Variância total
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),   # Desvio padrão por coluna
            np.std(matrix, axis=1).tolist(),   # Desvio padrão por linha
            matrix.std().item()                # Desvio padrão total
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),   # Máximo por coluna
            np.max(matrix, axis=1).tolist(),   # Máximo por linha
            matrix.max().item()                # Máximo total
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),   # Mínimo por coluna
            np.min(matrix, axis=1).tolist(),   # Mínimo por linha
            matrix.min().item()                # Mínimo total
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),   # Soma por coluna
            np.sum(matrix, axis=1).tolist(),   # Soma por linha
            matrix.sum().item()                # Soma total
        ]
    }


    # Retorna o dicionário com todos os cálculos
    return calculations
