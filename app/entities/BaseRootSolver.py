from .Math import Function
from .PrecisionFloat import PrecisionFloat
from typing import Optional


class BaseRootSolver:
    def __init__(self):
        # Atributos de instância
        self._xA: PrecisionFloat = PrecisionFloat(
            '0.0', PrecisionFloat.getDps())
        self._xB: PrecisionFloat = PrecisionFloat(
            '0.0', PrecisionFloat.getDps())
        self._function: Function = None

        self._errorPrecisionFloat: PrecisionFloat = None
        self._errorInt: int = 5
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

    def _initializeVariables(self, expStr: str, interval: Optional[list[float]], error: int):
        self._errorPrecisionFloat = PrecisionFloat(
            '10', PrecisionFloat.getDps()) ** PrecisionFloat(str(-error), PrecisionFloat.getDps())

        self._xA = PrecisionFloat(
            str(interval[1]), PrecisionFloat.getDps())
        self._xB = PrecisionFloat(
            str(interval[0]), PrecisionFloat.getDps())

        if self._xA < self._xB:
            aux = self._xA
            self._xA = self._xB
            self._xB = aux

        self._function = Function(expStr)
        self._existRoot = True
        self._cauntIteration = 0
        self._errorInt = error

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
        if self._testInterval(xA, xB):
            listInterval.append([xB, xA])
            return listInterval
        return listInterval


class BisectionMethodRootSolver(BaseRootSolver):
    def solve(self, expStr: str,
              interval: Optional[list[float]],
              error: int) -> Optional[PrecisionFloat]:

        if not expStr:
            return None
        if not isinstance(error, int):
            raise ValueError('erro não pode ser diferente de int.')
        if error <= 0:
            raise ValueError('error não pode ser 0 ou negativo.')

        super()._initializeVariables(
            expStr, interval, error)
        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        rootList: list[PrecisionFloat] = []
        for intervals in listInterval:
            rootList.append(
                self.__getZeroFunction(intervals))
            pass
        return rootList

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
    def solve(self, expStr: str,
              interval: Optional[list[float]],
              error: int) -> Optional[PrecisionFloat]:
        if not expStr:
            return None
        if not isinstance(error, int):
            raise ValueError('erro não pode ser diferente de int.')
        if error <= 0:
            raise ValueError('error não pode ser 0 ou negativo.')

        super()._initializeVariables(
            expStr, interval, error)
        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        rootList: list[PrecisionFloat] = []
        for intervals in listInterval:
            rootList.append(
                self.__getZeroFunction(intervals))
            pass
        return rootList

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

    def __getAproximateRoot(self, numB: PrecisionFloat,
                            numA: PrecisionFloat) -> PrecisionFloat:
        fun: Function = self._function

        aux1 = numB * fun.getImage(numA) - numA * fun.getImage(numB)
        aux2 = fun.getImage(numA) - fun.getImage(numB)
        return aux1 / aux2


class FixedPointMethodRootSolver(BaseRootSolver):
    def solve(self, expStr: str, interval: Optional[list[float]],
              listExpGx: list[str],
              error: int) -> Optional[PrecisionFloat]:
        if not expStr:
            return None
        if not isinstance(error, int):
            raise ValueError('erro não pode ser diferente de int.')
        if error <= 0:
            raise ValueError('error não pode ser 0 ou negativo.')

        self._initializeVariables(expStr, interval, listExpGx, error)

        if self.__funGx == None:
            return None

        super()._adjustIntervalIfNotImageExist()
        listInterval = super()._checkAndFindInterval()

        rootList: list[PrecisionFloat] = []
        for intervals in listInterval:
            rootList.append(
                self.__getZeroFunction(intervals))
            pass
        return rootList

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
