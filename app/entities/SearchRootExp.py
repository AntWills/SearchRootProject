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
                           error: int) -> Optional[list[SearchData]]:
        falsePosition = FalsePositionMethodRootSolver(expStr, interval, error)

        return falsePosition.solve()

    @staticmethod
    def fixedPointMethod(expStr: str, interval: Optional[list[float]],
                         listExpGx: list[str],
                         error: int) -> Optional[list[SearchData]]:
        fixedPoint = FixedPointMethodRootSolver(
            expStr, interval, listExpGx, error)

        return fixedPoint.solve()
