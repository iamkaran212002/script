#Try Block exception
'''
try:
    a=10/0
except Exception as e:
    print(e)

#Try exception else

try:
    a=10/2
except Exception as e:
    print(e)
else:
    print("A value:",a)

#Try exception else finally

try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("A value:",a)
finally:
    print("Your code will run")
#Types of exception
for a in list(dir(locals()['__builtins__'])):
    print(a)

#Nameerror Exception
try:
    print(a)
except NameError as e:
    print("A is not definied")

#ZeroDivisionerror exception
try:
    a=10/0
except ZeroDivisionError as e:
    print(e)

#ValueError Exception
try:
    a=int("Joes")
except ValueError as e:
    print("pls enter number only")

#IndexError Exception
try:
    a=[10,20,30,40,50]
    print(a[10])
except IndexError as e:
    print(e)

#FileNotFoundError Exception
try:
    a=open("test.txt")
except FileNotFoundError as e:
    print("file not Found")
else:
    print(a.read())

#Handling Multiple Exception
try:
    a=10/0
    print(a)
    b=[10,20,30]
    print(b[4])
except ZeroDivisionError:
    print("Denomoniator cannot be zero")
except IndexError as e  :
    print("Invalid Index")
'''
