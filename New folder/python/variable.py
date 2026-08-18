# # # # # marks=int(input("enter your number:"))

# # # # # if(marks >= 90):
# # # # #     print("grade D")
# # # # # elif(marks >= 70):
# # # # #     print("grade C")
# # # # # elif(marks >= 50):
# # # # #     print("grade B")
# # # # # else:
# # # # #     print("you are fail") 

# # # # # variable =10
# # # # # om=49.5
# # # # # tejas="hello"
# # # # # print(type(variable))
# # # # # print(type(om))
# # # # # print(type(tejas))

# # # # # var=(str(input("enter your name:")))
# # # # # var2=(int(input("enter your  age:")))
# # # # # kate=var,var2
# # # # # print(kate)

# # # # # var="omkate"
# # # # # var2=var[2:4]
# # # # # print(len(var2))



# # # # # var="omkate"
# # # # # var2=var[2:4]
# # # # # print(var2)

# # # # # color = input("enter a color:")

# # # # # if color == "red":
# # # # #     print("stop")
# # # # # elif color == "yellow":
# # # # #     print("wait")
# # # # # elif color == "green":
# # # # #     print("go")
# # # # # else:
# # # # #     print("invalid color")

# # # # # var1=input("enter your name")

# # # # # var2=(len(var1[0:3]))
# # # # # print(var2)

# # # # # var3=(type(var2))
# # # # # print(var3)

# # # # # marks=int(input("enter your marks:"))

# # # # # if (marks >=80 and marks <=100):
# # # # #     grade = "A"
# # # # # elif(marks >=70 and marks<=79):
# # # # #     grade = "B"
# # # # # elif(marks >=40 and marks<=69):
# # # # #     grade = "C"
# # # # # else:
# # # # #     grade = "F"

# # # # # print("the grade of student is:", grade)

# # # # # string_num = "100"
# # # # # num2 = int(string_num)

# # # # # result = num2 + 50
# # # # # print(result)

# # # # # age = int(input("enter your age:"))

# # # # # if (age >= 18):
# # # # #     if (age >=90):
# # # # #         print("you must drive")
# # # # #     else:
# # # # #         print("you drive")
# # # # # else:
# # # # #     print("not drive")

# # # # # num=int(input("enter your number:"))

# # # # # num2=num%2

# # # # # if(num2==0):
# # # # #     print("even")
# # # # # else:
# # # # #     print("odd")

# # # # # a=int(input("enter your number:"))
# # # # # b=int(input("enter your number:"))
# # # # # c=int(input("enter your number:"))

# # # # # if (a >=b and a >= c):
# # # # #         print("a is greatest")
# # # # # elif(b >= c):
# # # # #     print("b is greatest")
# # # # # else:
# # # # #     print("c is greatest")

# # # # # x=(int(input("enter your number:")))

# # # # # if(x % 7==0):
# # # # #     print("divisible")
# # # # # else:
# # # # #     print("not divisible")
# # # # # om=["a","g","t","h"]
# # # # # om.pop(2)
# # # # # print(om)

# # # # # movie=[]
# # # # # mov1=input("enter your fav movie:")
# # # # # mov2=input("enter your fav movie:")
# # # # # mov3=input("enter your fav movie:")
# # # # # movie.append(mov1)
# # # # # movie.append(mov2)
# # # # # movie.append(mov3)

# # # # # print(movie)
# # # # # movie.pop(2)


# # # # # student = {
# # # # #     "name":"om",
# # # # #     "age": "20",
# # # # #     "marks":90.9,
# # # # #     "subject": {
# # # # #         "python":90,
# # # # #         "java":80,
# # # # #         "c++":70,
# # # # #     },
# # # # #     "city":"pune",
# # # # # }
# # # # # new_dict={"name" : "tejas"}
# # # # # student.update(new_dict)
# # # # # print(student)

# # # # # set1 = {1,2,3,4}
# # # # # set2 = {2,4,5,6}
# # # # # print(set1.union(set2))

# # # # # marks = {}

