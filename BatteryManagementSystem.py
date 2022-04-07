class D2A_Conerter:
    def __init__(self, no_bits, flag_signed = False):
        self.number_of_bits = no_bits
        self.flag_is_signed = flag_signed
        self.max_possible_digital_value = self.get_maximum_value()

    def get_maximum_value(self):
        return pow(2,self.number_of_bits)-1

    def get_absolute_current_ampere_value(self, digital_value, max_current_in_amps):
        self.max_possible_current = max_current_in_amps
        if self.flag_is_signed:
            return (abs(round((self.max_possible_current/(self.max_possible_digital_value/2))*(digital_value-self.max_possible_digital_value/2))))
        return (abs(round((self.max_possible_current/self.max_possible_digital_value)*digital_value)))

class Temperature_Converter:
    #Pure Functions to convert between different units
    def convert_farenheit_to_celcius(self,farenheit):
        return ((farenheit - 32) * 5 / 9)

    def convert_celcius_to_farenheit(self,celcius):
        return ((celcius + 32) * 9 / 5)

    
