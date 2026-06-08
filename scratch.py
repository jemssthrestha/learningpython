'''print("hello world,", "i am jems")
a=23
b=24
print("sum:", a+b)
c=99.9
d=None
print(type(c))
print(type(d))
# hi i am comments
print(a==b)
e=6
e+=5
print(e)
print(True or False)

# Type conversion, automatic converion
v=2
w=3.5
print(v+w)

# Type casting
f="2"
g=5
print(int(f)+g)
print(type(f))
print(type(int(f)))

# input in python
name=input("Enter your name: ")
print(name)
print(type(name),name)
z=input("enter number: ")
print(type(int(z)),z)

o=2
print(o**3)
'''

# string and conditional statements
'''str1= "This is a string.\nwe arw creating it in python"
print(str1)
"scape sequence charecters= \n \t"
"concatination= '+' opearator"
Str1="hello"
Str2="world"
print(Str1+" "+Str2)
print(len(Str1))'''


'''# indexing
str="Jems Shrestha"
print(str[0])
# slicing
print(str[0:3])
print(str[ :3])
print(str[1: ])
#negative indexing
print(str[-3:-1])'''

'''#string function
str="i am studing python"
print(str.endswith("on"))
print(str.capitalize())
print(str.replace("o","a"))
print(str.replace("python","java"))
print(str.find("o"))
print(str.count("o"))'''

'''# qn
name=input("Enter your name: ")
print("length of string is: ",len(name))
p="hi i am $ and is 566$"
print(p.count("$"))'''

# Condtional Statements
'''age=21
if(age>18):
    print("can vote")
    print("can drive")
elif(age==18):
    print("is 18")
else:
    print("age<18")

marks=int(input("Enter your marks: "))
if(90<marks<=100):
    print("A+")
elif(marks>80):
    print("A")
elif(marks>70):
    print("B+")
elif(marks>60):
    print("B")
elif(marks>50):
    print("C+")
else:
    print("Fail")

age=16
weight=40
if(age>18):
    if(weight>25):
        print("can donate blod")
else:
    print("cannot donate blod")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>=b and a>=c):
    print("first is largest.")
elif(b>=c):
    print("second is largest.")
else:
    print("third is largest.")'''

# today no progress
# print("hi")

'''# lists and Tuple
marks=[93.5,98.5,87.5,23.3]
print(marks)
print(type(marks))
print(marks[0])
marks[1]="jems"
print(marks)
# list slicing
print(marks[1:3])
marks.append("hi")
print(marks)
list=[3,45,7,4,7,9,22]
print(list.sort(reverse=True))
print(list)
lists=["banana","apple","litchi"]
lists.sort()
print(lists)
print(lists.reverse())
print(lists)
lists.insert(6,"mango")
print(lists)
print(lists[3])
print(lists.remove("mango"))
print(lists)
lists.pop(2)
print(lists)'''

# tuples
'''tup=(1,2,3,4,5,6,2)
print(type(tup),tup)
print(tup[1])
tupl=(1,)
print(tupl)
# tuple slicing
# tuple methods
print(tup.index(2))
print(tup.count(2))'''

'''movies=[]
mov1=input("enter movie 1")
mov2=input("enter movie 2")
mov3=input("enter movie 3")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

movies.append(input("enter movie 1"))
movies.append(input("enter movie 2"))
movies.append(input("enter movie 3"))
print(movies)

list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list1==list1):
    print("yes is palindrome")
print("and")
if(copy_list2==list2):
    print("yes is palindrome")'''

# starting lecture 4
#dictionary and sets
'''dict={
    "subjects":["java","html","mth","phy"],
    "topics":("dict","tuple","sets"),
    "name":"jems",
    "learning":"coding",
    "age":35,
    "isadult":True,
    "marks":99.9,
    12.99:99.99
}
print(dict["topics"])
print(type(dict))
dict["name"]="ram"
dict["surname"]="shrestha"
print(dict)
null_dict={

}
print(null_dict)
student = {
    "name": "jems stha",
    "subjects": {
        "phy": 99,
        "che": 99.9
    }
}

print(student["subjects"]["phy"])
print(len(list(student.keys())))
print(list(student.values()))
pair=list(student.items())
print(pair[0])
print(student["name"])
print(student.get("name2"))
print(student.update({"city":"ktm"}))
print(student)'''

