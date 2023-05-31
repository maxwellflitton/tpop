"""
This file defines the LocationCacheAdapter class for handling the fake and true location caches.
"""
from typing import List, Dict

from t_pop.collections.components.car import Car
from t_pop.collections.components.location_cache import LocationCache, LocationCacheType


class LocationCacheAdapter:
    """
    This class is responsible for handling the fake and true location caches essentially acting as an interface.

    Attributes:
        true_cache (LocationCache): A cache of cars with True locations
        fake_cache (LocationCache): A cache of cars with Fake locations
    """
    def __init__(self) -> None:
        """
        The constructor for the LocationCacheAdapter class.
        """
        self.true_cache: LocationCache = LocationCache(cache_type=LocationCacheType.TRUE)
        self.fake_cache: LocationCache = LocationCache(cache_type=LocationCacheType.FAKE)

    def add_car(self, car: Car) -> Car:
        """
        Adds a car to the caches and updates the indexes of that car.

        :param car: the car to be added to the caches
        :return: the added car with the updated indexes
        """
        car = self.true_cache.add_car(car)
        if car.fake_y is not None and car.fake_x is not None:
            car = self.fake_cache.add_car(car)
        return car

    def move_car(self, car: Car) -> None:
        """
        Moves a car X and Y coordinates in location caches.

        :param car: the car to be moved
        :return: None
        """
        self.true_cache.update_car_position(car=car)
        if car.fake_position_index is not None:
            self.fake_cache.update_car_position(car=car)

    def get_neighbours(self, car: Car) -> Dict[LocationCacheType, List[int]]:
        """
        Gets the neighbours of a car.

        :param car: the car whose neighbours are to be found
        :return: the list of indexes of the neighbours mapped to the cache type
        """
        if car.honest is True and car.coerced is False:
            return {
                LocationCacheType.TRUE: self.true_cache.get_cars_in_range(car),
                LocationCacheType.FAKE: []
            }
        elif car.honest is True and car.coerced is True:
            return {
                LocationCacheType.TRUE: self.true_cache.get_cars_in_range(car),
                LocationCacheType.FAKE: self.fake_cache.get_cars_in_range(car)
            }
        elif car.honest is False and car.coerced is False:
            return {
                LocationCacheType.TRUE: self.true_cache.get_inverse_cars_in_range(car),
                LocationCacheType.FAKE: []
            }
        elif car.honest is False and car.coerced is True:
            return {
                LocationCacheType.TRUE: self.true_cache.get_inverse_cars_in_range(car),
                LocationCacheType.FAKE: self.fake_cache.get_cars_in_range(car)
            }
