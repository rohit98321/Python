students={
    "name":"rohit",
    "age":22,
    "course":"python",
    "marks":{
        "python":90,
        "java":80
    }

}

# print(students["marks"]["java"])

# print(list(students.values()))
# print(students.keys())
# print(students.values())
# print(students.items())

# pop

a=students["name"] # this will throw error if key is not present
b=students.get("name") # this will return None if key is not present
print(f"a --> {a} and b --> {b}")
# print(students["name"])
# print(students.get("name"))