"""
*** DESAFIO 01 ***
Faça um programa que preencha um vetor com 6 valores distintos digitados pelo usuário. 
Em seguida, exiba o maior e o menor valor do vetor, indicando em qual posição eles se encontram. 
Depois, imprima os itens no vetor em ordem crescente.
"""

a = []
n = 6
pos = 0

while (pos != n):
  num = input(f"Digite um valor inteiro da posição {pos}: ")
  try:
    a.append(int(num))
    pos = pos + 1
  except ValueError:
    print("Digite um número inteiro!")


print(f'Vetor original: {a}')

maxValue = max(a)
minValue = min(a)

maxValueIndex = a.index(maxValue)
minValueIndex = a.index(minValue)

print(f'O maior valor é {maxValue} na posição {maxValueIndex}')
print(f'O menor valor é {minValue} na posição {minValueIndex}')

print(f'Vetor em ordem crescente: {sorted(a)}')
