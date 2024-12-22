from .BaseRootSolver import BisectionMethodRootSolver
from typing import Optional
from .PrecisionFloat import PrecisionFloat


class SearchData:
    def __init__(self, root: PrecisionFloat,
                 quantIteration: int,
                 valuesPerIteration: list[list[PrecisionFloat]]):
        self.root: PrecisionFloat = root
        self.quantIteration: int = quantIteration
        self.valuesPerIteration: list[list[PrecisionFloat]
                                      ] = valuesPerIteration
        pass
    pass


class SearchRootExp:

    @staticmethod
    def bisectionMethod(expStr: str,
                        interval: Optional[list[float]],
                        error: int) -> Optional[SearchData]:
        bisectionmethod = BisectionMethodRootSolver()

        root = bisectionmethod.solve(expStr, interval, error)
        quantIteration = bisectionmethod.getQuantIteration()
        valuesPerIteration = bisectionmethod.getIterationValues()

        return SearchData(root, quantIteration, valuesPerIteration)
    pass
