import unittest
from unittest.mock import patch
import character as chrtr
#1
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
        retire = char.IsRetired() #False

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
        char.releaseFromJail(4, 4)
        self.assertEqual(False,char.in_jail)
        self.assertEqual(14,char.position)

        char1 = chrtr.Character("b")
        self.assertEqual((False, 0), char.getStatus())
        char1.go_to_jail()
        position = char1.position
        inJailStatus = char1.in_jail
        self.assertEqual(6, position)
        self.assertEqual(True, inJailStatus)
        char1.releaseFromJailPayFine(4, 4)
        self.assertEqual(False, char1.in_jail)
        self.assertEqual(14, char1.position)

    def test_coin_change(self):
        he= chrtr.Character("Tom")
        he.coin_change(500)
        self.assertEqual(he.coins,2000)

    def test_coin_change_to_neg_and_retire(self):
        he = chrtr.Character("Tom")
        he.coin_change(-2500)
        self.assertEqual(he.coins,-1000)
        self.assertEqual(he.retire,True)
        self.assertEqual(he.property, [])



if __name__ == '__main__':
    unittest.main()