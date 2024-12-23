from .BaseRootSolver import *
from typing import Optional
from .PrecisionFloat import PrecisionFloat


class SearchRootExp:
    @staticmethod
    def bisectionMethod(expStr: str,
                        interval: Optional[list[float]],
                        error: int) -> Optional[list[SearchData]]:
        bisectionmethod = BisectionMethodRootSolver(expStr, interval, error)

        return bisectionmethod.solve(expStr, interval, error)

    @staticmethod
    def falsePositionMetho(expStr: str,
                           interval: Optional[list[float]],
                           error: int) -> Optional[SearchData]:
        falsePosition = FalsePositionMethodRootSolver()

        root = falsePosition.solve(expStr, interval, error)
        quantIteration = falsePosition.getQuantIteration()
        valuesPerIteration = falsePosition.getIterationValues()

        return SearchData(root, quantIteration, valuesPerIteration)

    @staticmethod
    def fixedPointMethod(expStr: str, interval: Optional[list[float]],
                         listExpGx: list[str],
                         error: int) -> Optional[PrecisionFloat]:
        fixedPoint = FixedPointMethodRootSolver()

        root = fixedPoint.solve(expStr, interval, listExpGx, error)
        quantIteration = fixedPoint.getQuantIteration()
        valuesPerIteration = fixedPoint.getIterationValues()

        return SearchData(root, quantIteration, valuesPerIteration)
