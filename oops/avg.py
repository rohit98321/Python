class student:
    
    college="ricis"
    
    @staticmethod #decorator in python
    def greet():
        print("welcome to ricis")
    
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def avg(self):
        print(sum(self.marks)/3)    

s1=student("rohit",23,[99,99,99]) 
s1.avg()  
s1.greet()     