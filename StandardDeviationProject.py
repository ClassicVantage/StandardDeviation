import csv 

with open("data.csv",newline='') as f:
    reder=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#finding mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n 
    return mean

sqaredList=[]
for no in data:
    a=int (no)-mean(data)
    a=a**2
    squaredList.append(a)

sum=0
for i in squaredList:
    sum=sum+i
result=sum/(len(data)-1)
sd=math.sqrt(result)
print(sd)
