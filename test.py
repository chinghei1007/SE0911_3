from gameboard import Gameboard

o = Gameboard()
o.setup_board()
o.printPropertyNamewithOwned(['a','b'])
a = o.getProptertyList()
print(a[15]['name'])