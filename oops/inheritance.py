#single inheritance
class Car:
    
    var1="this is car class"
    
    @staticmethod
    def start():
        print("car is starting")
    
    @staticmethod
    def stop():
        print("car is stopping")

class Vehicle(Car):#single inheritance
    var2="this is vehicle class"
    
    def __init__(self,name):
        self.name=name            


class NewCar(Vehicle):#multilevel inheritance
    var3="this is newcar class"
    def __init__(self,model):
        self.model=model





v1=NewCar("vdi") 
v1.start()
v1.name="audi"
print(v1.name)
print(v1.model) 




   