# now sets in python
'''collection={1,2,3,4,"hello","world","world"}
collection.add("hi")
collection.remove(1)
collection.add((34,35,345))
print(collection)
print(collection.pop())
# collection.clear()
print(collection)
emptyset=set()
print(type(emptyset))
set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))'''

# Practice qn
'''marks={}
x=int(input("Enter phy: "))
marks.update({"phy": x})
y=int(input("Enter eng: "))
marks.update({"eng": y})
z=int(input("Enter che: "))
marks.update({"che": z})
print(marks)'''

# Now loops

#whilte loops
'''count=100
while count>=0:
    print(count)
    count-= 1

i=1
while i<=10:
    print(3*i)
    i+=1

nums=[1,2,3,4,5,6,7,8,9,10,11]
i=0
while i<len(nums):
    print(nums[i])
    i+=1

num=[1,2,3,4,5,6,7,8,9,10,11]
i=0
while i<len(num):
    if(num[i]==7):
        print("found")
        break
    else:
        print("finding..")
        i+=1


i=1
while i<=10:
    if(i==2):
        i+=1
        continue

    print(i)
    i+=1'''

#for loops
'''nums=[1,2,3,4]
for i in nums:
    print(i)
charecter="jems shrestha"
for i in charecter:
    print(i)
else:
    print("ends")

char="jems shrestha"
for i in char:
    if(i=="t"):
        print("t found")
        break
    print(i)
else:
    print("ends")

# practice qn
nums =(1,2,3,4,5,7,6,55,44,77,88,90)
x=55
idx=0
for el in nums:
    if(el==x):
        print("is found in ", idx)
    idx+=1

# range function
for el in range(2,10,2):
    print(el)
for el in range(10,0,-1):
    print(el)
for el in range(1,11):
    print(3*el)
for i in range(5):
    pass'''


# now chapter 6
# function and recursion

'''def calc_sum(a,b):
    sum=a+b
    print(sum)

calc_sum(1,2)
calc_sum(12,7)

def calc_sum(a,b):
    return a+b

sum= calc_sum(1,2)
print(sum)
sum=calc_sum(12,7)
print(sum)

def print_hello():
    print("hello")
print_hello()

def calculate_avg(a,b,c):
    avg=(a+b+c)/3
    print("avg: ", avg)
calculate_avg(1,2,3)'''

# Built in function
# User defined funtion
'''cities=["ktm","pkr","rth"]
heros=["ram","jems","shyam","hari"]
print(heros[0],end=" ")
print(heros[1],end="\n")
def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)

def print_len(list):
    print(len(list))
print()
print_len(cities)
print_len(heros)

fact=1
def factorial(n,fact):
    for i in range(1, n+1):
        fact*=i
    print(fact)
factorial(5,fact)

def U2N(usd):
    npr=usd*134
    print("USD values is: ", usd ,"=","npr: ", npr)
U2N(190)

def oddeven(num):
    if(num%2==0):
        print("is even")
    else:
        print("is odd")
oddeven(4)'''

# recursion- function it self repeatedly
'''def sum(num):
    if(num==0):
        return
    print(num)
    sum(num-1)
sum(4)


def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
fact=factorial(5)
print(fact)

def natural(n):
    if(n==0):
        return
    print(n)
    natural(n-1)
natural(5)

def natural(n):
    if(n==0):
        return 0
    print(n)
    return natural(n-1)+n

sum=natural(5)
print(sum)'''

num=[1,2,3,4,5,6,7,8,9,10,11]
def plist(list, index=0):
    if(index==len(list)):
        return
    print(list[index])
    plist(list, index+1)
plist(num)


    

    