"""" accept gender and print goodmorning sir or maam """

gender =str(input("Enter your gender(M/F): "))

if gender == "M" or gender == "m":
    print("hello sir good morning")
elif gender == "F" or gender == "f":
    print("hello maam good morning")    
else: 
    print("invalid input")   