'''oranges and baskets
More OOP practice'''
import datetime, random

class Oranges:
    all_oranges=[]
    'Nothing rhymes with orange'
    def __init__(self):
        self.id=random.randrange(5000000,9999999)
        self.day_picked=datetime.datetime.now()
        self.bask=''
        Oranges.all_oranges.append(self.id)

    def baskid(self,basketid):
        self.bask=basketid
        
        
    
    def identify(self):
        print(f'orangeid={self.id}\ntime picked={self.day_picked}\nbasket={self.bask}')

class Baskets:
    'Basket to store oranges'
    def __init__(self):
        self.id=random.randrange(1000000,4999999)
        self.orange_id=[]
        self.day_created=datetime.datetime.now()

    def add_orange(self,theorange):
        self.orange_id.append(theorange)
        return self.id

    def identify(self):
        print(f'id={self.id}\nday created={self.day_created}\norange amount={len(self.orange_id)}\noranges in basket={self.orange_id}')

#initialize an orange and basket
o=Oranges()
b=Baskets()

o.baskid(b.add_orange(o.id))
b.identify()
print('\n')
o.identify()
