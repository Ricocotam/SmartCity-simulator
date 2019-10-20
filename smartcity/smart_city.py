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

        self.base_energy = 2 * self.people.number
        self.needded_energy = self.base_energy
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
        self.stored -= self.needded_energy

        new_cost = self.energies.new_cost(self.energies.costs, self.energies.bought_amounts)
        new_amount = self.energies.new_amount(self.energies.amounts, self.energies.bought_amounts)

        self.energies.costs = new_cost
        self.energies.amounts = new_amount

        heaters_energy = self.heaters[self.heaters <= 18].sum() * 0.2 + \
                         self.heaters[(18 < self.heaters) & (self.heaters <= 20)].sum() * 0.4 + \
                         self.heaters[(20 < self.heaters) & (self.heaters <= 22)].sum() * 1.2 + \
                         self.heaters[self.heaters > 22].sum() * 1.8
        light_energy = 0.1 * self.lights.sum()
        self.needded_energy = self.base_energy + heaters_energy + light_energy

    def light_up(self, lights):
        self.lights = lights

    def heat_up(self, heaters):
        self.heaters = heaters

    def buy_energies(self, amounts):
        cost, quantity = self.energies.buy(amounts)
        self.stored += quantity
        return cost
