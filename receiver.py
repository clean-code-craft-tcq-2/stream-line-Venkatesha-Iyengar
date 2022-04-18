import sys

BatteryParameters = ["Current Readings in milliAmps", "Temperature Readings in Farenheit"]

def ReadBatteryParameterDataFromConsole():
    LinesRead = sys.stdin.readlines()
    return LinesRead  

def FindRangeFromDataRead(Data):
    minimumValueAmongData = min(Data,default="NULL")
    minimumValueAmongData = max(Data,default="NULL")
    return {'Minimum value of the parameter': MinimumValueAmongData, 'Maximum value of the parameter': MaximumValueAmongData}

def ReadDataFromConsoleAndPrintStatistics():
  DataReadFromConsole = ReadBatteryParameterDataFromConsole()
  for Parameter in BatteryParameters:
    RangeOfDataRead = FindRangeFromDataRead(DataReadFromConsole)
    MovingAvgOfDataRead = FindMovingAverageOfDataRead(DataReadFromConsole)
    printStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead)
