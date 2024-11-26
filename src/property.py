class Property:
    _owner_id: int
    _name: str
    _price: int
    _is_mortgaged: bool

    def __init__(self,name:str,price:int):
        self._name = name
        self._price = price
        self._is_mortgaged = False
        # How do you deal with rent/rent with monoply?/Rent with houses/hotels
  
    def change_owner(self,owner_id):
        self._owner_id = owner_id

    def mortgage(self):
        self._is_mortgaged = True
    