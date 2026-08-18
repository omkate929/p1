a=input("enter a name")
if a==a[::-1]:
      print(a,"this is palindrom")
else:
      print(a,"this is not palindrom")




num=int(input("enter the number:"))
if num >0 :
          print(num,"+ve")
else:
          print(num,"-ve")


a=list(range(-21,22))
pos=[]
neg=[]
zero=[]
for i in a:
    if i>0:
        pos.append(i)
    elif i<0:
       neg.append(i)
    else:
       zero.append(i)

print("+ve---->",pos)
print("-ve---->",neg)
print("zero--->",zero)
