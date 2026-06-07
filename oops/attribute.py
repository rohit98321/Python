#common in all objects
class student:
    college_name="ricis"
    def __init__(self,name,age):
        self.name=name
        self.age=age
      
s1=student("rohit",23)
s2=student("nidhi",22) 
print(s1.college_name) 
print(s2.college_name)      
        