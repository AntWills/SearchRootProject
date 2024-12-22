from sympy import sin, cos, tan, asin, acos, atan, log, pi, exp, deg, rad, sympify, nan, symbols, diff
from .PrecisionFloat import PrecisionFloat


class Math:
    @staticmethod
    def root(index: int, radicand: PrecisionFloat) -> PrecisionFloat:
        return radicand ** (PrecisionFloat(1)/PrecisionFloat(index))

    @staticmethod
    def log(x: PrecisionFloat, base: PrecisionFloat = 10) -> PrecisionFloat:
        return log(x.evalf(PrecisionFloat.getDps() + 5), base.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def logN(x: PrecisionFloat) -> PrecisionFloat:
        try:
            return log(x).evalf(PrecisionFloat.getDps() + 5).evalf(PrecisionFloat.getDps())
        except:
            raise ValueError(
                "O logaritmo natural não pode ser calculado para números não positivos.")

    @staticmethod
    def sin(x: PrecisionFloat) -> PrecisionFloat:
        aux = sin(x.evalf(PrecisionFloat.getDps() + 5)
                  ).evalf(PrecisionFloat.getDps())
        return aux

    @staticmethod
    def cos(x: PrecisionFloat) -> PrecisionFloat:
        return cos(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def tan(x: PrecisionFloat) -> PrecisionFloat:
        return tan(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def arcSin(x: PrecisionFloat) -> PrecisionFloat:
        return asin(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def arcCos(x: PrecisionFloat) -> PrecisionFloat:
        return acos(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def arcTan(x: PrecisionFloat) -> PrecisionFloat:
        return atan(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def pi() -> PrecisionFloat:
        return PrecisionFloat(num=pi, dps=(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def ePow(x: PrecisionFloat) -> PrecisionFloat:
        return exp(x.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def toRadians(degrees: PrecisionFloat) -> PrecisionFloat:
        return rad(degrees.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())

    @staticmethod
    def toDegrees(radians: PrecisionFloat) -> PrecisionFloat:
        return deg(radians.evalf(PrecisionFloat.getDps() + 5)).evalf(PrecisionFloat.getDps())


class ExpressionSolver:
    @staticmethod
    def expression(expStr: str, value: PrecisionFloat) -> PrecisionFloat:
        if isinstance(value, PrecisionFloat):
            value = PrecisionFloat(str(value), PrecisionFloat.getDps())

        exp = expStr.replace('^', '**')

        context = {
            'log': Math.log,
            'logN': Math.logN,
            'sin': Math.sin,
            'cos': Math.cos,
            'tan': Math.tan,
            'arcSin': Math.arcSin,
            'arcCos': Math.arcCos,
            'arcTan': Math.arcTan,
            'PI': Math.pi,
            'ePow': Math.ePow,
            'root': Math.root,
            'PrecisionFloat': PrecisionFloat,
            'x': symbols('x')
        }

        exp = sympify(expStr, locals=context)
        return exp.evalf(PrecisionFloat.getDps() + 5, subs={'x': value})


class Function():
    def __init__(self, exp: str):
        # x = symbols('x')
        # fun = sympify(exp)

        # self.derivative: str = str(diff(fun, x))
        self.derivative: str = None
        self.exp = exp
        pass

    def getImage(self, xValue: PrecisionFloat) -> PrecisionFloat:
        try:
            if not isinstance(xValue, PrecisionFloat):
                xValue = PrecisionFloat(xValue, PrecisionFloat.getDps())
            return ExpressionSolver.expression(self.exp, xValue)
        except:
            return None

    def getAbsImage(self, xValue: PrecisionFloat) -> PrecisionFloat:
        try:
            if not isinstance(xValue, PrecisionFloat):
                xValue = PrecisionFloat(xValue, PrecisionFloat.getDps())
            return abs(self.getImage(xValue))
        except:
            return None

    def getImageOfDerivate(self, xValue: PrecisionFloat) -> PrecisionFloat:
        try:
            if not isinstance(xValue, PrecisionFloat):
                xValue = PrecisionFloat(xValue, PrecisionFloat.getDps())

            if not self.derivative:
                x = symbols('x')
                fun = sympify(self.exp)

                self.derivative = str(diff(fun, x))

            return ExpressionSolver.expression(self.derivative, xValue)
        except:
            return None

    def __str__(self) -> str:
        return self.exp

    pass


# class RootData:
#     def __init__(self, index: int, radicand: float):
#         self.index = index
#         self.radicand = radicand
#         pass
#     pass


# class SearchRootExp:

#     __typeSearch: int = 0
#     '''
#     1, se for bisectionMethod
#     2, se for falsePositionMethod
#     0, se não ouver buscas no momento.
#     '''
#     __xA: PrecisionFloat = PrecisionFloat('0.0', PrecisionFloat.getDps())
#     __xB: PrecisionFloat = PrecisionFloat('0.0', PrecisionFloat.getDps())
#     __function: Function = None
#     '''
#     variavel criada para armazenar a função que está sendo buscada a raiz
#     '''
#     __functionGx: Function = None
#     '''
#     É a função Fi que converge, é usado no fixedPointMethod.
#     '''

#     __errorPrecisionFloat: PrecisionFloat = PrecisionFloat(
#         '0.0', PrecisionFloat.getDps())
#     __errorInt: int = 5
#     __existRoot: bool = True
#     __cauntIteration: int = 0
#     __iterationValues: list[list[PrecisionFloat]] = []

#     __funAproximateRoot: any = None
#     ''' Função de aproximação da raiz, é passada o ponteiro da função
#     '''

#     # @staticmethod
#     # def getCurrentError() -> int:
#     #     return SearchRootExp.__errorInt

#     # @staticmethod
#     # def getCurrentTypeSearch() -> int:
#     #     return SearchRootExp.__typeSearch

#     @staticmethod
#     def getQuantIteraion() -> int:
#         return SearchRootExp.__cauntIteration

#     @staticmethod
#     def getIterationValues() -> list[list[PrecisionFloat]]:
#         return SearchRootExp.__iterationValues

#     @staticmethod
#     def __getAproximateRootBisection(numB: PrecisionFloat, numA: PrecisionFloat) -> PrecisionFloat:
#         return (numA + numB) / PrecisionFloat('2', PrecisionFloat.getDps())

#     @staticmethod
#     def __getAproximateRootFalsePosition(numB: PrecisionFloat,
#                                          numA: PrecisionFloat) -> PrecisionFloat:
#         fun = SearchRootExp.__function

#         aux1 = numB * fun.getImage(numA) - numA * fun.getImage(numB)
#         aux2 = fun.getImage(numA) - fun.getImage(numB)
#         return aux1 / aux2

#     @staticmethod
#     def __getGxThatConverges(listOfGx: list[str]) -> Optional[str]:

#         return

#     @staticmethod
#     def bisectionMethod(expStr: str,
#                         interval: Optional[list[float]],
#                         error: int) -> Optional[list[PrecisionFloat]]:
#         if not expStr:
#             return None
#         if not isinstance(error, int):
#             raise ValueError('erro não pode ser diferente de int.')

#         SearchRootExp.__initializeVariables(
#             expStr=expStr, interval=interval, listOfGx=None, error=error, typeSearch=1)
#         SearchRootExp.__adjustIntervalIfNotImageExist()
#         rangeList = SearchRootExp.__checkAndFindInterval()

#         rootList: list[PrecisionFloat] = []
#         for intervals in rangeList:
#             rootList.append(SearchRootExp.__getZeroFunction(intervals))
#             pass
#         return rootList

#     @staticmethod
#     def falsePositionMethod(expStr: str,
#                             interval: Optional[list[float]],
#                             error: int) -> Optional[PrecisionFloat]:
#         if not expStr:
#             return None
#         if not isinstance(error, int):
#             raise ValueError('erro não pode ser diferente de int.')

#         SearchRootExp.__initializeVariables(
#             expStr=expStr, interval=interval, listOfGx=None, error=error, typeSearch=2)
#         SearchRootExp.__adjustIntervalIfNotImageExist()
#         rangeList = SearchRootExp.__checkAndFindInterval()

#         rootList: list[PrecisionFloat] = []
#         for intervals in rangeList:
#             rootList.append(SearchRootExp.__getZeroFunction(intervals))
#             pass
#         return rootList

#     @staticmethod
#     def fixedPointMethod(expStr: str,
#                          interval: Optional[list[float]],
#                          listOfGx: list[str],
#                          error: int) -> Optional[PrecisionFloat]:
#         if not expStr:
#             return None
#         if not isinstance(error, int):
#             raise ValueError('erro não pode ser diferente de int.')

#         SearchRootExp.__initializeVariables(
#             expStr, interval, listOfGx, error, 3)
#         pass

#     @staticmethod
#     def __initializeVariables(expStr: str,
#                               interval: Optional[list[float]],
#                               listOfGx: list[str],
#                               error: int,
#                               typeSearch: int) -> None:

#         SearchRootExp.__errorPrecisionFloat = PrecisionFloat(
#             '10', PrecisionFloat.getDps()) ** PrecisionFloat(str(-error), PrecisionFloat.getDps())

#         SearchRootExp.__xA = PrecisionFloat(
#             str(interval[1]), PrecisionFloat.getDps())
#         SearchRootExp.__xB = PrecisionFloat(
#             str(interval[0]), PrecisionFloat.getDps())

#         if SearchRootExp.__xA < SearchRootExp.__xB:
#             aux = SearchRootExp.__xA
#             SearchRootExp.__xA = SearchRootExp.__xB
#             SearchRootExp.__xB = aux
#             pass
#         # SearchRootExp.__expStr = expStr
#         SearchRootExp.__function = Function(expStr)
#         SearchRootExp.__existRoot = True
#         SearchRootExp.__cauntIteration = 0
#         SearchRootExp.__errorInt = error
#         SearchRootExp.__typeSearch = typeSearch

#         match typeSearch:
#             case 1:
#                 SearchRootExp.__funAproximateRoot = SearchRootExp.__getAproximateRootBisection
#             case 2:
#                 SearchRootExp.__funAproximateRoot = SearchRootExp.__getAproximateRootFalsePosition
#             case 3:
#                 SearchRootExp.__functionGx = SearchRootExp.__getGxThatConverges(
#                     listOfGx)
#                 pass
#         pass

#     @staticmethod
#     def __adjustIntervalIfNotImageExist() -> None:
#         if not SearchRootExp.__existRoot:
#             return
#         fun = SearchRootExp.__function
#         pointA = SearchRootExp.__xA
#         pointB = SearchRootExp.__xB

#         if fun.getImage(pointA):
#             pointA -= SearchRootExp.__errorPrecisionFloat
#         if fun.getImage(pointB):
#             pointB += SearchRootExp.__errorPrecisionFloat

#         SearchRootExp.__xA = pointA
#         SearchRootExp.__xB = pointB
#         pass

#     @staticmethod
#     def __checkAndFindInterval() -> list[list[PrecisionFloat]]:
#         if not SearchRootExp.__existRoot:
#             return

#         pointA = SearchRootExp.__xA
#         pointB = SearchRootExp.__xB
#         space: PrecisionFloat = PrecisionFloat('0.05', PrecisionFloat.getDps())

#         rangeList: list[list[PrecisionFloat]] = []
#         currentPoint: PrecisionFloat = pointA

#         while True:
#             currentPoint -= space
#             if currentPoint > pointB:
#                 if SearchRootExp.__testInterval(currentPoint, currentPoint + space):
#                     rangeList.append([currentPoint, currentPoint + space])
#                     pass
#                 pass
#             else:
#                 break
#             pass
#         return rangeList

#     @staticmethod
#     def __testInterval(xB, xA) -> bool:
#         fun = SearchRootExp.__function

#         fA = fun.getImage(xA)
#         fB = fun.getImage(xB)
#         return (fA * fB) < PrecisionFloat('0', PrecisionFloat.getDps())

#     @staticmethod
#     def __PrecisionFloatTruncate(number: PrecisionFloat) -> PrecisionFloat:
#         return round(number, SearchRootExp.__errorInt)

#     @staticmethod
#     def __getZeroFunction(interval: list[PrecisionFloat]) -> Optional[PrecisionFloat]:
#         if not SearchRootExp.__existRoot:
#             return None

#         a = PrecisionFloat(f'{interval[1]}', PrecisionFloat.getDps())
#         b = PrecisionFloat(f'{interval[0]}', PrecisionFloat.getDps())
#         aproximateRoot: PrecisionFloat = PrecisionFloat(
#             '0.0', PrecisionFloat.getDps())

#         fun = SearchRootExp.__function

#         if fun.getAbsImage(a) < SearchRootExp.__errorPrecisionFloat:
#             return a
#         if fun.getAbsImage(b) < SearchRootExp.__errorPrecisionFloat:
#             return b

#         while True:
#             SearchRootExp.__cauntIteration += 1
#             aproximateRoot = SearchRootExp.__funAproximateRoot(b, a)
#             absImageValue = fun.getAbsImage(aproximateRoot)

#             print(f'[{b}, {a}] => {aproximateRoot} : '
#                   + f'{absImageValue} > '
#                   + f'{SearchRootExp.__errorPrecisionFloat}')

#             SearchRootExp.__iterationValues.append(
#                 [SearchRootExp.__cauntIteration, b, a, aproximateRoot, absImageValue,
#                     SearchRootExp.__errorPrecisionFloat]
#             )

#             if absImageValue < SearchRootExp.__errorPrecisionFloat:
#                 break

#             if SearchRootExp.__testInterval(b, aproximateRoot):
#                 a = aproximateRoot
#             else:
#                 b = aproximateRoot
#             pass
#         # SearchRootExp.__typeSearch = 0
#         return SearchRootExp.__PrecisionFloatTruncate(aproximateRoot)
