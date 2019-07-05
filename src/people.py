class People:
    def __init__(self, pollution_pref, nuclear_pref, lights_pref, heater_pref,
                 lights_interraction, heaters_interration):
        self.pollution = pollution_pref
        self.nulcear = nuclear_pref
        self.lights_pref = lights_pref
        self.heater_pref = heater_pref
        self.lights_interraction = lights_interraction
        self.heaters_interration = heaters_interration

    def __str__(self):
        pass

    def to_json(self):
        pass
