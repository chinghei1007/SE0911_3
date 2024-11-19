import unittest
from unittest.mock import patch
import character as chrtr

class Test(unittest.TestCase):
    def testPositionChange(self):
        o = chrtr.Character("May")
        o.position_change(8,8)
        position = o.getPosition()
        self.assertEqual(position,17)

    def testCharacterInitialization(self):
        char = chrtr.Character("testChar")
        name = char.getName()
        coins = char.coins
        ownedProperties = char.property
        ownedPropertiesfunc = char.getOwnedProperties()
        injail = char.getStatus() #False, 0
        retire = char.isRetired() #False

        self.assertEqual(name, "testChar")
        self.assertEqual(coins,1500)
        self.assertEqual(ownedProperties,[])
        self.assertEqual(ownedPropertiesfunc,[])
        self.assertEqual(injail, (False,0))
        self.assertEqual(retire, False)

    def test_gotojail_releasefromjail(self):
        char = chrtr.Character("a")
        self.assertEqual((False,0),char.getStatus())
        char.go_to_jail()
        position = char.position
        inJailStatus = char.in_jail
        self.assertEqual(6,position)
        self.assertEqual(True, inJailStatus)
        char.releaseFromJail(8)
        self.assertEqual(False,char.in_jail)
        self.assertEqual(14,char.position)
if __name__ == '__main__':
    unittest.main()