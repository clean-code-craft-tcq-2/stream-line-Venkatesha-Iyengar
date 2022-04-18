import unittest
from receiver import *

class tdd_receiver_test(unittest.TestCase):
    def Test_Range_Receiver(self):
        AverageDataSize = 5
        DataReadFromConsole = [10,20,30,40,0,21,47,99,12]
        ReadDataFromConsoleAndPrintStatistics(AverageDataSize)
        RangeOfDataRead = FindRangeFromDataRead(Data)
       # self.assertEqual(RangeOfDataRead,{'Minimum value of the parameter': 0, 'Maximum value of the parameter': 99})
        
    def Test_MovingAverage_Receiver(self):
        AverageDataSize = 5
        DataReadFromConsole = [10,20,30,40,0]
        MovingAvergae = FindMovingAverageOfDataRead(DataReadFromConsole,AverageDataSize)
        self.assertEqual(MovingAvergae,[20])
    
        
unittest.main()
