from ..entities.Math import ExpressionSolver, Math
from ..entities.SearchRootExp import *
from sympy import *

import re
from prettytable import PrettyTable


def testAbs():
    num1 = Float('3.4', 40)
    num2 = Float('3', 5)

    print(f'{num1**num2}')


def exibir_tabela(headers, dados, maxLenData):
    dados_limitados = []

    for linha in dados:
        linha_limitada = []
        for valor in linha:
            str_valor = str(valor)
            # Limita cada valor a 30 caracteres, adicionando '...' se necessário
            if len(str_valor) > maxLenData:
                str_valor = str_valor[:maxLenData] + '...'
            linha_limitada.append(str_valor)
        dados_limitados.append(linha_limitada)

    tabela = PrettyTable(headers)

    for linha in dados_limitados:
        tabela.add_row(linha)
    print(tabela)


def testExp():
    exp1 = 'x*logN(x) - 10'
    intervalo1 = [0, 7]
    error = 5

    exp2 = 'arcTan(x) + x^2 - 4'
    intervalo2 = [-6, 3]

    exp3 = 'ePow(-x) - sin(x)'
    intervalo3 = [4, 7]

    # exp = 'x^2 -4*x + 4 - logN(x)'
    # intervalo = [Solve.expression(
    #     '0', None), Solve.expression('PI()/2 + 1', None)]

    # root = SearchRootExp.bisectionMethod(exp1, intervalo1, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )

    # root = SearchRootExp.falsePositionMethod(exp1, intervalo1, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )

    # root = SearchRootExp.bisectionMethod(exp2, intervalo2, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )

    # root = SearchRootExp.falsePositionMethod(exp2, intervalo2, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )

    function_str_1: str = 'x**3-x-1'
    lista_teste_1: list[str] = [
        '1/(x**2-1)',
        '(x+1)**(1/3)'
    ]
    x_a_1, x_b_1 = 1, 2

    searchData: SearchData = SearchRootExp.fixedPointMethod(
        function_str_1, [x_a_1, x_b_1], lista_teste_1, 5)
    print(f'\nRaiz(Aproximada): {searchData.root} iterações: '
          + f'{searchData.quantIteration}')

    print('\nOperações:\n\n')
    # exibir_tabela(["Iteração", "xB", "xA",
    #                "raiz aproximada", "F(Xn)", "erro"],
    #               searchData.valuesPerIteration, 15)

    exibir_tabela(["Iteração", "Xn", "F(Xn)", "erro", "Xn+1 = G(Xn)",],
                  searchData.valuesPerIteration, 15)

    # root = SearchRootExp.falsePositionMethod(exp, intervalo, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )

    # root = SearchRootExp.falsePositionMethod(exp1, intervalo1, error)
    # print(
    #     f'\nRaiz(Aproximada): {root} iterações: {
    #         SearchRootExp.getQuantIteraion()}'
    # )


def testRoot():
    exp1 = 'x * sin(x) + root(2, 8.5)'
    exp2 = 'root(2, 8.5)'

    # print(Solve.expression(exp, 8))

    # root = SearchRootExp.bisectionMethod(exp1, [5, 6], 5)
    # quantIt = SearchRootExp.getQuantIteraion()
    # print(root, ' - ', quantIt)

    root = SearchRootExp.bisectionMethod(exp2, None, 5)
    quantIt = SearchRootExp.getQuantIteraion()
    print(root, ' - ', quantIt)

    # root = SearchRootExp.falsePositionMethod(exp, None, 5)
    # quantIt = SearchRootExp.getQuantIteraion()
    # print(root, ' - ', quantIt)
    pass


def testConversao():
    def truncate(number: Float, decimals: int) -> Float:
        fator = 10 ** decimals
        return (floor(number * fator) / fator).evalf()

    def truncar(numero, casas_decimais):

        # Convertemos o número para uma fração racional para maior precisão
        frac = Rational(str(numero))

        # Multiplicamos por 10 elevado ao número de casas decimais desejado
        # para "mover" a vírgula decimal para a direita
        multiplicador = 10 ** casas_decimais

        # Aplicamos a função floor para remover a parte fracionária
        resultado = floor(frac * multiplicador)

        # Dividimos novamente para "mover" a vígula decimal de volta
        return resultado / multiplicador

    numberStr = '53.72892465975761413574219'
    portionInt = len(numberStr.split('.')[0])
    num = Float('53.72892465975761413574219', 5)

    print(f'{num}')
    pass


def test():

    exp = 'ePow(-x) - sin(x)'
    print(ExpressionSolver.expression(exp, 0))


def test1():
    SearchRootExp.test1('sin(x) + root(2, 8) + 3')
    pass


def test2():
    Math.setPrec(5)
    num1 = Float('0.123456789')
    num2 = Float('01.123456789')
    print(num1.evalf(5), ' - ', num2.evalf(5))
    pass


def test3():
    num = ExpressionSolver.expression('root(x, 2) + root(x, 2)', 4)
    print(num)
    pass


def test4():
    math_methods = [
        'sin', 'cos', 'tan', 'arcSin', 'arcCos', 'arcTan',
        'log', 'logN', 'pi', 'ePow', 'toRadians', 'toDegrees', 'root'
    ]

    pattern = r'\b(' + '|'.join(math_methods) + r')\b'

    expression = 'arcTan(x) + x^2 - 4 + root()'

    matches = re.findall(pattern, expression)

    print("Métodos chamados:", matches)
    print("Tipo", type(matches[0]).__name__)
    pass