# # # # # y = int(input("enter your marks:"))
# # # # # marks.update({"phy " : y})

# # # # # y = int(input("enter your marks:"))
# # # # # marks.update({"che " : y})

# # # # # y = int(input("enter your marks:"))
# # # # # marks.update({"math " : y})

# # # # # print(marks)

# # # # # 1 to 100 values

# # # # # i = 1
# # # # # while i<=100:
# # # # #     print(i)
# # # # #     i+=1

# # # # # 100 to 1 values

# # # # # i = 100
# # # # # while i>=1:
# # # # #     print(i)
# # # # #     i-=1

# # # # # multiplicationn table

# # # # # i=int(input("enter your number:"))
# # # # # while i<=10:
# # # # #     print ("3 *",i,"=",3*i)
# # # # #     i +=1

# # # # # y = [1,2,3,4,5,6,7,8,9,10]

# # # # # x=0

# # # # # while x < len(y):
# # # # #     print(y[x])
# # # # #     x+=1

# # # # #break loop

# # # # # i=1
# # # # # while i<=10:
# # # # #     if(i==5):
# # # # #         break
        
# # # # #     print(i)
# # # # #     i+=1

# # # # # # continue
# # # # # i=1
# # # # # while i<10:
# # # # #     if(i%2==0):
# # # # #         i+=1
# # # # #         continue
# # # # #     print(i)
# # # # #     i+=1

# # # # #for loop

# # # # # nums=[1,4,9,16,25,36,49,64,81,100]

# # # # # for num in nums:
# # # # #     if(num == 36):
# # # # #         print("found")
# # # # #         break
# # # # #     print(num)

# # # # # for i in range(10):
# # # # #     while i<=10:
# # # # #         if(i==5):
# # # # #             print("found")
# # # # #         i+=1

# # # # #     break
# # # # #     print(i)

# # # # #1 to 100 values

# # # # # for i in range(1,100):
# # # # #     print(i)

# # # # # 100 to 1 values

# # # # # for i in range(100,0,-1):
# # # # #     print(i)

# # # # # n = int(input("enter your number:"))

# # # # # for i in range(1,11):
# # # # #     print(n*i)

# # # # # n = 5

# # # # # sum =0
# # # # # for i in range(1,n+1):
# # # # #     sum += i
# # # # # print(sum)

# # # # # print("total sum:",sum)

# # # # #function

# # # # # def var1(a,b,c):
# # # # #     sum=a+b+c
# # # # #     avg=sum/3
# # # # #     print(avg)

# # # # # var1(2,4,6)

# # # # # num =[1,23,45,56,76,2343,56,78,34,56,78,90]

# # # # # def len_num(num):
# # # # #     print(len(num))

# # # # # len_num(num)


# # # # # #calculator

# # # # # num1 =int(input("enter first number:"))
# # # # # num2 =int(input("enter second number:"))



# # # # # num3=float(input("\n1.addition\n2.substraction\n3.multiplication\n4.division\nenter your choice:"))

# # # # # if num3==1:
# # # # #     print(num1+num2)
# # # # # elif num3==2:
# # # # #     print(num1-num2)
# # # # # elif num3==3:
# # # # #     print(num1*num2)
# # # # # elif num3==4:
# # # # #     print(num1/num2)
# # # # # else:
# # # # #     print("error")

# # # # # #dollar to inr
# # # # # # def dollar(n):
# # # # # #     inr=n*85
# # # # # #     print("dollar",n,"=" ,inr,"inr")

# # # # # # dollar(100)

# # # # # # f=open("lecture.txt","r")
# # # # # # show=f.read()
# # # # # # print(show)
# # # # # # print(type(show))
# # # # # # f.close()

# # # # # a =[]
# # # # # b=["om",80,"pune","python"]
# # # # # def var1():
# # # # #     name=input("enter your name:")
# # # # #     age=input("enter your age:")
# # # # #     marks=input("enter your marks:")
# # # # #     student={
# # # # #         "name":name,
# # # # #         "age":age,
# # # # #         "marks":marks
# # # # #     }
# # # # # #     a.append(student)
# # # # # #     print(a)

