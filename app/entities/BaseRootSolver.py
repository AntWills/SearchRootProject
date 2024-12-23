from .Math import Function
from .PrecisionFloat import PrecisionFloat
from typing import Optional


class SearchData:
    def __init__(self, root: PrecisionFloat,
                 quantIteration: int,
                 valuesPerIteration: list[list[PrecisionFloat]],
                 funGx: Optional[Function] = None):
        self.root: PrecisionFloat = root
        self.quantIteration: int = quantIteration
        self.valuesPerIteration: list[list[PrecisionFloat]
                                      ] = valuesPerIteration
        self.funGx = funGx
        pass
    pass


class BaseRootSolver:
    def __init__(self, expStr: str, interval: list[PrecisionFloat], error: int):
        # Atributos de instância

        if not expStr:
            raise ValueError('expStr não pode None.')
        if not isinstance(error, int):
            raise ValueError('Erro não pode ser diferente de int.')
        if error <= 0:
            raise ValueError('Error não pode ser 0 ou negativo.')

        self._xA: PrecisionFloat = PrecisionFloat(
            interval[1], PrecisionFloat.getDps())
        self._xB: PrecisionFloat = PrecisionFloat(
            interval[0], PrecisionFloat.getDps())
        self._function: Function = Function(expStr)

        if self._xA < self._xB:
            aux = self._xA
            self._xA = self._xB
            self._xB = aux

        self._errorPrecisionFloat: PrecisionFloat = PrecisionFloat(
            '10', PrecisionFloat.getDps()) ** PrecisionFloat(str(-error), PrecisionFloat.getDps())
        self._errorInt: int = error

        self._existRoot: bool = True
        self._cauntIteration: int = 0
        self._iterationValues: list[list[PrecisionFloat]] = []

        # Inicializar as variáveis da instância

    def getQuantIteration(self) -> int:
        return self._cauntIteration

    def getIterationValues(self) -> list[list[PrecisionFloat]]:
        return self._iterationValues

    def _testInterval(self, xB: PrecisionFloat, xA: PrecisionFloat) -> bool:
        fun: Function = self._function

        fA: PrecisionFloat = fun.getImage(xA)
        fB: PrecisionFloat = fun.getImage(xB)
        return (fA * fB) < PrecisionFloat('0', PrecisionFloat.getDps())

    def _PrecisionFloatTruncate(self, number: PrecisionFloat) -> PrecisionFloat:
        return round(number, self._errorInt)

    def _initializeVariables(self):
        self._existRoot: bool = True
        self._cauntIteration: int = 0
        self._iterationValues: list[list[PrecisionFloat]] = []

    def _adjustIntervalIfNotImageExist(self) -> None:
        if not self._existRoot:
            return
        fun = self._function
        xA = self._xA
        xB = self._xB

        if fun.getImage(xA):
            xA -= self._errorPrecisionFloat
        if fun.getImage(xB):
            xB += self._errorPrecisionFloat

        self._xA = xA
        self._xB = xB

    def _checkAndFindInterval(self) -> list[list[PrecisionFloat]]:
        xA = self._xA
        xB = self._xB

        listInterval: list[list[PrecisionFloat]] = []

        space = PrecisionFloat('0.05', PrecisionFloat.getDps())

        auxA = xA
        auxB = xA - space

        while xB <= auxB:
            if self._testInterval(auxB, auxA):
                listInterval.append([auxB, auxA])

            auxA = auxB
            auxB -= space
            pass

        if self._testInterval(xB, auxA):
            listInterval.append([xB, auxA])

        return listInterval


class BisectionMethodRootSolver(BaseRootSolver):
    def solve(self) -> Optional[list[SearchData]]:
        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        dataList: list[SearchData] = []
        for intervals in listInterval:
            data = SearchData(
                self.__getZeroFunction(intervals),
                self._cauntIteration,
                self._iterationValues
            )
            dataList.append(data)
            super()._initializeVariables()
            pass
        return dataList

    def __getZeroFunction(self, interval: list[PrecisionFloat]) -> Optional[PrecisionFloat]:
        if not self._existRoot:
            return None

        a = PrecisionFloat(f'{interval[1]}', PrecisionFloat.getDps())
        b = PrecisionFloat(f'{interval[0]}', PrecisionFloat.getDps())
        aproximateRoot: PrecisionFloat = PrecisionFloat(
            '0.0', PrecisionFloat.getDps())

        fun: Function = self._function

        if fun.getAbsImage(a) < self._errorPrecisionFloat:
            return a
        if fun.getAbsImage(b) < self._errorPrecisionFloat:
            return b

        while True:
            self._cauntIteration += 1
            aproximateRoot = self.__getAproximateRoot(
                b, a)
            absImageValue = fun.getAbsImage(aproximateRoot)

            # print(f'[{b}, {a}] => {aproximateRoot} : '
            #       + f'{absImageValue} > '
            #       + f'{self._errorPrecisionFloat}')

            self._iterationValues.append(
                [self._cauntIteration, b, a, aproximateRoot, absImageValue,
                    self._errorPrecisionFloat]
            )

            if absImageValue < self._errorPrecisionFloat:
                break

            if super()._testInterval(b, aproximateRoot):
                a = aproximateRoot
            else:
                b = aproximateRoot
            pass
        # SearchRootExp.__typeSearch = 0
        return super()._PrecisionFloatTruncate(aproximateRoot)

    def __getAproximateRoot(self, xB: PrecisionFloat, xA: PrecisionFloat) -> PrecisionFloat:
        return (xA + xB) / PrecisionFloat('2', PrecisionFloat.getDps())


