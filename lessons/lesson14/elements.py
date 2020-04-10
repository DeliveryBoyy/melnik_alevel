class Element:
    def __init__(self, temperature_melting, temperature_boiling):
        self.temperature_melting = temperature_melting
        self.temperature_boiling = temperature_boiling

    def agg_state(self, temperature, scale):
        temperature = self.convert_to_c(temperature, scale)
        if temperature >= self.temperature_boiling:
            return 'Gas'
        elif temperature >= self.temperature_melting:
            return 'Liquid'
        else:
            return 'Solid'

    def convert_to_c(self, temperature, scale):
        if scale == 'K':
            temperature += 273
        return temperature


def run():
    oxygen = Element(-218, -182)
    print(oxygen.agg_state(-300, 'C'))
    print(oxygen.agg_state(-300, 'K'))
    print(oxygen.agg_state(-200, 'C'))
    print(oxygen.agg_state(69, 'C'))
    iron = Element(temperature_melting=1538, temperature_boiling=2862)



run()
