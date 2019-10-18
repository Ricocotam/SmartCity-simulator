""" Controller for the `Simulator` class.
"""


class Engine:
    def __init__(self, smart_city):
        self.smart_city = smart_city
        self.scores = []

    def __str__(self):
        pass

    def light_up(self, lights):
        self.smart_city.light_up(lights)

    def heat_up(self, heaters):
        self.smart_city.heat_up(heaters)

    def buy_energies(self, amounts):
        self.smart_city.buy_energies(amounts)

    def get_obs(self):
        return {
            "lights": self.smart_city.lights,
            "heaters": self.smart_city.heaters,
            "energies_cost": self.smart_city.energies.costs,
            "energies_amount": self.smart_city.energies.amounts,
            "needed_energy": self.smart_city.needded_energy
        }

    def get_info(self):
        return {
            "light_interraction": self.smart_city.people.lights_interraction,
            "heaters_interraction": self.smart_city.people.heaters_interraction
        }

    def step(self):
        step_scores = self.smart_city.step()
        return step_scores, self.get_obs(), self.get_info()
