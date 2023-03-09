class Player():
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money

    def showMoney(self):
        print(self.money)

    def fold(self):
        print("fold")
        self.money = 0

joueur01 = Player("henry", 1000)
joueur02 = Player("jack", 5000)




while joueur01.money > 0:
    joueur01.showMoney()
    print(f"{joueur01.name} joue")
    joueur01.fold()
    joueur01.showMoney()
    
