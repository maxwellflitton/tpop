"""
This file defines the LocationCache class which is responsible for keeping track of the locations of all cars in the
simulation.
"""
from typing import List
from enum import Enum

from scipy.spatial import KDTree

from t_pop.collections.components.car import Car


class LocationCacheType(Enum):
    """
    This enum is responsible for defining the different types of location caches.
    """
    FAKE = "fake_position_index"
    TRUE = "true_position_index"


class LocationCache(list):
    """
    This class is responsible for keeping track of the locations of all cars in the simulation.

    Attributes:
        cache_size (int): the size of the cache which is the total number of cars in the simulation.
        cache_type (LocationCacheType): the type of the cache which is either fake or true
    """
    def __init__(self, cache_type: LocationCacheType) -> None:
        """
        The constructor for the LocationCache class.
        """
        super().__init__([])
        self.cache_size: int = 0
        self.cache_type: LocationCacheType = cache_type

    def add_car(self, car: Car) -> Car:
        """
        Adds a car location to the cache.

        :param car: the car owning the location to be added to the cache
        :return: the updated car with the position index set
        """
        if getattr(car, self.cache_type.value) is not None:
            raise ValueError("Car already in cache")

        if self.cache_type == LocationCacheType.FAKE:
            self.append((car.fake_x, car.fake_y))
        else:
            self.append((car.true_x, car.true_y))

        setattr(car, self.cache_type.value, self.cache_size)
        self.cache_size += 1
        return car

    def update_car_position(self, car: Car) -> None:
        """
        Updates the location of a car in the cache.

        :param car: the car whose location is to be updated
        :return: None
        """
        if self.cache_type == LocationCacheType.FAKE:
            self[getattr(car, self.cache_type.value)] = (car.fake_x, car.fake_y)
        else:
            self[getattr(car, self.cache_type.value)] = (car.true_x, car.true_y)

    def get_cars_in_range(self, car: Car) -> List[int]:
        """
        Returns a list of the indices of the cars in range_of_sight of the given car.

        :param car: the car whose range of sight is to be checked
        :return: a list of the indices of the cars in range_of_sight of the given car
        """
        kdtree = KDTree(self)
        if self.cache_type == LocationCacheType.FAKE:
            return kdtree.query_ball_point((car.fake_x, car.fake_y), car.range_of_sight)
        else:
            return kdtree.query_ball_point((car.true_x, car.true_y), car.range_of_sight)

    def get_inverse_cars_in_range(self, car: Car) -> List[int]:
        """
        Returns a list of the indices of the cars in range_of_sight of the given car in the opposite cache.

        :param car: the car whose range of sight is to be checked
        :return: a list of the indices of the cars in range_of_sight of the given car from the opposite cache
        """
        kdtree = KDTree(self)
        if self.cache_type == LocationCacheType.FAKE:
            return kdtree.query_ball_point((car.true_x, car.true_y), car.range_of_sight)
        else:
            return kdtree.query_ball_point((car.fake_x, car.fake_y), car.range_of_sight)
