import unittest
from receiver import *

class tdd_receiver_test(unittest.TestCase):
    def test_receiver(self):
        AverageDataSize = 5
        DataReadFromConsole = [10,20,30,40,0]
        ReadDataFromConsoleAndPrintStatistics(AverageDataSize)
        MovingAvergae = FindMovingAverageOfDataRead(DataReadFromConsole,AverageDataSize):
        self.assertEqual(MovingAvergae,30)
    
unittest.main()