# # # # # # def display_stu():
# # # # # #     print(b)


# # # # # # print("1.add student\n2.display student\n")

# # # # # # choice=int(input("\nenter your choice:"))

# # # # # # if choice==1:
# # # # # #     var1()
# # # # # # elif choice==2:
# # # # # #     display_stu()
# # # # # # else:
# # # # # #     print("invalid choice")

# # # # # a=["om","pune","python"]

# # # # # def add():
# # # # #     item=input("enter you add:")
# # # # #     a.append(item)
# # # # #     print(add)


# # # # # def sorts():
# # # # #     print(len(a))
# # # # #     a.sort()
# # # # #     print(a)

# # # # # def inserts():
# # # # #     item =("enter you insert:")
# # # # #     a.insert(2,item)
# # # # #     print(a)

# # # # # choice = int(input("1.add\n2.sorts\n3.insert\nenter your choice:"))


# # # # # if  choice==1:
# # # # #     add()
# # # # #     print((a))
# # # # # elif choice==2:
# # # # #     sorts()
# # # # # elif choice==3:
# # # # #     inserts()
# # # # # else:
# # # # #     print("invalid operation")

# # # # # a =int(input("enter first player number:"))

# # # # # num=[]
# # # # # num.append(a)
# # # # # print(num)

# # # # # b=int(input("enter second player number:")) 
# # # # # num2=[]
# # # # # num2.append(b)
# # # # # print(num2)

# # # # # if num2 == num:
# # # # #     print("correct")
# # # # # elif num2!=num:
# # # # # print("wrong")

# # # # #  w is automaticaly create file


# # # # # num=input("enter your comment:")

# # # # # f=open("lecture.txt","w")
# # # # # num2=f.write(num)
# # # # # print(f)

# # # # print(bool(0))
# # # # my_list=[1,2,3,4]
# # # # print(my_list[2])
# # # # str="pynative"
# # # # print(str[1:3])
# # # # result=True and False
# # # # print(result)
# # # # p,q,r=12,13,14
# # # # print(p,q,r)

# # # # print(3*"abc")
# # # # listOne = [20, 40, 60, 80]
# # # # listTwo = [20, 40, 60, 80]

# # # # print(listOne == listTwo)
# # # # print(listOne is listTwo)
# # # # print("om"+"tejas")

# # # # var= "James Bond"
# # # # print(var[2::-1])

# # # # a = [1, 2, 3]
# # # # b = a
# # # # b.append(4)
# # # # print(a)
# # # # x = 10
# # # # y = 3
# # # # print(x % y)
# # # # print('Python' * 2 + ' is fun')
# # # # a, b = 12, 5
# # # # if a + b:
# # # #     print('True')
# # # # else:
# # # #   print('False')

# # # #oops

# # # # class student:
# # # #     name="om"

# # # # name1=student()
# # # # print(student.name)

# # # # class account():
# # # #     def __init__(self,bal,acc):
# # # #         self.balance=bal
# # # #         self.account_no=acc

# # # #     def dabit(self,amount):
# # # #         self.balance =-amount 
# # # #         print("Rs.",amount, "was debited")
# # # #         print("total balance =", self.get_balance())

# # # #     def credit(self, amount):
# # # #         self.balance +=amount 
# # # #         print("Rs.",amount,"was creadited")
# # # #         print("total balance =",self.get_balance())

# # # #     def get_balance(self):
# # # #         return self.balance




# # # # acc1 = account("10000","12345")
# # # # acc1.dabit(100)
# # # # acc1.credit(20)

# # # # class student:
# # # #     def __init__(self ,name,):
# # # #         self.name=name
        
# # # # s1=student("om")
# # # # print(s1.name)

# # # # with open("lacture1.txt","w")as f:
# # # #     student=f.write("hi my name  is om kate ")
# # # #     print(student)

