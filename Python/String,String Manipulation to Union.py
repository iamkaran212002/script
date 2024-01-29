# string & string function
'''a="Karan subramanian"
print(a)
print(type(a))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.count("a"),a.count("n"))
print(a.endswith("n"))
print(a.find("a" ,5))
print(a.replace('a' , 'A'))
a="karan 1234"
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isnumeric())
print(a.isalnum())
print(a.istitle())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.isprintable())
print(a.isspace())
print(a.isascii())'''

'''a="he\nis\ngood"
print(a)
print(a.splitlines())
print(a.splitlines(True))
a="Karan is very smart"
print(a.split(' '))
b='   karan    '
print(len(b.strip()))
print(len(b.lstrip()))
print(len(b.rstrip()))
c='12-03-2022'
print(c.partition('-'))
print(c.rpartition('-'))
'''
# string manipulation

'''a='saran'
print(a)
print(a[3:])
print(a[1:3])
print(a[-2:])
print(a[-5:-3])'''

'''a=int(input('Enter the No:'))
print(a>=10 and a<=20)
print(a>=10 or a<=20)
print(not (a>=10 or a<=20))'''

# Bitwise operator
# a = 25
# print(a >> 2)

# If statement in python
'''
print('Given No is Even or not')

a = int(input("Enter the NO:"))
if a % 2 == 0:
    print("Even number")
else:
    print("Odd Number")
'''
"""
a = input("Enter the Your Name:")
b = int(input("Enter Your Age:"))

if b >= 18:
    print(a, "age is", b, "You are eligible to vote")
else:
    print(a, "age is", b, "You are not eligible to vote")
"""
# Elseif statement
'''
days = int(input("Enter the No of Days:"))
if days == 0 :
    print("No Fine")
elif (days>=1 and days<=5):
    print("Your Fine amount is",days*0.5,"Rupee")
elif (days>5 and days <= 10):
    print("your Fine Amount is",days*1,"Rupee")
elif (days >10 and days <= 30):
    print("Your Fine Amount is",days*5,"Rupees")
else:
    print("Your Membership is Cancelled")
'''

#Nested If Statement
"""
m1,m2,m3=list(map(int,input("Enter the number:").split()))
total=m1+m2+m3
average=total//3.0
print("Total:",total)
print("Average:",average)
if m1>=35 and m2>=35 and m3>=35 :
    print("Result:Pass")
    if average>90 and average<=100 :
        print("Your Grade id A")
    elif average<80 and average>=89 :
        print("Your Grade is B")
    elif average<70 and average>=79 :
        print("Your Grade is C")
    else :
        print("Your Grade is D")
else:
    print("Result:Fail")
"""
'''
# While Loop
i = int(input("Enter the number:"))
j = int(input("Enter the limit:"))
while i <= j:
    if i % 2 == 0:
        i += 1
        continue;
    print(i)
    i += 1
'''
#Range
'''print(list(range(0,10)))
print(list(range(2,8)))
print(list(range(0,21,1)))'''

#For loop
'''
a=10
b=10
for i in range(5) :
    c=a+b
    print(c)
    a+=1
    b+=1
'''

#Nested For Loop
'''
for i in range(0,6):
    for j in range(i):
        print('*',end="")
    print("")
print("")
for i in range(5,0,-1):
    for j in range(i):
        print('*',end="")
    print("")
print("")'''
"""
for i in range(0,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print("")
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print("")
"""
"""
for i in range(97,103):
    for j in range(97,102,1):
        print(chr(j),end="")
    print("")
"""
"""
#while else and for else

i=1
while i<=5:
    if(i==4):
        break
    print(i)
    i+=1
else:
    print("completed")

for i in range(0,21,1):
    print(i)
    if i==16:
        break
else:
    print("loop completed")
"""
"""
a=[1,2,3,4,5]
print(a)
"""
"""
a=[20,45,23,45,89,67,45,78]
print(a.count(45))
print(a.index(89))
print(len(a))
print(max(a),min(a))
a.pop(0)
print(a)
a.remove(45)
print(a)
"""
"""names=["tar"]
print(names)
names.append("sar")
names.append("karan")
print(names)
name=["sara","jeni"]
names.extend(name)
print(names)
names.insert(0,"Bala")
print(names)
print(list(range(15)))
print(list("tarcin"))
a=[10,80,58,96,45]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=['Bala', 'tar', 'sar', 'karan', 'sara', 'jeni']
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)

#Tuple

a=(1,2.5,"Karan",True)
print(type(a))
print(a)
print(a[0:3])
b=list(a)
b.append("Thar")
print(type(b))
print(b)
a=tuple(b)
print(a)

for i in a:
    print(i)

if "Karan" in a:
    print("Yes")
else:
    print("No")


a=(1,6,7,8,9)
b=(2,3,4,5,7)
c=(a,b)
print(c)
print(c[0],c[1],c[0][1])

print(max(a))
print(min(a))"""

"""
#Sets
name={"karan","ziva","Tuple","insert"}
print(type(name),"\n",name)
#access value from for loop
for i in name:
    print(i)
#Adding value
name.add("Sara")
print(name)
#Update another set
a={"Han","Siddu","For"}
name.update(a)
print(name)
name.remove("For")
print(name)
name.discard("insert")
print(name)
name.pop()
"""
#union
"""
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.union(b)
print(c)
a.update(b)
print(a)
a.intersection_update(b)
print(a)
"""
