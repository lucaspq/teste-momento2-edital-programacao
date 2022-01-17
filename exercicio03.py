"""
*** DESAFIO 03 ***
Escreva um programa que lê 2 matrizes A e B, cada uma com 3 linhas e 2 colunas. Construir uma matriz C de mesma dimensão (3x2) onde C é formada pela soma dos elementos da matriz A com os elementos da matriz B (exemplo: C[1][1] = A[1][1] + B[1][1]). Apresentar ao final as 3 matrizes (A, B e C).
"""

import numpy as np

def preencheMatriz(n, m):
  mat = np.zeros((n, m))
  for i in range(n):
    for j in range(m):
        mat[i, j] = int(input(f"Digite o valor do elemento na linha {i} e coluna {j}: "))

  return mat


print(f"Preencha a matriz A")
matA = preencheMatriz(3,2)

print(f"Preencha a matriz B")
matB = preencheMatriz(3,2)

matC = matA + matB

print(f"Matriz A: \n{matA}")
print(f"Matriz B: \n{matB}")
print(f"Matriz C: \n{matC}")
