try:
    num1,num2=eval(input("enter two numbers seperated by comma :"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is error")
except SyntaxError:
    print("comma is missing.Enter a numbers seperated by comma like this 1,2")
except:
    print("wrong input")
finally:
    ("this will esecute no matter what")