# # # # class bank:
# # # #     def __init__(self,bal,acc):
# # # #         self.balance=bal
# # # #         self.account=acc

# # # #     def debit(self,amount):
# # # #         self.balance-=amount
# # # #         print("rs",amount,"was debited")
# # # #         print("total balance=", self.balance)

# # # #     def creadit(self,amount):
# # # #         self.balance+=amount
# # # #         print("rs",amount,"was debit")
# # # #         print("total balance=",self.balance)

# # # #     def balance(self,self_balance):
# # # #         return self.balance

# # # # s1=bank(10000,12345)
# # # # print(s1.balance,s1.account)
# # # # s1.debit(200)
# # # # s1.creadit(300)
# # # # print(s1.balance)

# # # a=10
# # # b=20

# # # # while (a>=b):
# # # #     print("a is greater than b")
# # # # else:
# # # #     print("b is greater than a")

# # # # for i in range(1,10):
# # # #     while i<10:
# # # #         print("om")

# # # # class student:
# # # #     def __init__(self,phy,chem,biol):
# # # #         self.phy = phy
# # # #         self.chem =chem
# # # #         self.biol =biol

# # # #         print((phy+chem+biol)/3 ,"%")

# # # # s1=student(59,76,87)
# # # # print(s1)

# # # a = input("enter first number:")
# # # b = input("enter second number:")

# # # choice=float(input("1.add\n2.sub\n3.mul\n4.div\nenter your choice:"))

# # # if choice==1:
# # #     print(a + b)
# # # elif choice==2:
# # #     print(a * b)
# # # elif choice==3:
# # #     print(a - b)
# # # elif choice==4:
# # #     print(a / b)
# # # else:
# # #     print("invalid operation")

# # student=[]
# # num1=float(input("enter first number:"))
# # num2=float(input("enter second number:"))

# # print("1.add")
# # print("2.age")
# # print("3 marks")
# # print("4.sub")

# # choice=float(input("enter your choice:"))

# # if choice==1:
# #      num3=num1+num2
# #      student.append(num3)
# #      print(student)
# # elif choice==2:
# #      num3=num1+num2
# #      student.append(num3)
# #      print(student)

# # elif choice==3:
# #      num3=num1+num2
# #      student.append(num3)
# #      print(student)

# # elif choice==4:
# #      num3=num1+num2
# #      student.append(num3)
# #      print(student)
# # else:
# #      print("invalid operation")


# # cap=['d','r','w','e','g','y','t']
# # cap.insert(3,'n')
# # print(cap)

# # traffic=str(input("enter your signal:"))

# # if traffic=="red":
# #      print("stop")
# # elif traffic=="yellow":
# #      print("see the bike,car")
# # elif traffic=="green":
# #      print("go")
# # else:
# #      print("you are not available in signal")

# # with open("lecture2.txt","w")as f:
# #      f.write("hi my name is om kate,jsjh djhd ekre elkrj r klf dkjslkdj rljrk")
# #      print(f)

# # class student:
# #      def __init__(self,name,age,marks,subject):
# #           self.name=name
# #           self.age=age
# #           self.marks=marks
# #           self.subject=subject

# # stu1=student("om",20,90,"python")
# # print(stu1.name)
# # print(stu1.age)
# # print(stu1.marks)
# # print(stu1.subject)
# # stu1=student("rohit",24,80,"jaava")
# # print(stu1.name)
# # print(stu1.age)
# # print(stu1.marks)
# # print(stu1.subject)

# # i=10

# # while i>=20:
# #      print("write")
# # else:
# #      print("wrong")
# # num=30
# # for i in range(1,10):
# #     if i<10:
# #           print("om")
# #     if i==7:
# #           exit()

# # car =["bmw","fortuner","safari"]
# # fruit=["apple","banana","orange"]

# # car.extend(fruit)
# # print(car)

# # car=["bmw","fortuner","safari"]
# # car.insert(2,"audi")
# # print(car)

# # car=["bmw","fortuner","safari"]
# # car.pop()
# # print(car)

# # cart = ['mobile', 'laptop', 'headphones']

