import unittest
from instructions import *
from unittest.mock import patch, MagicMock




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

    @patch('builtins.input', side_effect=['1', 'Mike', 'y'])              #not working
    def test_change_player_names(self, mock_input):

        player_names = ['Tom', 'Jerry',]


        updated_names = change_player_names(player_names)


        self.assertEqual(updated_names[0], 'Mike')
        self.assertEqual(updated_names[1], 'Jerry')



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

if __name__ == '__main__':
    unittest.main()