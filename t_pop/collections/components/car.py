"""
This file defines the Car class which is responsible for representing a car in the simulation.
"""
import random
import string
from typing import Optional, List, Tuple

import numpy as np


class Car:
    """
    This class is responsible for representing a car in the simulation.

    Attributes:
        car_id (str): the unique identifier of the car
        coerced (bool): whether the car is coerced or not
        parent (Optional[Car]): the parent car
        true_x (int): the real x coordinate of the car
        true_y (int): the real y coordinate of the car
        fake_x (Optional[int]): the fake x coordinate of the car
        fake_y (Optional[int]): the fake y coordinate of the car
        velocity (int): the velocity of the car
        range_of_sight (float): the range of sight of the car
        position_history (List[Tuple[int, int]]): the history of the car's position
        honest (bool): whether the car is honest or not
        true_position_index (Optional[int]): the index of the car's true position in the position cache
        fake_position_index (Optional[int]): the index of the car's fake position in the position cache
    """
    def __init__(self, x: int, y: int, coerced: bool, parent: Optional["Car"] = None) -> None:
        """
        The constructor for the Car class.

        :param x: the real x coordinate of the car
        :param y: the real y coordinate of the car
        :param coerced: whether the car is coerced or not
        :param position_index: the index of the car's position in the position cache
        :param parent: the parent car
        """
        self.car_id: str = self._generate_hex_string(length=5)
        self.coerced: bool = coerced
        self.parent: Optional["BaseCar"] = parent
        self.true_x: int = x
        self.true_y: int = y
        self.fake_x: Optional[int] = None
        self.fake_y: Optional[int] = None
        self.velocity: int = self._generate_velocity()
        self.range_of_sight: float = 0.1
        self.position_history: List[Tuple[int, int]]  = []
        self.honest: bool = True
        self.true_position_index: Optional[int] = None
        self.fake_position_index: Optional[int] = None

    @staticmethod
    def _generate_velocity() -> np.array:
        """
        Generates a random velocity for the car.

        :return: the velocity of the car
        """
        return ((np.random.rand(2)*2)-1)

    @staticmethod
    def _generate_hex_string(length: int) -> str:
        """
        Generates a random hex string of a given length.

        :param length: the length of the hex string
        :return: the hex string
        """
        hex_characters = string.hexdigits[:-6]
        return ''.join(random.choice(hex_characters) for _ in range(length))

    def set_as_fake(self, fake_x: int, fake_y: int) -> None:
        """
        Sets the car as a fake car.

        :param fake_x: the fake x coordinate of the car
        :param fake_y: the fake y coordinate of the car
        :return: None
        """
        self.fake_x = fake_x
        self.fake_y = fake_y
        self.honest = False

    @property
    def x(self) -> int:
        if self.honest is False:
            return self.fake_x
        return self.true_x

    @property
    def y(self) -> int:
        if self.honest is False:
            return self.fake_y
        return self.true_y
