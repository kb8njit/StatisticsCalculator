from Calculator.Calculator import Calculator
from StatCalculator.Mean import mean
from StatCalculator.Median import median
from StatCalculator.Mode import mode
from StatCalculator.Variance import variance
from StatCalculator.StandardDev import stand_dev
from StatCalculator.ZScore import z_score


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stand_dev(self, data):
        self.result = stand_dev(data)
        return self.result

    def z_score(self, data):
        self.result = z_score(data)
        return self.result

    pass
