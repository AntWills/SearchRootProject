from sympy import Float


class PrecisionFloat(Float):

    __dpsInstance = 24

    @staticmethod
    def setDps(dps: int) -> None:
        PrecisionFloat.__dpsInstance = dps
        pass

    @staticmethod
    def getDps() -> int:
        return PrecisionFloat.__dpsInstance

    # def __new__(cls, num, dps=..., precision=...):
    #     # dps = PrecisionFloat.__dpsInstance
    #     quant = PrecisionFloat.__countDigits(Float(num))

    #     if dps is not None:
    #         return super().__new__(cls, num, dps=(dps + quant))
    #     elif precision is not None:
    #         return super().__new__(cls, num, precision=precision)
    #     else:
    #         return super().__new__(cls, num)

    def __init__(self, num, dps=15, precision=...):
        self.__dps = dps
        self.__quantDigitsBeforeDecimal = PrecisionFloat.__countDigits(
            Float(num))
        super().__init__()

    # def getDps(self) -> int:
    #     return self.__dps

    # def getQDBD(self) -> int:
    #     '''
    #     numero de casas decimais antes do ponto
    #     '''
    #     return self.__quantDigitsBeforeDecimal

    # def superEvalf(self, n=15, subs=None, maxn=100, chop=False, strict=False, quad=None, verbose=False):
    #     return super().evalf(n, subs, maxn, chop, strict, quad, verbose)

    def evalf(self, n=15, subs=None, maxn=100, chop=False, strict=False, quad=None, verbose=False):
        quant = PrecisionFloat.__countDigits(self)
        n = (quant + n)
        # print('Aqui 02')
        return super().evalf(n, subs, maxn, chop, strict, quad, verbose)
    pass

    # def truncate(self, dps):
    #     """Retorna um valor truncado na quantidade de dígitos desejada."""
    #     factor = Float(10) ** dps
    #     truncated_val = int(str(self * factor)) / factor
    #     return PrecisionFloat(truncated_val, dps)

    @staticmethod
    def __countDigits(n: Float):
        if not isinstance(n, Float):
            n = Float(n)
        integerPart = str(n).split('.')[0]
        return len(integerPart) if integerPart != '0' else 0
