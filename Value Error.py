try:
    number=int(input("enter a number:"))
    print("the number enterd is",number)
except ValueError as ex:
    print("Exeption:",ex)