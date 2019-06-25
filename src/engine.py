"""

"""

class Engine:
    def __init__(self, simulator):
        self.simulator = simulator
        self.scores = []

    def light_up(self, lights_on):
        self.simulator.lights_on()
    
    def heat_up(self, heats, temperatures):
        self.simulator.heat_up(heats, temperatures)
    
    def buy_energies(self, amounts):
        self.simulator.buy(amounts)

    def step(self):
        step_scores = self.simulator.step()
        self.scores.append(step_scores)

    def __str__(self):
        pass