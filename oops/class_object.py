class car:
    
    color = "red"
    def __init__(self,name):
        self.name=name
        print("this is constructor")


c1=car("ford")
print(c1.name)    