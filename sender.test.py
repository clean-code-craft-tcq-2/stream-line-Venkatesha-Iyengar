import unittest
import time
from sender import *
from BatteryManagementSystem import *

class tdd_sender_test(unittest.TestCase):
    #Tests for Battery Management System
    def test_D2A_Converter(self):
        d2a_object1 = D2A_Conerter(no_bits=12)
        d2a_object2 = D2A_Conerter(no_bits=10,flag_signed=True)
        
        #Test for maximum value
        self.assertEqual(d2a_object1.get_maximum_value(),4095)
        self.assertEqual(d2a_object2.get_maximum_value(),1023)

        #Test for digital value
        self.assertEqual(d2a_object1.get_absolute_current_ampere_value(0,max_current_in_amps=10),0)
        self.assertEqual(d2a_object2.get_absolute_current_ampere_value(0,max_current_in_amps=15),15)

    def test_Temperature_Converter(self):
        temp_conv_object = Temperature_Converter()
        #Test for conversion
        self.assertEqual(temp_conv_object.convert_farenheit_to_celcius(100),37.77777777777778)
        self.assertEqual(temp_conv_object.convert_farenheit_to_celcius(0),-17.77777777777778)

        self.assertEqual(temp_conv_object.convert_celcius_to_farenheit(100),237.6)
        self.assertEqual(temp_conv_object.convert_celcius_to_farenheit(0),57.6)

    #Tests for sender
    def test_send_data_to_console(self):
        Sender_object = Sender()
        self.assertEqual(Sender_object.send_data_to_console("All is well!"), "All is well!")

    #Tests for sending simulated data
    def test_send_simulated_parameter_data_to_console(self):
        Sender_object = Sender()
        self.assertTrue(Sender_object.send_parameter_readings())

    #Tests for sending data from file
    def test_send_generated_parameter_data_to_console(self):
        Sender_object = Sender(False, 'current_data.txt', 'temperature_data.txt')
        self.assertTrue(Sender_object.send_parameter_readings())
    
unittest.main()
