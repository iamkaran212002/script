#Dictonaries
'''
user = {
    "name":"DJ",
    "age":21,
    "isMarried":True
}
print(user)
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items( ))
for x in user:
    print(x,user[x])

for x in user.keys():
    print(x)

for x in user.values():
    print(x)

for x in user.items():
    print(x)

if "gender" in user:
    print("Yes")
else:
    print("No")

#Changing values

user.update({"Gender":"Male"})
print(user)
user["age"]=25
print(user)

users = {
    "user1" : {
        "name":"DJ",
        "age":21,
        "isMarried":True
    },
    "user2" : {
            "name":"DJ",
            "age":21,
            "isMarried":True}
}
print(users.keys(),users.values()
      ,users.items())
'''
'''
#Identity opeerators
a=[1,2]
b=[3,4]
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a==b)
print( a is not b)
print( a is not c)
print( a!=b)'''
'''
#Membership Operator

a=[100,20,30,22,45]
print(22 in a)
print(22 not in a)'''

#Functions
'''
def karan():
    print("Vanakam da Mapla Madurai la Irunthu")

karan()
karan()
karan()
'''
#No-Return Type without Argument Function
'''
def add():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of b:"))
    c=a+b
    print("Total:",c)

add()
'''

#Noreturn Type with Argument Function
'''
def sub(x,y): 
    c=x-y
    print("Difference:",c)

a=10
b=20
sub(a,b)'''

#Return Type without Argument Function
'''
def mul():
    a=int(input())
    b=int(input())
    c=a*b
    return c

x=mul()
print("Mul:",x)'''

#Return Type with Argument Function
'''
def div(x,y):
    z=x/y
    return z
a=float(input("a:"))
b=float(input("b:"))
c=div(a,b)
print("Div:",int(c))'''

#Arbitrary Argument Function
'''
def class_B(*karan):
    print(karan)
    for i  in karan:
        print(i)

class_B("Ram","raja","Ziva","sam")'''

#Keyword argument Function
'''
def karan(name,age):
    print(name,"age is",age)
karan(age=25,name="sam")'''

#Arbitrary Keyword Function
'''
def biodata(**data):
    print(data)

biodata(name="karan",age=21,gender="Male")
'''
#Default paramter function
'''
def home(name,city="Madurai"):
    print(name,"is from",city)

home("Karan")'''
'''
#Passing List in Argument Function
def total(marks):
        return sum(marks)

print(total([12,34,56,78,98]))'''

#Recursive Funtion
'''
def factorail(x):
        if x==1:
                return 1
        else:
                return (x*factorail(x-1))
print(factorail(5))
'''
'''
#Lambda function
c=lambda a:a+50
e=lambda a,b:a*b
d=c(20)+e(10,2)
print(d)'''







