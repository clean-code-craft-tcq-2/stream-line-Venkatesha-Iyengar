import sys

def ReadDataFromConsoleAndPrintStatistics():
  DataReadFromConsole = ReadBatteryParameterDataFromConsole()
  for Parameter in BatteryParameters:
    RangeOfDataRead = FindRangeFromDataRead(DataReadFromConsole)
    MovingAvgOfDataRead = FindMovingAverageOfDataRead(DataReadFromConsole)
    printStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead)
