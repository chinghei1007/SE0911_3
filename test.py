import unittest
from unittest.mock import patch

import gameboard
from functions import importGbFunc, getDefaultPath, saveDefaultPath

class TestFunctions(unittest.TestCase):

    @patch('os.path.exists', return_value=True)
    #@patch('configparser.ConfigParser.read')
    #@patch('configparser.ConfigParser.__getitem__', return_value={"path": "property.txt"})
    def test_get_default_path_exists(self,  mock_exists):
        path = getDefaultPath()
        self.assertEqual(path, "property.txt")

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