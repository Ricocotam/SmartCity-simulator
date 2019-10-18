name = "smartcity"
__name__ = name
__package__ = '.'.join('.'.join(__name__.split('/')).split('.')[:-1])

__author__ = "Adrien Pouyet (Ricocotam)"

from gym.envs.registration import register

register(
    id='SmartCity-v0',
    entry_point='smartcity.env:SmartCityEnvSmall',
)

register(
    id='SmartCity-v1',
    entry_point='smartcity.env:SmartCityEnvMedium',
)

register(
    id='SmartCity-v2',
    entry_point='smartcity.env:SmartCityEnvBig',
)