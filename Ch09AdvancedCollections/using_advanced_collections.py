#filter

sayilar=[1,2,3,4,5,6]
cift_sayilar=filter(lambda x: x%2==0,sayilar)
print(list(cift_sayilar))
tek_sayilar=filter(lambda x: x%2==1,sayilar)
print(list(tek_sayilar))
#Liste Anlayışları (List Comprehensions)

kareler =[x**2 for x in sayilar]
print(kareler)

cift_sayilar2=[x for x in sayilar if x%2==0]
print(cift_sayilar2)
tek_sayilar2=[x for x in sayilar if x%2==1]
print(tek_sayilar2)

#Küme ve Sözlük Anlayışları (Set and Dictionary Comprehensions)

#Küme

sayilar2= [1,2,3,4,4,5,5]
kareler_kumesi= {x**2 for x in sayilar2}
print(kareler_kumesi)

#Sözlük / dictionary
sayilar3=[1,2,3,4,5]
kareler_sozlugu={x:x**2 for x in sayilar3}
print(kareler_sozlugu)

#Lazy List
#Tembel değerleme, ihtiyaç duyulana kadar hesaplamaların ertelenmesini sağlar. Bu, bellek verimliliği sağlar.

sayilar4=(x**2 for x in range(5))
for sayi in sayilar4:
    print(sayi)

#Generator yield

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
for sayi in fibonacci(10):
    print(sayi)

#Generator - next()
def basit_generator():
    yield 1
    yield 2
    yield 3

#yield anahtar kelimesi kullanılarak oluşturulan generator nesneleri üzerinde
# next() fonksiyonu ile iterasyon yapılabilir.
gen=basit_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#Liste anlayışları ile Generator

generator= (x**2 for x in range(5))
for sayi in generator:
    print(sayi)
#Kopyalama problemi
original_p=[1,2,3]
kopya_p=original_p
kopya_p.append(4)
print(kopya_p)
print(original_p)

#Dilimleme ile kopyalama
orijinal=[1,2,3]
kopya=orijinal[:]
kopya.append(4)
print(orijinal)
print(kopya)

#deep copy

import copy
orijinal_d=[[1,2,3],[4,5,6]]
kopya_d=copy.deepcopy(orijinal_d)
kopya_d[0].append(7)
print(kopya_d)
print(orijinal_d)