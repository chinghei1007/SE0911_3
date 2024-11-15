import unittest
from unittest.mock import patch
from functions import importGbFunc, getDefaultPath, saveDefaultPath

class TestFunctions(unittest.TestCase):

    @patch('tkinter.Tk')
    @patch('tkinter.filedialog.askopenfilename')
    @patch('builtins.input', side_effect=['y'])  # Mock user input
    @patch('functions.saveDefaultPath')  # Mock saveDefaultPath function
    @patch('functions.getDefaultPath', return_value="default/path.txt")  # Mock getDefaultPath
    @patch('gameboard.Gameboard.importGbfromFunc')  # Mock the import function
    def test_import_gameboard_and_set_default(self, mock_import, mock_get_default, mock_save, mock_askopenfilename, mock_Tk):
        # Mock the file dialog to return a test file path
        mock_askopenfilename.return_value = "test_gameboard.txt"

        importGbFunc()

        # Assertions
        mock_askopenfilename.assert_called_once()
        mock_save.assert_called_once_with("test_gameboard.txt")
        mock_import.assert_called_once_with("test_gameboard.txt")

    @patch('tkinter.Tk')
    @patch('tkinter.filedialog.askopenfilename')
    @patch('builtins.input', side_effect=['n'])  # Mock user input for not setting default
    @patch('functions.saveDefaultPath')  # Mock saveDefaultPath function
    @patch('functions.getDefaultPath', return_value="default/path.txt")  # Mock getDefaultPath
    @patch('gameboard.Gameboard.importGbfromFunc')  # Mock the import function
    def test_import_gameboard_and_not_set_default(self, mock_import, mock_get_default, mock_save, mock_askopenfilename, mock_Tk):
        # Mock the file dialog to return a test file path
        mock_askopenfilename.return_value = "test_gameboard.txt"

        importGbFunc()

        # Assertions
        mock_askopenfilename.assert_called_once()
        mock_save.assert_not_called()  # Ensure saveDefaultPath was not called
        mock_import.assert_called_once_with("test_gameboard.txt")

    @patch('os.path.exists', return_value=True)
    @patch('configparser.ConfigParser.read')
    @patch('configparser.ConfigParser.__getitem__', return_value={"path": "default/path.txt"})
    def test_get_default_path_exists(self, mock_getitem, mock_read, mock_exists):
        path = getDefaultPath()
        self.assertEqual(path, "default/path.txt")

    @patch('os.path.exists', return_value=False)
    @patch('configparser.ConfigParser.write')
    @patch('configparser.ConfigParser.__setitem__')
    def test_get_default_path_creates_file(self, mock_setitem, mock_write, mock_exists):
        path = getDefaultPath()
        self.assertEqual(path, "./property.txt")
        mock_setitem.assert_called_once_with("DEFAULT", {"path": "./property.txt"})
        mock_write.assert_called_once()

    @patch('configparser.ConfigParser.read')
    @patch('configparser.ConfigParser.__setitem__')
    @patch('configparser.ConfigParser.write')
    def test_save_default_path(self, mock_write, mock_setitem, mock_read):
        saveDefaultPath("new/default/path.txt")
        mock_setitem.assert_called_once_with("DEFAULT", {"path": "new/default/path.txt"})
        mock_write.assert_called_once()

if __name__ == '__main__':
    unittest.main()