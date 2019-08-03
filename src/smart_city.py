""" This module contains all simulation functions for the entire city. Those
are called at each tick.
"""
from .scores import compute_scores


class NotEnoughEnergy(Exception):
    def __init__(self, bought, needed):
        msg = f"You bought {bought} energy but you need {needed}"
        super(NotEnoughEnergy, self).__init__(msg)


class SmartCity:
    def __init__(self, people, energies, lights, heaters):
        self.people = people
        self.energies = energies
        self.lights = lights
        self.heaters = heaters

        self.needded_energy = 50
        self.stored = 0

    def step(self):
        """ Compute (and returns) the score for the current step, then update
        the city's data to the next step.
        """
        if self.stored < self.needded_energy:
            raise NotEnoughEnergy(self.energies.bought_amounts.sum(), self.needded_energy)
        scores = compute_scores(people=self.people, energies=self.energies,
                                lights=self.lights, heaters=self.heaters)
        self.energies_step()
        return scores

    def energies_step(self):
        assert self.stored >= self.needded_energy
        new_cost = self.energies.new_cost(self.energies.costs, self.energies.bought_amounts)
        new_amount = self.energies.new_amount(self.energies.amounts, self.energies.bought_amounts)

        self.energies.costs = new_cost
        self.energies.amounts = new_amount

    def light_up(self, lights_on):
        pass

    def heat_up(self, heats, temperatures):
        pass

    def buy_energies(self, amounts):
        cost, quantity = self.energies.buy(amounts)
        self.stored += quantity
        return cost
