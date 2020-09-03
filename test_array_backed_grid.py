import unittest
from array_backed_grid import Grid
from grid_colour_changer import ColourChangerGame


class TestArrayBackedGrid(unittest.TestCase):
    def setUp(self):
        self.array_create = Grid
        self.color_changer = ColourChangerGame

    def test_check_grid_number(self):
        result = self.array_create.check_cell(16, 22)

        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()