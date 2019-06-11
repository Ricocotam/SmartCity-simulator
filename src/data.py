"""Any entity is defined here.

This module defines citizens, city, ... objects.
"""
from dataclasses import dataclass
from typing import List, NewType


Stat = NewType("Stat", (float, float))  # mean, std
Range = NewType("Range", (float, float))  # minimum, maximum
Position = NewType("Position", (float, float))  # x, y

@dataclass
class Building:
    position : Position


@dataclass
class Transport:
    stations : List[Position]


@dataclass
class Lights:
    position : Position


@dataclass
class Neighbourhood:
    buildings : List[Building]
    pass


@dataclass
class District:
    hoods : List[Neighbourhood]


@dataclass
class Citizen:
    temperature : Stat
    light_distance : float
    nuclear : Stat
    pollution : Stat


@dataclass
class City:
    districts : List[District]
    citizens : List[Citizen]
    transpors : List[Transport]
    

@dataclass
class Energy:
    name: str
    pollution: float
    cost: float
    available: int