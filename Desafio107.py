"""
Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DOMINUIR(), DOBRO() e
METADE().

Faça também um programa que IMPORTE esse módulo e use algumas dessas funções.
"""

from exercicio107 import teste

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${teste.metade(p)}')
print(f'O dobro de R${p} é R${teste.dobro(p)}')
print(f'Aumentando 10%, temos R${teste.aumentar(p)}')
