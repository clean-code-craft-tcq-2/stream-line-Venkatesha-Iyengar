import sys
from signal import signal, SIGPIPE, SIG_DFL 

BatteryParameters = ["Current Readings in milliAmps", "Temperature Readings in Farenheit"]

def ReadBatteryParameterDataFromConsole():
    signal(SIGPIPE,SIG_DFL)
    LinesRead = sys.stdin.readlines()
    StrippedData = []
    for Reading in LinesRead:
      Reading = Reading.strip('\n')
      ReadingList = list(map(float,Reading.split(',')))
      StrippedData.append(ReadingList)
    return StrippedData

def FindRangeFromDataRead(Data):
    MinimumValueAmongData = min(Data,default="NULL")
    MaximumValueAmongData = max(Data,default="NULL")
    return {'Minimum value of the parameter': MinimumValueAmongData, 'Maximum value of the parameter': MaximumValueAmongData}

def FindMovingAverageOfDataRead(DataReadFromConsole):
    DataStream = [DataReadFromConsole[index : index + 5] for index, value in enumerate(DataReadFromConsole) if index < len(DataReadFromConsole) - 5 + 1]
    MovingAvgOfDataRead = [round(sum(Data)/len(Data), 2) for Data in DataStream]
    return MovingAvgOfDataRead

def PrintStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead):
  StringToBePrinted = f'{Parameter}:{RangeOfDataRead},{MovingAvgOfDataRead}'
  print(StringToBePrinted)

def ReadDataFromConsoleAndPrintStatistics():
  DataReadFromConsole = ReadBatteryParameterDataFromConsole()
  for Parameter in BatteryParameters:
    RangeOfDataRead = FindRangeFromDataRead(DataReadFromConsole)
    MovingAvgOfDataRead = FindMovingAverageOfDataRead(DataReadFromConsole)
    PrintStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead)
