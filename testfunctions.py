import unittest
import os
from functions import *
import configparser
from tkinter import filedialog  # Assuming tkinter is used for filedialog; adjust if different.
from unittest.mock import patch


# ... (functions getDefaultPath and saveDefaultPath from your previous response) ...


class TestConfigFunctions(unittest.TestCase):

    def setUp(self):
        # Create a dummy config.ini file for testing.  Clean up afterwards.
        self.config_file = "config.ini"
        if os.path.exists(self.config_file):
            os.remove(self.config_file)  # Remove any existing config file

    def tearDown(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def test_getDefaultPath_file_exists_with_path(self):
        # Create a config.ini with a path
        config = configparser.ConfigParser()
        config["DEFAULT"] = {"path": "property.txt"}
        with open(self.config_file, "w") as f:
            config.write(f)

        path = getDefaultPath()
        self.assertEqual(path, "property.txt")

    def test_getDefaultPath_file_exists_without_path(self):
        # Create an empty config.ini file
        open(self.config_file, "w").close()

        path = getDefaultPath()
        self.assertEqual(path, "property.txt")
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.assertEqual(config["DEFAULT"]["path"], "property.txt")

    def test_getDefaultPath_file_does_not_exist(self):
        # Ensure file doesn't exist before test
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

        path = getDefaultPath()
        self.assertEqual(path, None)

    @patch('tkinter.filedialog.asksaveasfilename', return_value='test_path2.txt')
    def test_saveDefaultPath_valid_path(self, mock_asksaveasfilename):
        saveDefaultPath(None)  # Passing None as root since it's not crucial for this test.
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.assertEqual(config["DEFAULT"]["path"], "test_path2.txt")


if __name__ == '__main__':
    unittest.main()
