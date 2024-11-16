import unittest
from unittest.mock import patch
import character as chrtr

class Test(unittest.TestCase):
    def testPositionChange(self):
        o = chrtr.Character("May")
        o.position_change(8,8)
        position = o.getPosition()
        self.assertEqual(position,17)

