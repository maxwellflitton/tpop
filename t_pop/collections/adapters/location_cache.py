from typing import List, Dict

from t_pop.collections.components.car import Car
from t_pop.collections.components.location_cache import LocationCache, LocationCacheType


class LocationCacheAdapter:

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
