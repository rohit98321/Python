class student:
    __college="ricis"#private variable
    def __greet(self):#private method
        print(f"welcome to {self.__college}")
    
    def welcome(self):
        self.__greet()    

s1=student()
s1.welcome()       