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

def FindMovingAverageOfDataRead(DataReadFromConsole,AverageDataSize):
    DataStream = [DataReadFromConsole[index : index + AverageDataSize] for index, value in enumerate(DataReadFromConsole) if index < len(DataReadFromConsole) - AverageDataSize + 1]
    MovingAvgOfDataRead = [round(sum(Data)/len(Data), 2) for Data in DataStream]
    return MovingAvgOfDataRead

def ExtractBatteryParametersReadFromConsole(DataRead, BatteryParameter):
    for index, Parameter in enumerate(BatteryParameters):
        if Parameter == BatteryParameter:
            return [BatteryParameterValue[index] for BatteryParameterValue in DataRead]

def PrintStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead):
  StringToBePrinted = f'{Parameter}:{RangeOfDataRead}'
  print(StringToBePrinted)
  print('Moving average', MovingAvgOfDataRead)

def ReadDataFromConsoleAndPrintStatistics(AverageDataSize):
  DataReadFromConsole = ReadBatteryParameterDataFromConsole()
  for Parameter in BatteryParameters:
    ExtractedDataReadFromConsole = ExtractBatteryParametersReadFromConsole(DataReadFromConsole, Parameter)
    RangeOfDataRead = FindRangeFromDataRead(ExtractedDataReadFromConsole)
    MovingAvgOfDataRead = FindMovingAverageOfDataRead(ExtractedDataReadFromConsole, AverageDataSize)
    PrintStatisticsOnConsole(Parameter,RangeOfDataRead,MovingAvgOfDataRead)
