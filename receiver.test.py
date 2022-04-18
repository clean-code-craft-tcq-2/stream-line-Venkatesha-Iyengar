import unittest
from receiver import *

class tdd_receiver_test(unittest.TestCase):
    def test_receiver(self):
        AverageDataSize = 5
        ReadDataFromConsoleAndPrintStatistics(AverageDataSize)
    
unittest.main()
