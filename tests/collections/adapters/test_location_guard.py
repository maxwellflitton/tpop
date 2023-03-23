from unittest import TestCase, main
from unittest.mock import patch
import numpy as np

from t_pop.collections.adapters.location_guard import TwoDLocationGuardAdapter, Car


class TestTwoDLocationGuardAdapter(TestCase):

    def setUp(self) -> None:
        self.test = TwoDLocationGuardAdapter(x_min=5, x_max=15, y_min=7, y_max=18)
        self.car_pass = Car(x=6, y=9, coerced=False)
        self.car_out_of_bounds = Car(x=4, y=19, coerced=False)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        self.assertEqual(self.test.x_min, 5)
        self.assertEqual(self.test.x_max, 15)
        self.assertEqual(self.test.y_min, 7)
        self.assertEqual(self.test.y_max, 18)

    def test_check_bounds(self):
        self.assertEqual(True, self.test.check_bounds(car=self.car_pass))
        self.assertEqual(False, self.test.check_bounds(car=self.car_out_of_bounds))


if __name__ == '__main__':
    main()
