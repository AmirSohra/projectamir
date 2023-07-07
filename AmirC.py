# ********* In The Nmae Of God ***********
#  Student ID: 401130433
#  Student Name: Amir Ali Sohrabi
#  Fundamental of Computers and Programming (python)
#  Hamedan University of Technology, Hamedan, Iran.


# -------------------------------------------Packs-----------------------------------------------

class Pack:                                 # Parent class
    def __init__(self, count, weight, finish, start, history):
        self.packNumber = count
        self.weight = weight
        self.destination = finish
        self.start = start
        self.history = history
        
    def get_type_pack(self) :
          return  "Pack"

class Pack_breakable(Pack):                   # Child class
    def __init__(self, count, weight, finish, start, history):
        super().__init__( count, weight, finish, start , history)
        
    def get_type_pack(self) :
          return  "Pack_breakable"

class Pack_cold(Pack):                         # Child class
    def __init__(self, count, weight, finish, start, history, temperature):
        super().__init__(count, weight, finish, start, history)
        self.temperature = temperature

    def get_type_pack(self) :
          return  "Pack_cold"

# -------------------------------------------Continers-----------------------------------------------
class Continer:
    def __init__(self, count, weight, countMax_pack):
        self.continerNumber = count
        self.weight = weight
        self.countMax_pack = countMax_pack

    def get_type_continer(self) :
          return  "Continer"

class Freezer_Container(Continer):
    def __init__(self, count, weight, countMax_pack, Car_refrigerator_temperature ):
        super().__init__(count, weight, countMax_pack)
        self.Car_refrigerator_temperature = Car_refrigerator_temperature
        self.list_packs_To_Freezer_Container = []
    
    def get_type_continer(self) :
          return  "Freezer_Container"

class breakable_Container(Continer):
    def __init__(self, count, weight, countMax_pack, speed):
        super().__init__(count, weight, countMax_pack)
        self.speed = speed
        self.list_packs_To_breakable_Container = []

    def get_type_continer(self) :
          return  "breakable_Container"

# -------------------------------------------Cars-----------------------------------------------

class Car:
    def __init__(self, count, weight):
        self.carNumber = count
        self.weight = weight

    def get_type_car(self) :
          return  "Car"

class Room_Car(Car):
    def __init__(self, count, weight, countMax_pack, ):
        super().__init__(count, weight)
        self.countMax_pack = countMax_pack
        self.list_packs_ordinary = []

    def get_type_car(self) :
          return  "Room_Car"
    
class Car_Carry_Continer(Car):
    def __init__(self, count, weight, countMax_continer):
        super().__init__(count, weight)
        self.countMax_continer = countMax_continer
        self.list_continers_To_car = []

    def get_type_car(self) :
        return  "Car_Carry_Continer"





