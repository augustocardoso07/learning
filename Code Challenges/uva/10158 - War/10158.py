class War():
    def __init__(self, n):
        self.list = list(range(n))
    
    def findLider(p):
        pass

    def setFriends(self, x, y):
        liderx = self.findLider(x)
        lidery = self.findLider(y)
        pass

    def setEnemies(self, x, y):
        pass
    
    def areFriends(self, x, y):
        liderx = self.findLider(x)
        lidery = self.findLider(y)
        
        if liderx == lidery:
            print(1)
        

    def areEnemies(self, x, y):
        liderx = self.findLider(x)
        lidery = self.findLider(y)
        
        

n = int(input())
war = War(n)
while True:
    c, x, y = [int(x) for x in input().split()]
    if c == x == y == 0: break
    if c == 1: war.setFriends(x, y)
    if c == 2: war.setEnemies(x, y)
    if c == 3: war.areFriends(x, y)
    if x == 4: war.areEnemies(x, y)
    
