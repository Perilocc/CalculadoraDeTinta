# OBJETIVO: Criar uma aplicação cuja função calcular a quantidade de tinta 
# necessária para pintar um cômodo através de suas dimensões (Altura, Largura e Profundidade).

from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    (input('Qual o valor da Largura do cômodo em metros?  ')),
    (input('Qual o valor da Profundidade do cômodo em metros? ')), 
    (input('Qual o valor da Altura do cômodo em metros? '))
)

print(
    'A área das Paredes é: {} metros quadrados'
    .format(calc.calcular_area_paredes(comodo))
)

print(
    'A área do Teto é: {} metros quadrados'
    .format(calc.calcular_area_teto(comodo))
)

print(
    'A Litragem de Tinta necessária é: {} Litros'
    .format(calc.calcular_litragem())
)