
class Indicator:
    def __init__(self):
        pass

    def get_sma(self, data):
        """
        simple moving average
        """
        return sum(data) / len(data)

    def get_ema(self, multiplier, prev_ema, current_value):
        """
        get_exponential_moving_average
        """
        return multiplier * current_value + (1 - multiplier) * prev_ema

    def get_macd(self, ema1, ema2):
        return ema1 - ema2

    def get_macd_histogram(self, macd, ema_macd):
        return macd - ema_macd
