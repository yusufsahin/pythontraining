x=int(input('Bir sayı giriniz: '))
if x>5:
    print("x, 5'den büyüktür")
    if x >10:
        print("x, 10'dan da büyüktür")
elif x==5:
    print("x, 5'e eşittir")
else:
    print("x, 5 'den küçüktür")

if not []:
    print("Empty list is considered False")

a=True
b=False
print(a and b)
print(a or b)
print(not a)

#ab=5
#aB=5
#print(ab)
#print(aB)
#print(ab+aB)

k=7
print(1<k<10)
print(10<k<20)

meyveler=["elma","portakal","mandalina"]
print("elma" in meyveler)
print("üzüm" not in meyveler)
#Object Types
z=42
#z=42.4
print(type(z) is int)
print(isinstance(z,int))

try:
    result=10/0
    #result=10/2
except:
    print("sayi sifira bolunemez")
else:
    print("Hata ile karşılaşılmadı")
finally:
    print("Her durumda çalışır")

count=0
while count<5:
    print(count)
    count+=1

for i in range(10):
    if i==5:
        break
    print(i)

for meyve in meyveler:
    print(meyve)

for index,meyve in enumerate(meyveler):
    print(index,meyve)

names=["Alice","Bob","Charlie"]
ages=[25,30,33]
for name,age in zip(names,ages):
    print(f"{name} is {age} years old")

age=18
status="Adult" if age>=18 else "Minor"
print(status)

m = 4
if m > 0:
    pass #Henüz kodlanmadı
else:
    print("m negatif bir sayı")

numbers=[]
for i in range(10):
    numbers.append(i)
print(numbers)

x = range(3, 6)
for n in x:
  print("sayi" +str(n))