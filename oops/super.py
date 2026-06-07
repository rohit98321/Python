class Car:
    def __init__(self,tpye):
        self.type=tpye

class Vehicle(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name 
        
v1=Vehicle("audi","sedan")   
print(v1.type)            