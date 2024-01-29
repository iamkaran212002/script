'''
class car():
    a=10
    b=20
a=10
print(a)
swift=car()
print(isinstance(swift,car))
print(isinstance(a,int))
print(swift.a)

#setattr Method
class DB():
    name="karan"
    age=21

#getattr method
print(getattr(DB,"name"))
print(getattr(DB,"age"))
print(getattr(DB,"gender","No Such attribute"))

#dot notation
print(DB.name)
print(DB.age)

#setattr Method
setattr(DB,"name","Thonas")
print(DB.name)

#adding attr using dot and setattr
setattr(DB,"Gender","Male")
print(DB.Gender)
DB.City="Madurai"
print(DB.City)

#Map class in Dict
print(DB.__dict__)

#Deleteattr
delattr(DB,"Gender")
print(DB.__dict__)
del(DB.age)
print(DB.__dict__)


#Instance attribute
class user:
    courses="Java"

c=user()
print(user.__dict__)
print(user.courses)
try:
    print(c.user)
except Exception as e:
    print(e)
print(c.__dict__)
c.courses="Python"
c.courses="C"
print(c.courses)
print(c.__dict__)
c1=user()
print(c1.courses)


#class Methods
class stud:
    name="karan"
    age=21

    def print():
        print("Name:",stud.name)
        print("Age:",stud.age)

stud.print()
print(stud.__dict__)
print(getattr(stud,"print"))
getattr(stud,"print")()
stud.__dict__['print']()

#Instance Method
class stud:
    name="karan"
    age=21

    def print(self,gender):
        print("Name:",stud.name)
        print("Age:",stud.age)
        print("Gender:",gender)
o=stud()
o.print("Male")
stud.print(o,'Male')
'''
#__init__ Method or Constructor
class stud:
    def __init__(self,name):
        print("Hello")
        self.name=name

    def print(self):
        print("Name:",self.name)

o=stud("Karan")
o.print()
print(stud.__dict__)
o1=stud("Ziva")
o1.print()
print(o.__dict__,o1.__dict__)
