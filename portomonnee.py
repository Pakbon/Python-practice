"""Trying out classes and OOP"""

class portomonnee:
    def __init__(self,geld,pasjes,bonnen):
        self.geld,self.pasjes,self.bonnen=geld,pasjes,bonnen

    def hoeveel(self):
        print(f'Er zijn {self.geld+self.pasjes+self.bonnen} items in mijn portomonnee')

potmoni=portomonnee(3,3,2)
wallet=portomonnee(10,20,5)
print(f'{potmoni} {wallet}')
potmoni.hoeveel()
wallet.hoeveel()