# # #charger ko end me add kare
# # cart.append("charger")

# # #smart watch ko index 1 pr add kare
# # cart[1]="smart watch"

# # # #laptop ko remove kare
# # cart1=cart.pop()
# # print(cart1)

# # #last item ko remove kare or usse print kare
# # cart.remove("headphones")

# # #list ko alphabetical kare
# # cart.sort()

# # #final cart
# # print("final cart:",cart)


# # num =int(input("enter a number:"))

# # # if num%2==0:
# # #     print("even")
# # # else:
# # #     print("odd")

# # # num =int(input("enter number:"))
# # # num2=[]

# # # for i in range(num,50):
# # #     num2.append(i)
# # #     print(num2)

# # # for i in range(1,101):
# # #     print(i)

# # # i = 1
# # # while i < 6:
# # #     print(i)
# # #     if i == 3:
# # #         break
# # #     i += 1

# # # import datetime

# # # x=datetime.datetime.now()
# # # y=x.time
# # # print(y)

# # # set1={1,3,5,6,9}
# # # set2={1,4,5,9,2}
# # # set3=[]

# # # set4=set1.union(set2)
# # # set3.append(set4)
# # # print(set3)
# # # user_input =input("enter your number:")
# # # my_list = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]

# # # for i in range(len(my_list)):
# # #     for j in range(i+1,len(my_list)):
# # #         if my_list[i]>my_list[j]:
# # #             swap=my_list[i]
# # #             my_list[i]=my_list[j]
# # #             my_list[j]=swap
# # #             print(my_list)

# # # fruit={"apple","mango","banana","graps"}
# # # fruit.add("cherry")
# # # x=fruit.copy()
# # # print(x)
# # # # fruit.clear()
# # # print(fruit)

# # # fruit1=["apple","mango","banana"]
# # # user=str(input("enter your favourite fruit:"))
# # # index=int(input("enter index to add:"))
# # # fruit1.insert(index,user)

# # # print("update list:",fruit1)

# # # import cowsay

# # # num = 5
# # # table = ""

# # # for i in range(1, 11):
# # #     table += f"{num} x {i} = {num*i}\n"

# # # cowsay.cow(table)

# # user1 =int(input("enter first number:"))
# # num1=[]
# # num1.append(user1)

# # while True:
# #     guess =int(input("enter 1-100 number"))

# #     if num1 < guess:
# #         print("small number")

# #     elif num1 > guess:
# #         print("to large")

# # #     else:
# # #         print("you won the game")
# # # #     break


# # #gussing game

# # import random

# # number=random.randint(1,200)


# # while True:

# #     guess_number=int(input("enter your (1-200)number:"))

# #     if guess_number < number:
# #         print("to small")
# #     elif guess_number > number:
# #         print("to large")
# #     else :
# #         print("Correct! You guessed it 🎉")
# #         break

# # num =int(input("enter your number:"))

# # if num%2==0:
# #     print("even")
# # else:
# #     print("odd")

# # num =int(input("enter number:"))
# # num2=[]

# # for i in range(num,6):
# #     num2.append(i)
# #     print(num2)

# # score =int(input("enter your number:"))
# # num4=[]

# # if score<=100 and score>=90:
# #     num1= "A"
# #     num4.append(num1)
# # elif score<=89 and score>=60:
# #     num2= "B"
# #     num4.append(num2)
# # elif score<=59 and score>=35:
# #     num3= "C"
# #     num4.append(num3)
# # else:
# #     print("fail")

# # age=20
# # print(f"hi my name is om kate.my age is,{age}.my clg name gfcct.and my grade in clg+{num4}")

# import random

# number=random.randint(1,200)

# while True:
#     guess_number=int(input("enter (1-200) number: "))

#     if guess_number < number :
#         print(" to small")
#     elif guess_number > number:
#         print("to large")
#     else:
#         print("Correct! You guessed it 🎉",number)

# import random

# while True:
#     play=str(input("game start? (yes/no):"))

