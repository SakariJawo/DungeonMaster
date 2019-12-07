import unittest
import main
import game_functions

class TestCases(unittest.TestCase):
    def test_make_board(self):
        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(4)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(5)
        self.assertEqual(expected_result, actual_result)

        expected_result = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result = main.make_board(8)
        self.assertEqual(expected_result, actual_result)

    def test_get_grid_size(self):

        menu_choice1 = "1"
        menu_choice2 = "2"
        menu_choice3 = "3"

        expected_result1 = 4
        expected_result2 = 5
        expected_result3 = 8

        actual_result1 = main.get_grid_size(menu_choice1)
        actual_result2 = main.get_grid_size(menu_choice2)
        actual_result3 = main.get_grid_size(menu_choice3)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)

    def test_start_position(self):

        choice1 = "1"
        choice2 = "2"
        choice3 = "3"
        choice4 = "4"
        grid_size = 4

        expected_result1 = (0,0)
        expected_result2 = (0, grid_size-1)
        expected_result3 = (grid_size-1, 0)
        expected_result4 = (grid_size-1, grid_size -1)

        actual_result1 = main.start_position(choice1, grid_size)
        actual_result2 = main.start_position(choice2, grid_size)
        actual_result3 = main.start_position(choice3, grid_size)
        actual_result4 = main.start_position(choice4, grid_size)

        self.assertEqual(expected_result1, actual_result1)
        self.assertEqual(expected_result2, actual_result2)
        self.assertEqual(expected_result3, actual_result3)
        self.assertEqual(expected_result4, actual_result4)

    def test_place_hero(self):

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        coordinates1 = (0,0)
        coordinates2 = (0,3)
        coordinates3 = (3,0)
        coordinates4 = (3,3)

        expected_result1 = [['[x]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result1 = main.place_hero(coordinates1, board)
        self.assertEqual(expected_result1, actual_result1)

        expected_result2 = [['[ ]', '[ ]', '[ ]', '[x]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]

        actual_result2 = main.place_hero(coordinates2, board)
        self.assertEqual(expected_result2, actual_result2)

        expected_result3 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[x]', '[ ]', '[ ]', '[ ]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result3 = main.place_hero(coordinates3, board)
        self.assertEqual(expected_result3, actual_result3)

        expected_result4 = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                           ['[ ]', '[ ]', '[ ]', '[x]']]

        board = [['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]'],
                 ['[ ]', '[ ]', '[ ]', '[ ]']]
        actual_result4 = main.place_hero(coordinates4, board)
        self.assertEqual(expected_result4, actual_result4)


    def test_generate_treasure(self):
        chance = 40
        treasure_type = 'Lösa slantar: 2'
        treasure_value = 2

        expected_result_1 = 2
        expected_result_2 = 0
        actual_result_1 = game_functions.generate_treasure(chance, treasure_type, treasure_value, 15)
        actual_result_2 = game_functions.generate_treasure(chance, treasure_type, treasure_value, 50)

        self.assertEqual(expected_result_1, actual_result_1)
        self.assertEqual(expected_result_2, actual_result_2)

    def test_treasure_sum(self):

        test_list = [1, 2, 3]
        expected_result = 6
        actual_result = game_functions.treasure_sum(test_list)
        self.assertEqual(expected_result, actual_result)


    def test_clean_list(self):

        test_list = [0, 0, (1,2), 0, (1,2)]
        expected_result = [(1,2), (1,2)]
        actual_result = game_functions.clean_list(test_list)
        self.assertEqual(expected_result,actual_result)


if __name__ == '__main__':

    unittest.main()