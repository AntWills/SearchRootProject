import sympy
from ..entities.PrecisionFloat import PrecisionFloat
from ..entities.Math import Math


def testPrecision():
    Math.setPrec(5)

    print(Math.pi(), ' - ', len(str(Math.pi())))
    print(Math.pi().evalf(), ' - ', len(str(Math.pi().evalf())))

    print(sympy.Float(sympy.pi, 5))
    pass


def testPrecision2():
    # Math.setPrec(10)
    num = PrecisionFloat(sympy.pi)
    # print(num)
    # print(num.truncate(40))

    # aux = sympy.sin(num)
    # print(aux)
    # print(Math.sin(num))
    # print(sympy.sin(num).evalf(10))
    # print(sympy.sin(num.evalf(10)).evalf(10))
    # print(aux.evalf(10))

    # print(sympy.Float(sympy.pi))
    # print(sympy.Float(sympy.pi, 40))
    # print(sympy.Float(sympy.pi).evalf(40))
    pass


def testPrecision3():
    Math.setPrec(10)
    num = PrecisionFloat(10, 5)
    num = Math.sin(num)
    print(num)
    pass


def testConvertion():
    num = sympy.Float('3.1415926535897932384626433832')
    numStr = str(num).split('.')[0]
    numInt = int(numStr)

    print(numInt)
    pass

# def testCustomFloat1():

#     nums = [
#         CustomFloat('0.123456789').evalf(50),
#         CustomFloat('1.123456789').evalf(5),
#         CustomFloat('10.123456789').evalf(5),
#         CustomFloat('088.123456789').evalf(5),
#         CustomFloat('0.1234567890').evalf(5),
#         CustomFloat('888.123456789').evalf(5)
#     ]

#     aux: CustomFloat = CustomFloat('0.0')
#     for num in nums:
#         aux = aux + num
#         pass
#     print(aux)
#     pass

# def __init__(self, value, precision=None):
#         # Se uma precisão personalizada for fornecida, aplica-a; caso contrário, usa a padrão.
#         if precision is not None:
#             # Passa o valor e a precisão ao inicializador de Float
#             super().__init__(str(value), precision)
#         else:
#             super().__init__(str(value))
#         print('CustomFloat inicializado com valor:',
#               value, ' e precisão: ', precision)
