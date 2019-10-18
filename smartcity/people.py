from .utils import estimate_beta_parameters

class People:
    def __init__(self, pollution_pref, nuclear_pref, lights_pref, heater_pref,
                 lights_interraction, heaters_interraction):
        # pref is simulated using beta function
        self.pollution = pollution_pref
        self.nuclear = nuclear_pref
        self.lights_pref = lights_pref
        self.heater_pref = heater_pref
        self.lights_interraction = lights_interraction
        self.heaters_interraction = heaters_interraction
        self.number = lights_interraction.shape[0]

    def __str__(self):
        pass

    def to_json(self):
        pass