"""Any entity is defined here.

This module defines citizens, city, ... objects.
"""

class Energies:
    
    def __init__(self, initial_costs, initial_amounts, pollution_factors, 
                       sampler_cost_factors, sampler_amount_factors):
        self.costs = initial_costs
        self.amounts = initial_amounts
        self.pollution_factors = pollution_factors

        self.sampler_cost_factors = sampler_cost_factors
        self.sampler_amount_factors = sampler_amount_factors
    