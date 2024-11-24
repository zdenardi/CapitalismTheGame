class Property:
    name: str
    price: int
    is_mortgaged: bool

    def __init__(self,name:str,price:int):
        self.name = name
        self.price = price
        self.is_mortgaged = False
        # How do you deal with rent/rent with monoply?/Rent with houses/hotels
  
    def change_owner(self,owner_id):
        self.owner_id = owner_id

    def mortgage(self):
        self.is_mortgaged = True
    