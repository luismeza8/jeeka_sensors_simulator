import pandas as pd

class PocketQubeSimulator:
    simulated_data = pd.read_csv('datos_corregidos.csv')
    iteration_data = 0
    trama = {
        'beginnig': 0xff,
        'source_address': None,
        'destine_address': None,
        'lenght': None,
        'rssi': None,
        'instruccion': None,
        'message': None,
        'end': 0xef
    }
    instructions = {
        # Acctions
        'str': None, 
        'abr': None,
        'rst': None,
        'fin': None,
        # Data
        'ori': None,#generate_orientation,
        'alt': None,#generate_altitude,
        'vel': None,#generate_velocity,
        'acl': None,#generate_acelerations,
        'tem': None,#generate_temperature,
        'pre': None,#generate_pressure,
        'pos': None,#generate_position,
        'bat': None,#generate_battery,
        'pha': None,#generate_phase,
        'all': None,#generate_all_data,
    }

#    def generate_orientation(self):
#        return [self.csv_data['gx'].loc[self.iteration], self.csv_data['gy'].loc[self.iteration], self.csv_data['gz'].loc[self.iteration]]
#
#    def generate_altitude(self):
#        return self.csv_data['altura'].loc[self.iteration]
#
#    def generate_velocity(self):
#        return self.csv_data[''].loc[self.iteration]
#
#    def generate_acelerations(self):
#        return [self.csv_data['ax'].loc[self.iteration], self.csv_data['ay'].loc[self.iteration], self.csv_data['az'].loc[self.iteration]]
#
#    def generate_temperature(self):
#        return self.csv_data['temperatura'].loc[self.iteration]
#
#    def generate_pressure(self):
#        return self.csv_data['presion'].loc[self.iteration]
#
#    def generate_position(self):
#        return [random.uniform(-40, 40), random.uniform(-40, 40)]
#
#    def generate_battery(self):
#        return random.randint(0, 100)
#
#    def generate_phase(self):
#        return random.randint(0, 3)
#
#    def get_medition(self):
#        return self.csv_data['medicion'].loc[self.iteration]
#
#    def get_time(self):
#        return self.csv_data['tiempo'].loc[self.iteration]
#
#    def generate_all_data(self):
#        self.iteration += 1
#        return [
#            self.get_medition(),
#            self.get_time(),
#            self.generate_altitude(),
#            self.generate_temperature(),
#            self.generate_pressure(),
#            self.generate_acelerations(), 
#            self.generate_orientation(),
#            #generate_velocity(),
#            #generate_position(),
#            #generate_battery(),
#            #generate_phase()
#        ]
#
#    instructions = {
#        # Acctions
#        'str': None, 
#        'abr': None,
#        'rst': None,
#        'fin': None,
#        # Data
#        'ori': generate_orientation,
#        'alt': generate_altitude,
#        'vel': generate_velocity,
#        'acl': generate_acelerations,
#        'tem': generate_temperature,
#        'pre': generate_pressure,
#        'pos': generate_position,
#        'bat': generate_battery,
#        'pha': generate_phase,
#        'all': generate_all_data,
#    }
