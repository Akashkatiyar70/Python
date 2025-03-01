class AgeError(Exception):
    pass

age = int(input("Enter age: "))
if age>=13:
    print("start the game")
else:
    raise AgeError("age must be 13+")