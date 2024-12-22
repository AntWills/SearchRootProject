from ..entities.Math import ExpressionSolver
from ..entities.SearchRootExp import SearchRootExp
from ..entities.PrecisionFloat import PrecisionFloat


def getOption() -> int:
    op: int = 0

    print('\n##   Menu Inicial   ##\n')

    print('1. Buscar zero da função.')
    print('2. Buscar raiz de um dado número.')
    print('0. Sair.')

    print('\nDigite a opção: ', end='')
    op = int(input())
    return op


def searchZeroFuncion():
    print('\nDigite os dados:\n')
    print('A expressão: ', end='')
    exp = input()
    print('x de A (ponto A): ', end='')
    pointA = ExpressionSolver.expression(input(), None)
    print('x de B (ponto B): ', end='')
    pointB = ExpressionSolver.expression(input(), None)

    print('A aproximação, obs: só número int: ', end='')
    erro = int(input())

    print('\nDigite agora o método: ')
    print('1. Bissceção.')
    print('2. Falsa posição.')

    print('\n::', end='')
    metodo = int(input())
    root: PrecisionFloat = None
    if metodo == 1:
        root = SearchRootExp.bisectionMethod(exp, [pointB, pointA], erro)
    elif metodo == 2:
        root = SearchRootExp.falsePositionMethod(exp, [pointB, pointA], erro)

    print('\nRaiz (aproximada): ', root, ', iterações: ',
          SearchRootExp.getQuantIteraion(), '.')
    pass


def searchRoot():
    print('\nDigite o indice: ', end='')
    index = int(input())
    print('Digite o radicando: ', end='')
    radicand = int(input())
    print('A aproximação, obs -> só número int: ', end='')
    erro = int(input())

    exp = f'root({index}, {radicand})'

    print('\nDigite agora o método: ')
    print('1. Bissceção.')
    print('2. Falsa posição.')

    print('\n::', end='')
    metodo = int(input())
    root: PrecisionFloat = None
    if metodo == 1:
        root = SearchRootExp.bisectionMethod(exp, None, erro)
    elif metodo == 2:
        root = SearchRootExp.falsePositionMethod(exp, None, erro)
    print('Raiz (aproximada): ', root, ', iterações: ',
          SearchRootExp.getQuantIteraion(), '.')
    pass


def options(op: int):
    if op == 1:
        searchZeroFuncion()
    elif op == 2:
        searchRoot()
    pass


def menuLopp():
    while True:
        try:
            aux = getOption()
            options(aux)
        except:
            print('\nOuvi um erro, pode ser na expressão, intervalo...\n')
        if aux == 0:
            break
        pass
    print('\nEncerrando...')
    pass
