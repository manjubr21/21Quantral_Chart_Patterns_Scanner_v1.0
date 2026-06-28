"""
===============================================================================
Indicator Cache Keys
===============================================================================
"""


class IndicatorKey:

    @staticmethod
    def sma(period: int):

        return f"SMA:{period}"

    @staticmethod
    def ema(period: int):

        return f"EMA:{period}"

    @staticmethod
    def rsi(period: int):

        return f"RSI:{period}"

    @staticmethod
    def atr(period: int):

        return f"ATR:{period}"