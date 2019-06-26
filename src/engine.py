""" Controller for the `Simulator` class.
"""


class Engine:
    def __init__(self, smart_city):
        self.smart_city = smart_city
        self.scores = []

    def __str__(self):
        pass

    def light_up(self, lights_on):
        self.smart_city.lights_on()

    def heat_up(self, heats, temperatures):
        self.smart_city.heat_up(heats, temperatures)

    def buy_energies(self, amounts):
        self.smart_city.buy(amounts)

    def step(self):
        step_scores = self.smart_city.step()
        self.scores.append(step_scores)


if __name__ == '__main__':
    pass