#     if play == "yes":
#         user_dice=random.randint(1,100)
#         computer_dice=random.randint(1,100)

#         print("user dice:",user_dice)
#         print("computer_dice:",computer_dice)

#     elif play=="no":
#         print("Game over")
#         break

#     elif user_dice<computer_dice:
#         print("computer win Game 🥰")
#     elif user_dice>computer_dice:
#         print("user win Game")
#     elif user_dice!=computer_dice:
#         print("bad 😡")

# class student():
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

# student_detail=student("om",20,90)
# print(student_detail.name)

# num=int(input("enter your number:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#         print()





# a=6

# for i in range(1,a):
#     for j in range(i):
#         print("*",end="")
#     print()

# class bank():

#     def __init__(self,balance,balance3):
#         self.balance=balance
#         self.balance3=balance3
       

#     def creadit(self,balance1):
#         amount=int(input("enter your amount:"))

#         if amount<=self.balance:
#             print(self.balance)
#         elif amount>=self.balance:
#             print("self.balance")


# detail=bank(1000,2000)
# detail.creadit(200)


# a=int(input("enter number:"))
# for i in range(1,11):
#     print(a*i)

# a=int(input("enter number:"))
# b=1

# while b<11:
#     print(a,"*",b,"=",a*b)

#     b+=1

# dict={

# }
# list=[]
# tuple=( )
# set=( )
# print(type(dict))
# print(type(list))
# print(type(tuple))
# print(type(set))

# x=int(input("enter any number:"))
# y=x*x*x
# print(y)

# for x in range(1,6):
#     for y in range(x,6):
#         print(y)


# f=open("om.txt","w")
# f.write("hi om")
# f.close()

# i=input("enter any number")
# print(i)

# age=input("enter any number:")
# i=int(age)
# print(i)

# i=[1,2,3,4,5,6,7]
# i.append(8)
# i.insert(1,2)
# print(i[2])
# i.pop()
# print(i[1:5])
# print(len(i))
# i.remove(2)
# i.pop()
# print(i)

# i=int(input("enter any number:"))

# if i%2==0:
#     print("even")
# else:
#     print("odd")

# i=str(input("enter your name:"))

# if i=="red":
#     print("stop")
# elif i=="yellow":
#     print("wait")
# elif i=="green":
#     print("go")
# else:
#     print("invalid color")

# i=1

# while i<=10:
#     print("om")
#     i+=1
# print(len("om"))

# x=int(input("enter your number:"))
# for i in range(1,11):
#     print(x,"*",i,"=",i*x)

# n = int(input("Enter number: "))

# i = 1

# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1

# for i in range(1,11):
#     if i==5 or i==8:
#         print(5)
#         continue
#     print("om")


# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,7):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# import random

# A=random.randint(1, 200)

# while True:
#     guess = int(input("guess a number between 1 and 200:"))

#     if guess < A:
#         print("to low")
#     elif guess > A:
#         print("too high")
#     elif guess == A:
#         print("correct!")

# for i in range(1,7):
#     for j in range(i,7):
#         print("*",end="")
#     print()

# for i in range(7,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# i=5

# while i<=10:
#     print("om")
#     i+=1

# a=input("enter a name")
# if a==a[::-1]:
#       print(a,"this is palindrom")
# else:
#       print(a,"this is not palindrom")


# num=int(input("enter the number:"))
# if num >0 :
#       print(num,"+ve")
# else:
#       print(num,"-ve")


# a=list(range(-21,22))
# pos=[]
# neg=[]
# zero=[]
# for i in a:
#       if i>0:
#             pos.append(i)
#       elif i<0:
#             neg.append(i)
#       else:
#             zero.append(i)
# print("+ve---->",pos)
# print("-ve---->",neg)
# print("zero--->",zero)

# a=int(input("enter tour number:"))

pos=[]
neg=[]
zero=[]
for i in range(-22,22):
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)
    elif i==0:
        zero.append(i)

print("+ve---->",pos)
print("-ve---->",neg)
print("zero--->",zero)