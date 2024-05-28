#Değişken ve değer atama
x=5
a=4.5
name="John"
is_student = True
print(x)
print(a)
print(name)
print(is_student)
#Değeri tekrar atama
x=10
print(x)


#değişken adı sayı ile başlamaz
#2degiken=5

degisken2=5
print(degisken2)
#Hatalı tanımlama
#benim-degiskenim=5
#print(benim-degiskenim)

name="Alice"
print(name.upper())
print(name.lower())
#Operatörler
k=5
l=7
print(k+l)

str1= "Hello"
str2="World"
print(str1+str2)

c=5
c=c+7
c+=7
print(c)

d=24
#d/=2
d//=2
print(d)

#Python types

#int
#float
#str
#bool

age=25
height=5.9
firstname="John"
bool=True
print(age)
print(height)
print(firstname)
print(bool)

#Switching Types

t="123"
print(type(t))
print(t+str(1))
u=int(t)
print(u+1)

#List

meyveler=["apple","banana","cherry"]
print(meyveler)
print(meyveler[0])
meyveler[0]="ananas"
print(meyveler)
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
mixed=[1,"apple",3.5,True]
print(mixed)

#Tuples - Demetler
point=(20,30)
print(point)
print(type(point))
coordinates=(5.0,6.7,8.3)
print(coordinates)

#dictionaries / sözlükler

person={"name":"John","age":25,"city":"New York"}
print(person)
print(type(person))

person["name"]="Jane"
print(person)
print(person["age"])
del person["age"]
print(person)

for key in person.keys():
    print(key,person[key])

for key,value in person.items():
    print(key,value)

# Tüm anahtarları alma
keys = person.keys()
print(keys)  # dict_keys(['name', 'age'])

# Tüm değerleri alma
values = person.values()
print(values)  # dict_values(['John', 26])

# Tüm anahtar-değer çiftlerini alma
items = person.items()
print(items)  # dict_items([('name', 'John'), ('age', 26)])

person.update({"city":"Texas"})
print(person)
# İç içe sözlük tanımlama
person2 = {
    "name": "John",
    "age": 25,
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# İç içe sözlüğe erişim
print(person2["address"]["city"])  # New York
print(person2["address"]["zip"])   # 10001
