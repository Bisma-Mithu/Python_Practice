#List
#List: An ordered, changeable collection that allows duplicates (e.g., [1, 2, 2]
#Practice
Cars=["BMW", "Bugatti", "Ferrari", "Honda", "Lamborghini" ]
print(Cars)
print(Cars[2])
print('Hello')

Subject=['Urdu' , 'English', 'Math', 'Physics', 'Chemistry', 'PST']
print(Subject[0])
print(Subject[5])
print(Subject)
print(Subject[0:5])

Fruits=['Apple','Orange','Mango','Banana','Kiwi','Papaya']
Fruits.append('Grapes')
Fruits.insert(3,'Pineapple')
Fruits[4]='Banana juice'
print(Fruits)
Fruits.remove('Kiwi')
print(Fruits[0:4])

fruits = ["apple", "banana", "mango", "orange"]
fruits[2:5]
fruits[0]="grapes"
fruits.remove("banana")
fruits.pop(-1)
fruits.insert(1,"kiwi")
fruits.sort()
print(fruits) 

number=[1,2,3,4,5,6,7,8,9,10]
number.pop()
number[9:11]=11,12,13
assending=sorted(number,reverse=True)
print(assending)

#Tuple
#A tuple is a collection which is ordered and unchangeable.(e.g., ("apple", "banana", "cherry")
#Practice
Number=(10,20,30,20,40,50,20)
print(Number.count(20))
print(Number.index(40))
num=list(Number)
print(type(num))
num[2]=300
print(num)
Number=tuple(num)
print(Number)
print(type(Number))

A=('a','b','c','d','e')
B=(1,2,3,4,5)
C=list(A)
D=list(B)
C.extend(D)
print(C)
print(3*A)
print('b' in A)

#Set 
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Practice
Set={'Green','Blue','Purple','Pink','Red'}
print(Set)
Set.add('Yellow')
print(Set)
z={'Black','White'}
Set.update(z)
print(Set)
Set.remove('Green')
print(Set)
Set.discard('Light Blue')
print(Set)

a={1,2,3} 
b={3,4,5}
c=a.union(b)
print(c)
O={1,2,3,4,5}
Set.update(O)
print(Set)
Set.add(5)
print(Set)
print(len(Set))
Q=list(O)
Assending=sorted(Q,reverse=True)
Dessending=sorted(Q,reverse=False)
print(Assending)
print(Dessending)

#Dictionary
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Practice
K={
   'brand':'Toyota' ,
   'model':'Corolla',
   'year':2020
   }
K['color']='Black'
print(K.keys())
print(K.values())
print(K)
K.pop('model')
print(K)

Student={
    'Ali':85,
    'Sara':92,
    'Hassan':78
}
for name in Student:
    Student[name]+=5
print(Student)
Student['Nayyab']=100
print(Student)



