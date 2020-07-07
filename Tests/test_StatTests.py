import unittest
from StatCalculator.Statistics import Statistics
from CSVReader.CSVReader import CSVReader
from pprint import pprint



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Statistics = Statistics()

    # To test instantiation of calculator class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    #Testing mode
    def test_mean(self):
        test_data = CSVReader('/Tests/Data_Statistics/Mean_Data.csv').data
        for row in test_data:
            self.assertEqual(self.Statistics.mean(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Mean']))
            self.assertEqual(self.Statistics.result, float(row['Mean']))
        test_data.clear()
