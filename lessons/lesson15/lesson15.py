class Elements:
    def __init__(self, melting_temp, vaporization_temp):
        self.melting_temp = melting_temp
        self.vaporization_temp = vaporization_temp

    def temp_converter(self, temperature, scale_type):
        # adjusting temperature from Kelvin or Fahrenheit to Celsius
        if scale_type == 'K':
            temperature -= 273
        elif scale_type == 'F':
            temperature = (temperature - 32) * 5 / 9
        return temperature

    def matter_state(self, temperature, scale_type):
        # determining and printing the matter state
        temperature = self.temp_converter(temperature, scale_type)
        if temperature < self.melting_temp:
            print("State is solid")
        elif temperature <= self.vaporization_temp:
            print("State is liquid")
        else:
            print("State is gaseous")


# class Iron(Elements):
#     melting_temp = 1538
#     vaporization_temp = 2862


# class Chlorine(Elements):
#     melting_temp = -101.5
#     vaporization_temp = -34.04


# class Oxygen(Elements):
#     melting_temp = -218.8
#     vaporization_temp = -183


iron = Elements(1538, 2862)
chlorine = Elements(-101.5, -34.04)
oxygen = Elements(-218.8, -183)

iron.matter_state(1600, 'K')
chlorine.matter_state(1600, 'C')
oxygen.matter_state(1600, 'F')
