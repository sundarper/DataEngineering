import datetime

print("This is Python data type example")

varInt1 = 5
varInt2 = 10
varFlt1 = 2.7
varFlt2 = 4.9
varNone = None
varInt3 = varInt1+varInt2+varFlt1+int(varFlt2)
print(varInt3)
print(type(varInt1), type(varFlt1))
print(type(varNone))

varComp=10+10j
print(type(varComp))

varList=["Sundar", 200, '10', '30', 'Rajan', "Python"]
print(varList)
print(type(varList))
varList.append("Valar")
varList.append("sridevi")
varList.remove("Rajan")
print(varList)

lstLen=len(varList)
print("Length = ", lstLen)

varTuple=(10,40,65,4,'Sundar', 'Sridevi', '100')
print(varTuple)
print((len(varTuple)))
print(type(varTuple))

varDic={"name": "Sundar", "age": "40", "City": "Fairfax"}
print(varDic)
name=varDic.get('name')
age=varDic['age']
print("Name = ", name)
print("Age = ", age)
print(len(varDic.keys()))
print(varDic.values())
print(type(varDic))

varDate=datetime.datetime.now()
print(varDate)
print(datetime.date)
print(varDate.date())

a=100
b=50
varBool=(a==b)
print(varBool)
if(a>b):
    print("A is greater than B")
else:
    print("B greate than A")
print(type(varBool))











