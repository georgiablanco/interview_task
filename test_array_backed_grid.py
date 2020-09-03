"""
testing array_backed_grid.py and grid_colour_changer.py
"""

import unittest, pygame
from array_backed_grid import Grid
from grid_colour_changer import ColourChangerGame


class TestArrayBackedGrid(unittest.TestCase):
    def setUp(self):
        self.array_create = Grid()

    # checking Index Error is given when attempting to accessing out of range
    def test_check_grid_number(self):
        with self.assertRaises(IndexError):
            result = self.array_create.check_cell(16, 22)

    # checking Grid class updates correctly
    def test_check_updates(self):
        self.array_create.update_cell(2, 9)
        result = self.array_create.check_cell(2, 9)
        self.assertEqual(result, 1)

    # checking no negative numbers can be given to ColourChangerGame()
    def test_function_inputs(self):
        with self.assertRaises(Exception):
            color_changer = ColourChangerGame(1, -12, 1, [22, -22])

    # don't need this now as function above ensures no negative numbers to screen
    # def test_window_size(self):
    #     with self.assertRaises(pygame.error):
    #         color_changer = ColourChangerGame(-1, -1, -1, [-22, -22])

    # checking inputs have been given for ColourChangerGame()
    def test_inputs_given(self):
        with self.assertRaises(TypeError):
            color_changer = ColourChangerGame()


if __name__ == '__main__':
    unittest.main()