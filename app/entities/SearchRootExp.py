from .BaseRootSolver import *
from typing import Optional
from .PrecisionFloat import PrecisionFloat


class SearchRootExp:
    @staticmethod
    def bisectionMethod(expStr: str,
                        interval: Optional[list[float]],
                        error: int) -> Optional[list[SearchData]]:
        bisectionmethod = BisectionMethodRootSolver(expStr, interval, error)

        return bisectionmethod.solve()

    @staticmethod
    def falsePositionMetho(expStr: str,
                           interval: Optional[list[float]],
                           error: int) -> Optional[SearchData]:
        falsePosition = FalsePositionMethodRootSolver(expStr, interval, error)

        # root =
        # quantIteration = falsePosition.getQuantIteration()
        # valuesPerIteration = falsePosition.getIterationValues()

        return falsePosition.solve()

    @staticmethod
    def fixedPointMethod(expStr: str, interval: Optional[list[float]],
                         listExpGx: list[str],
                         error: int) -> Optional[PrecisionFloat]:
        fixedPoint = FixedPointMethodRootSolver()

        root = fixedPoint.solve(expStr, interval, listExpGx, error)
        quantIteration = fixedPoint.getQuantIteration()
        valuesPerIteration = fixedPoint.getIterationValues()

        return SearchData(root, quantIteration, valuesPerIteration)
