from jjpine.tool.indicator import Indicator as JJIndicator

class Filter:
    def __init__(self):
        self._indicator = JJIndicator()

    def _update_ema(self, ema, partial_data, ema_multiplier):
        if (not partial_data) or (not all([isinstance(value, (int, float)) for value in partial_data])):
            ema.append(None)
        elif ema[-1] is None:
            ema.append(self._indicator.get_sma(partial_data))
        else:
            ema.append(self._indicator.get_ema(ema_multiplier, ema[-1], partial_data[-1]))
        return ema

    def get_macd_histogram_filter(self, data, ema1_period, ema1_multiplier, ema2_period, ema2_multiplier, ema_macd_period, ema_macd_multiplier):
        ema1 = list()
        ema2 = list()
        macd = list()
        ema_macd = list()
        macd_histogram = list()
        filter_result = list()
        for i, value in enumerate(data):
            self._update_ema(ema1, data[i - ema1_period + 1 : i + 1], ema1_multiplier)
            self._update_ema(ema2, data[i - ema2_period + 1 : i + 1], ema2_multiplier)
            if ema1[-1] and ema2[-1]:
                macd.append(self._indicator.get_macd(ema1[-1], ema2[-1]))
            else:
                macd.append(None)
            self._update_ema(ema_macd, macd[i - ema_macd_period + 1 : i + 1], ema_macd_multiplier)
            if macd[-1] and ema_macd[-1]:
                macd_histogram.append(self._indicator.get_macd_histogram(macd[-1], ema_macd[-1]))
            else:
                macd_histogram.append(None)
            if len(macd_histogram) < 2:
                filter_result.append(None)
            elif macd_histogram[-1] and macd_histogram[-2]:
                filter_result.append(macd_histogram[-1] >= macd_histogram[-2])
            else:
                filter_result.append(None)
        return filter_result
