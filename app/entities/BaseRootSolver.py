from .Math import Function
from .PrecisionFloat import PrecisionFloat
from typing import Optional


class BaseRootSolver:
    _xA: PrecisionFloat = PrecisionFloat('0.0', PrecisionFloat.getDps())
    _xB: PrecisionFloat = PrecisionFloat('0.0', PrecisionFloat.getDps())
    _function: Function = None

    _errorPrecisionFloat: PrecisionFloat = None
    _errorInt: int = 5
    _existRoot: bool = True
    _cauntIteration: int = 0
    _iterationValues: list[list[PrecisionFloat]] = []

    @staticmethod
    def getQuantIteraion() -> int:
        return BaseRootSolver._cauntIteration

    @staticmethod
    def getIterationValues() -> list[list[PrecisionFloat]]:
        return BaseRootSolver._iterationValues

    @staticmethod
    def _testInterval(xB: PrecisionFloat, xA: PrecisionFloat) -> bool:
        fun = BaseRootSolver._function

        fA = fun.getImage(xA)
        fB = fun.getImage(xB)
        return (fA * fB) < PrecisionFloat('0', PrecisionFloat.getDps())

    @staticmethod
    def _PrecisionFloatTruncate(number: PrecisionFloat) -> PrecisionFloat:
        return round(number, BaseRootSolver._errorInt)

    @staticmethod
    def _initializeVariables(expStr: str,
                             interval: Optional[list[float]],
                             error: int):
        BaseRootSolver._errorPrecisionFloat = PrecisionFloat(
            '10', PrecisionFloat.getDps()) ** PrecisionFloat(str(-error), PrecisionFloat.getDps())

        BaseRootSolver._xA = PrecisionFloat(
            str(interval[1]), PrecisionFloat.getDps())
        BaseRootSolver._xB = PrecisionFloat(
            str(interval[0]), PrecisionFloat.getDps())

        if BaseRootSolver._xA < BaseRootSolver._xB:
            aux = BaseRootSolver._xA
            BaseRootSolver._xA = BaseRootSolver._xB
            BaseRootSolver._xB = aux
            pass

        BaseRootSolver._function = Function(expStr)
        BaseRootSolver._existRoot = True
        BaseRootSolver._cauntIteration = 0
        BaseRootSolver._errorInt = error
        pass

    @staticmethod
    def _adjustIntervalIfNotImageExist() -> None:
        if not BaseRootSolver._existRoot:
            return
        fun = BaseRootSolver._function
        xA = BaseRootSolver._xA
        xB = BaseRootSolver._xB

        if fun.getImage(xA):
            xA -= BaseRootSolver._errorPrecisionFloat
        if fun.getImage(xB):
            xB += BaseRootSolver._errorPrecisionFloat

        BaseRootSolver._xA = xA
        BaseRootSolver._xB = xB
        pass
    pass

    @staticmethod
    def _checkAndFindInterval() -> list[list[PrecisionFloat]]:
        xA = BaseRootSolver._xA
        xB = BaseRootSolver._xB

        listInterval: list[list[PrecisionFloat]] = []
        if BaseRootSolver._testInterval(xA, xB):
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

        fun = self._function

        if fun.getAbsImage(a) < self._errorPrecisionFloat:
            return a
        if fun.getAbsImage(b) < self._errorPrecisionFloat:
            return b

        while True:
            self._cauntIteration += 1
            aproximateRoot = self.__getAproximateRoot(
                b, a)
            absImageValue = fun.getAbsImage(aproximateRoot)

            print(f'[{b}, {a}] => {aproximateRoot} : '
                  + f'{absImageValue} > '
                  + f'{self._errorPrecisionFloat}')

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
    @staticmethod
    def solve(expStr: str,
              interval: Optional[list[float]],
              error: int) -> Optional[PrecisionFloat]:
        if not expStr:
            return None
        if not isinstance(error, int):
            raise ValueError('erro não pode ser diferente de int.')
        if error <= 0:
            raise ValueError('error não pode ser 0 ou negativo.')

        FalsePositionMethodRootSolver.__initializeVariables(
            expStr, interval, error)
        return

    @staticmethod
    def __initializeVariables(expStr: str,
                              interval: Optional[list[float]],
                              error: int):
        super().__initializeVariables(expStr, interval, error)
        pass

    @staticmethod
    def __getAproximateRootFalsePosition(numB: PrecisionFloat,
                                         numA: PrecisionFloat) -> PrecisionFloat:
        fun = super().__function

        aux1 = numB * fun.getImage(numA) - numA * fun.getImage(numB)
        aux2 = fun.getImage(numA) - fun.getImage(numB)
        return aux1 / aux2


class FixedPointMethodRootSolver(BaseRootSolver):
    @staticmethod
    def solve():
        return
