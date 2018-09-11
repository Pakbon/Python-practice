"""Define class wallet, initiate with values
print values given, do simple maths on values"""

class wallet:
    def __init__(self,money,cards,receipts,name):
        self.money,self.cards,self.receipts,self.name=money,cards,receipts,name

    def hoeveel(self):
        print(f'There are  {self.money+self.cards+self.receipts} items in {self.name}')

    def vakjes(self,cards_vakjes):
        print(f'There are {cards_vakjes} sleeves in {self.name}',end='')
        print(f', of which {cards_vakjes-self.cards} unused')

potmoni=wallet(3,3,2,'potmoni') #2 objects of class wallet
portomonnee=wallet(10,8,5,'portomonnee')
cardholder=wallet(0,4,0,'cardholder')

obj_wallet=[potmoni,portomonnee,cardholder]
sleeves=[13,15,7]

for i,n in zip(obj_wallet,sleeves):
    i.hoeveel()
    i.vakjes(n)
