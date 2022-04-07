import sys
from BatteryManagementSystem import *
import random

Stream_Data_Limit = 50

class Sender:
    def __init__(self, simulate_parameter=True, current_parameter_readings_file = None, temperature_parameter_readings_file = None):
        self.simulate_parameter = simulate_parameter
        self.current_parameter_readings_file= current_parameter_readings_file
        self.temperature_parameter_readings_file = temperature_parameter_readings_file
        self.current_values_amperes = []
        self.temperature_values = []
        
    def send_data_to_console(self,data_to_write):
        sys.stdout.write(data_to_write+'\n')
        #print(data_to_write)
        return data_to_write

    def send_parameter_readings(self):
        self.get_parameter_readings()
        for data_index in range(Stream_Data_Limit):
            self.send_data_to_console(f'{self.current_values_amperes[data_index]},{self.temperature_values[data_index]}')
        return True

    def get_parameter_readings(self):
        if self.simulate_parameter:
            self.simulate_sensor_data()
            return
        self.read_parameter_readings_from_file()
        return

    def simulate_sensor_data(self):
        d2a_object = D2A_Conerter(no_bits=12)
        temp_conv_object = Temperature_Converter()
        
        for data_index in range(Stream_Data_Limit):
            self.current_values_amperes.append(d2a_object.get_absolute_current_ampere_value(random.randrange(0, 4095),max_current_in_amps=10))
            self.temperature_values.append(temp_conv_object.convert_celcius_to_farenheit(random.randrange(0, 150)))

    def read_parameter_readings_from_file(self):
        d2a_object = D2A_Conerter(no_bits=12)
        temp_conv_object = Temperature_Converter()
        
        with open (self.current_parameter_readings_file, 'r') as f_current_readings:
            for current_reading in f_current_readings:
                self.current_values_amperes.append(d2a_object.get_absolute_current_ampere_value(int(current_reading), max_current_in_amps=10))

        with open (self.temperature_parameter_readings_file, 'r') as f_temp_readings:
            for temp_reading in f_temp_readings:
                self.temperature_values.append(temp_conv_object.convert_celcius_to_farenheit(int(temp_reading)))

        
            
            
            
    


    
    
    
