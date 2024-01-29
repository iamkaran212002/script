import datetime as DT

current_date=DT.datetime.now()
print(current_date)
print("")
sas=DT.date(2024,1,19)
print(sas,sas.year,sas.month,sas.day)
print("")
n=DT.time(10,45,6,7787)
print(n,n.hour,n.minute,n.second,n.microsecond)
print("")
m=DT.datetime(2024,1,19,12,00,00,00000)
print(m)
print(m.time(),m.date())
print()
current=DT.datetime.now()
new_year=DT.datetime(2025,1,1)
difference=new_year-current
print(difference)
print(difference.total_seconds())
print()
current=DT.datetime.now()
s=current.strftime("%A %b %d %Y")
print(s)
print()




