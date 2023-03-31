class Car:
    #Base_price = 100000
    TYPES = ("EX1.5VTVT", "S1.5VTVT","SX1.5VTVT","SX1.5VTVTIVT")
    def __init__(self, name, type:str , price:int) -> None:
        self.name = name
        self.type = type
        self.price = price

    def __str__(self) -> str:
        return f"car name is {self.name} and model {self.type} price is {self.price}"


    @classmethod
    def carmodel(cls, name, model, cost):
        if model == "small" :
            return Car(name,Car.TYPES[0], cost)
        elif model == "medium" :
            return Car(name,Car.TYPES[1], cost * 1.5 )
        elif model == "large" :
            return Car(name, Car.TYPES[2], cost * 2)
        elif model == "extralarge" :
            return Car(name, Car.TYPES[3], cost * 2.5 )
        else:
            pass



verna = Car.carmodel("verna" ,"large",20000)

print(verna)

# verna = Car("verna", "gallery")
# print(verna)
