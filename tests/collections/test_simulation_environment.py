from unittest import TestCase, main
from unittest.mock import patch
import numpy as np

from t_pop.collections.simulation_environment import SimulationEnvironment


class TestSimulationEnvironment(TestCase):

    def setUp(self) -> None:
        self.test = SimulationEnvironment([0,0.25], [0,0.25], 0.05)

    def tearDown(self) -> None:
        pass

    def test___init__(self) -> None:
        print(self.test)
        print(self.test)


if __name__ == '__main__':
    main()
