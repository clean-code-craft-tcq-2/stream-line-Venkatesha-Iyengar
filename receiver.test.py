import unittest
from receiver import *

class tdd_senderToReceiver_test(unittest.TestCase):
    def test_senderToReceiver(self):
        AverageDataSize = 5
        DataReadFromConsole = [10,20,30,40,0]
        ReadDataFromConsoleAndPrintStatistics(AverageDataSize)
        MovingAvergae = FindMovingAverageOfDataRead(DataReadFromConsole,AverageDataSize)
        self.assertEqual(MovingAvergae,[20])
    
unittest.main()
