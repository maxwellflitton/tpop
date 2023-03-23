from t_pop.collections.adapters.location_cache import LocationCacheAdapter
from t_pop.collections.components.car import Car


class TwoDLocationGuardAdapter:

    def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int) -> None:
        self.x_min: int = x_min
        self.x_max: int = x_max
        self.y_min: int = y_min
        self.y_max: int = y_max
        self.location_cache: LocationCacheAdapter = LocationCacheAdapter()

    def check_bounds(self, car: Car) -> bool:
        if car.true_x < self.x_min or car.true_x > self.x_max:
            return False
        if car.true_y < self.y_min or car.true_y > self.y_max:
            return False
        if car.fake_x is not None:
            if car.fake_x < self.x_min or car.fake_x > self.x_max:
                return False
        if car.fake_y is not None:
            if car.fake_y < self.y_min or car.fake_y > self.y_max:
                return False
        return True

    def add_car(self, car: Car) -> Car:
        if self.check_bounds(car=car) is True:
            return self.location_cache.add_car(car=car)
        raise ValueError("car is out of bounds")

    def move_car(self, car: Car, time: float) -> Car:
        car.move_position(time=time, x_min=self.x_min, x_max=self.x_max, y_min=self.y_min, y_max=self.y_max)
        if car.fake_position_index is not None:
            car.move_fake_position(time=time, x_min=self.x_min, x_max=self.x_max, y_min=self.y_min, y_max=self.y_max)
        self.location_cache.move_car(car=car)

