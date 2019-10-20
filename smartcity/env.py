import os
import random

import numpy as np
import gym

from .factory import load_from_json


path = os.path.dirname(os.path.realpath(__file__))


class SmartCityEnv(gym.Env):
    def __init__(self, json_file_path):
        self.engine = None
        self.fp = json_file_path

    def __initialize_env(self, json_file_path):
        self.engine = load_from_json(json_file_path)

    def change_settings(self, setting_file_path):
        self.__initialize_env(setting_file_path)

    def step(self, actions):
        energies, heaters, lights = [np.array(actions[k]) for k in ["energies", "heaters", "lights"]]
        energies[energies < 0] = 0
        heaters[heaters < 0] = 0
        self.engine.buy_energies(energies)
        self.engine.light_up(lights)
        self.engine.heat_up(heaters)

        scores, observation, info = self.engine.step()
        return observation, scores, False, info

    def seed(self, seed):
        np.random.seed(seed)
        random.seed(seed)

    def reset(self):
        self.__initialize_env(self.fp)
        return self.engine.get_obs(), self.engine.get_info()

    def render(self):
        raise NotImplementedError


class SmartCityEnvSmall(SmartCityEnv):
    def __init__(self):
        super(SmartCityEnvSmall, self).__init__(json_file_path=f"{path}/data/small.json")


class SmartCityEnvMedium(SmartCityEnv):
    def __init__(self):
        super(SmartCityEnvMedium, self).__init__(json_file_path=f"{path}/data/medium.json")


class SmartCityEnvBig(SmartCityEnv):
    def __init__(self):
        super(SmartCityEnvBig, self).__init__(json_file_path=f"{path}/data/big.json")
