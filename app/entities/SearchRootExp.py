from .BaseRootSolver import BisectionMethodRootSolver
from typing import Optional
from .PrecisionFloat import PrecisionFloat


class SearchRootExp:
    __cauntIteration: int = 0

    @staticmethod
    def getQuantIteraion() -> int:
        return SearchRootExp.__cauntIteration

    @staticmethod
    def bisectionMethod(expStr: str,
                        interval: Optional[list[float]],
                        error: int) -> Optional[list[PrecisionFloat]]:
        bisectionmethod = BisectionMethodRootSolver()
        root = bisectionmethod.solve(expStr, interval, error)
        SearchRootExp.__cauntIteration = BisectionMethodRootSolver.getQuantIteraion()
        return root
    pass
