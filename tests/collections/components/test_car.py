from unittest import TestCase, main
from unittest.mock import patch
import numpy as np

from t_pop.collections.components.car import Car


class TestCar(TestCase):

    @patch("t_pop.collections.components.car.Car._generate_velocity")
    @patch("t_pop.collections.components.car.Car._generate_hex_string")
    def setUp(self, mock__generate_hex_string, mock__generate_velocity) -> None:
        self.test = Car(x=3, y=2, coerced=False)
        self.mock__generate_hex_string = mock__generate_hex_string
        self.mock__generate_velocity = mock__generate_velocity

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        self.assertEqual(self.test.car_id, self.mock__generate_hex_string.return_value)
        self.assertEqual(self.test.coerced, False)
        self.assertEqual(self.test.parent, None)
        self.assertEqual(self.test.true_x, 3)
        self.assertEqual(self.test.true_y, 2)
        self.assertEqual(self.test.fake_x, None)
        self.assertEqual(self.test.fake_y, None)
        self.assertEqual(self.test.velocity, self.mock__generate_velocity.return_value)
        self.assertEqual(self.test.range_of_sight, 0.1)
        self.assertEqual(self.test.position_history, [])
        self.assertEqual(self.test.honest, True)

        self.assertEqual(3, self.test.x)
        self.assertEqual(2, self.test.y)

    @patch("t_pop.collections.components.car.np.random.rand")
    def test__generate_velocity(self, mock_rand) -> None:
        mock_rand.return_value = np.array([0.33218903, 0.50438249])
        self.assertEqual(np.array([-0.33562194, 0.00876498]).all(), self.test._generate_velocity().all())

    def test_set_as_fake(self) -> None:
        self.test.set_as_fake(fake_x=10, fake_y=5)
        self.assertEqual(self.test.fake_x, 10)
        self.assertEqual(self.test.fake_y, 5)
        self.assertEqual(self.test.honest, False)
        self.assertEqual(10, self.test.x)
        self.assertEqual(5, self.test.y)


if __name__ == '__main__':
    main()
