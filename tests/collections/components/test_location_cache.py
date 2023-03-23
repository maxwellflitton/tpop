from unittest import TestCase, main

from t_pop.collections.components.car import Car
from t_pop.collections.components.location_cache import LocationCache, LocationCacheType


class TestLocationCache(TestCase):

    def setUp(self) -> None:
        self.test = LocationCache(cache_type=LocationCacheType.TRUE)
        self.car_one = Car(x=3, y=2, coerced=False)
        self.car_one.fake_y = 5
        self.car_one.fake_x = 10

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        self.assertEqual(self.test, [])
        self.assertEqual(self.test.cache_size, 0)

    def test_add_car_true(self) -> None:
        self.test.add_car(self.car_one)
        self.assertEqual(self.test, [(3, 2)])
        self.assertEqual(self.test.cache_size, 1)
        self.assertEqual(self.car_one.true_position_index, 0)

        with self.assertRaises(ValueError) as error:
            self.test.add_car(self.car_one)
        self.assertEqual("Car already in cache", str(error.exception))

    def test_add_car_fake(self) -> None:
        self.test.cache_type = LocationCacheType.FAKE
        self.test.add_car(self.car_one)
        self.assertEqual(self.test, [(10, 5)])
        self.assertEqual(self.test.cache_size, 1)
        self.assertEqual(self.car_one.fake_position_index, 0)

        with self.assertRaises(ValueError) as error:
            self.test.add_car(self.car_one)
        self.assertEqual("Car already in cache", str(error.exception))

    def test_update_car_position(self) -> None:
        self.test.append((3, 20))
        self.test.append((10, 5))
        self.test.append((6, 7))
        self.car_one.true_position_index = 1

        self.test.update_car_position(self.car_one)

        self.assertEqual(self.test, [(3, 20), (3, 2), (6, 7)])

    def test_get_cars_in_range(self) -> None:
        self.test.append((3, 20))
        self.test.append((10, 5))
        self.test.append((11, 6))
        self.test.append((9, 4))
        self.test.append((6, 7))

        self.car_one.position_index = 1
        self.car_one.range_of_sight = 2
        self.car_one.true_x = 10
        self.car_one.true_y = 5

        result = self.test.get_cars_in_range(self.car_one)
        self.assertEqual([1, 2, 3], result)


if __name__ == '__main__':
    main()
