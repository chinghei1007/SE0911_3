import unittest
from instructions import *
from unittest.mock import patch, MagicMock, mock_open
import string
import io


#1

class TestInstructions(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', 'y'])
    def test_get_number_of_players(self, mock_input):
        result = get_number_of_players()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=[ 'Tom', 'Mike', 'Xavier', 'c'])
    def test_get_player_names(self, mock_input):
        with patch('builtins.print') as mock_print:
            player_names = get_player_names(3)
            self.assertEqual(player_names, ['Tom', 'Mike', 'Xavier'])

    '''@patch('builtins.input', side_effect=['1', 'Mike', 'y'])              #not working
    def test_change_player_names(self, mock_input):

        player_names = ['Tom', 'Jerry']


        updated_names = change_player_names(player_names)


        self.assertEqual(updated_names[0], 'Mike')
        self.assertEqual(updated_names[1], 'Jerry' '''

    @patch('builtins.input', side_effect=['1','aa','0','y'])
    def test_change_player_names(self,mockinput):
        player_names = ['a', 'b']
        updated_names = change_player_names(player_names)

        self.assertEqual(updated_names,['aa','b'])




    @patch('builtins.input')
    def test_print_player_names(self, mock_input):
        player_names = ['Tom', 'Jerry']
        with patch('builtins.print') as mock_print:
            print_player_names(player_names)
            mock_print.assert_any_call("Player 1 : Tom")
            mock_print.assert_any_call("Player 2 : Jerry")




    @patch('builtins.open', new_callable=MagicMock)
    def test_read_to_list(self, mock_open):
        mock_open.return_value.__enter__.return_value.readlines.return_value = [

            "Central, 800, 90\n",
            "Wan Chai, 700, 65\n"
        ]
        result = read_to_list('mock_path.txt')
        expected = [
            {"name": "Central", "price": 800, "rent": 90},
            {"name": "Wan Chai", "price": 700, "rent": 65}
        ]
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=['5'])
    def test_input_number_within_range(self, mock_input):
        result = input_number_within_range(2, 6)
        self.assertEqual(result, 5)



    @patch('builtins.input', side_effect=['y'])
    def test_double_confirm(self, mock_input):
        result = double_confirm()
        self.assertEqual(result, 'y')

    # second set of test
    def test_read_to_list2(self):
        with patch('builtins.open', mock_open(read_data='name1, 10, 5\nname2, 20, 10\nname3, 30, 15')):
            result = read_to_list('test_file.txt')
            self.assertEqual(result, [
                {'name': 'name1', 'price': 10, 'rent': 5},
                {'name': 'name2', 'price': 20, 'rent': 10},
                {'name': 'name3', 'price': 30, 'rent': 15}
            ])

        # Test file not found
        with patch('builtins.print') as mock_print:
            read_to_list('non_existent_file.txt')
            mock_print.assert_called_with("Error: File not found")

        # Test other exceptions
        with patch('builtins.open', mock_open(read_data='name1, 10, a')), \
                patch('builtins.print') as mock_print:
            read_to_list('test_file.txt')
            mock_print.assert_called()

    def test_input_number_within_range2(self):
        with patch('builtins.input', side_effect=['11', '0', 'abc', '5']), \
                patch('builtins.print') as mock_print:
            result = input_number_within_range(1, 10)
            self.assertEqual(result, 5)
            self.assertEqual(mock_print.call_count, 3)
            mock_print.assert_any_call("Error: the number must be between 1 and 10. Please try again")
            mock_print.assert_any_call("Please enter a valid number. ")

    def test_double_confirm2(self):
        # Test valid input 'y'
        with patch('builtins.input', return_value='y'):
            result = double_confirm()
            self.assertEqual(result, 'y')

        # Test valid input 'n'
        with patch('builtins.input', return_value='n'):
            result = double_confirm()
            self.assertEqual(result, 'n')

        # Test invalid input
        with patch('builtins.input', side_effect=['invalid', 'y']), \
                patch('builtins.print') as mock_print:
            result = double_confirm()
            self.assertEqual(result, 'y')
            mock_print.assert_called_with("Please type only y or n")

    def test_double_confirm_true_false(self):
        # Test valid input 'y'
        with patch('builtins.input', return_value='y'):
            result = double_confirm_true_false()
            self.assertTrue(result)

        # Test valid input 'n'
        with patch('builtins.input', return_value='n'):
            result = double_confirm_true_false()
            self.assertFalse(result)

        # Test invalid input
        with patch('builtins.input', side_effect=['invalid', 'y']), \
                patch('builtins.print') as mock_print:
            result = double_confirm_true_false()
            self.assertTrue(result)
            mock_print.assert_called_with("Please type only y or n")

    def test_generate_random_string(self):
        # Test random string generation
        for _ in range(10):
            result = generate_random_string(10)
            self.assertEqual(len(result), 10)
            self.assertTrue(all(c in string.ascii_letters + string.digits for c in result))


if __name__ == '__main__':
    unittest.main()