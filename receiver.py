import sys

BatteryParameters = ["Current Readings in milliAmps", "Temperature Readings in Farenheit"]

def ReadBatteryParameterDataFromConsole():
    LinesRead = sys.stdin.readlines()
    return LinesRead  
  
def ReadDataFromConsoleAndPrintStatistics():
  DataReadFromConsole = ReadBatteryParameterDataFromConsole()
  for Parameter in BatteryParameters:
    RangeOfDataRead = FindRangeFromDataRead(DataReadFromConsole)
    MovingAvgOfDataRead = FindMovingAverageOfDataRead(DataReadFromConsole)
    printStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead)