class FalsePositionMethodRootSolver(BaseRootSolver):
    def solve(self) -> Optional[list[SearchData]]:
        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        dataList: list[SearchData] = []
        for intervals in listInterval:
            data = SearchData(
                self.__getZeroFunction(intervals),
                self._cauntIteration,
                self._iterationValues
            )
            dataList.append(data)
            super()._initializeVariables()
            pass
        return dataList

    def __getZeroFunction(self, interval: list[PrecisionFloat]) -> Optional[PrecisionFloat]:
        if not self._existRoot:
            return None

        a = PrecisionFloat(f'{interval[1]}', PrecisionFloat.getDps())
        b = PrecisionFloat(f'{interval[0]}', PrecisionFloat.getDps())
        aproximateRoot: PrecisionFloat = PrecisionFloat(
            '0.0', PrecisionFloat.getDps())

        fun: Function = self._function

        if fun.getAbsImage(a) < self._errorPrecisionFloat:
            return a
        if fun.getAbsImage(b) < self._errorPrecisionFloat:
            return b

        while True:
            self._cauntIteration += 1
            aproximateRoot = self.__getAproximateRoot(
                b, a)
            absImageValue = fun.getAbsImage(aproximateRoot)

            self._iterationValues.append(
                [self._cauntIteration, b, a, aproximateRoot, absImageValue,
                    self._errorPrecisionFloat]
            )

            if absImageValue < self._errorPrecisionFloat:
                break

            if super()._testInterval(b, aproximateRoot):
                a = aproximateRoot
            else:
                b = aproximateRoot
            pass
        return super()._PrecisionFloatTruncate(aproximateRoot)

    def __getAproximateRoot(self, numB: PrecisionFloat,
                            numA: PrecisionFloat) -> PrecisionFloat:
        fun: Function = self._function

        aux1 = numB * fun.getImage(numA) - numA * fun.getImage(numB)
        aux2 = fun.getImage(numA) - fun.getImage(numB)
        return aux1 / aux2


class FixedPointMethodRootSolver(BaseRootSolver):
    def solve(self) -> Optional[list[SearchData]]:
        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        dataList: list[SearchData] = []
        for intervals in listInterval:
            super()._initializeVariables()
            data = SearchData(
                self.__getZeroFunction(intervals),
                self._cauntIteration,
                self._iterationValues
            )
            dataList.append(data)

            pass
        return dataList

    def _initializeVariables(self, expStr: str, interval: Optional[list[float]],
                             listExpGx: list[str],
                             error: int):
        super()._initializeVariables(expStr, interval, error)
        self.__funGx = self.__getExpThatConverges(listExpGx)

        pass

    def __getExpThatConverges(self, listExpGx: list[str]) -> Optional[Function]:
        for exp in listExpGx:
            fun = Function(exp)

            img_a = fun.getImageOfDerivate(self._xA)
            img_b = fun.getImageOfDerivate(self._xB)

            if not img_a == None and not img_b == None:
                if abs(img_a) < 1 and abs(img_b) < 1:
                    return fun
            pass
        return None

    def __getZeroFunction(self, interval: list[PrecisionFloat]) -> Optional[PrecisionFloat]:
        hypothesis = (interval[0] + interval[1]) / \
            PrecisionFloat('2', PrecisionFloat.getDps())

        fun: Function = self._function
        funGx: Function = self.__funGx

        currentX: PrecisionFloat = hypothesis
        while True:
            self._cauntIteration += 1
            absImageValue = fun.getAbsImage(currentX)

            if absImageValue < self._errorPrecisionFloat:
                return currentX

            nextX = funGx.getImage(currentX)

            # print(f'X{self._cauntIteration} = {currentX} : {funGx}'
            #       + f' => X{self._cauntIteration+1} = {nextX}'
            #       + f' # Imagem: {absImageValue} < {self._errorPrecisionFloat}')

            self._iterationValues.append(
                [self._cauntIteration, currentX, absImageValue,
                 self._errorPrecisionFloat, nextX
                 ]
            )

            currentX = nextX
            pass
        return None
