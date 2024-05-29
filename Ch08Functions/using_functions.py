#Basit bir fonksiyon tanımlama

def merhaba():
    print("Merhaba Dünya!")

merhaba()

#Parametre Kullanımı
def topla(a,b):
    return a+b

sonuc=topla(3,5)
print(sonuc)

sonuc2=topla(3.5,5.0)
print(sonuc2)

sonuc3=topla(3.5,5)
print(sonuc3)

#Değişken sayıda parametre
def topla(*args):
    return sum(args)

print(topla(1,2,3,4))

def bilgiler(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}")
bilgiler(isim="Ali",yas=25)
bilgiler(isim="Ahmet",yas=30,sehir="İstanbul")
bilgiler(isim="Mehmet",yas=33,sehir="İstanbul",ilce="Sarıyer")

#Parametrelere Değer atama
#Default/Varsayılan değer

def selamla(isim="Dünya"):
    print(f"Merhaba, {isim}!")

selamla()
selamla(isim="Ali")

def kare(x):
    return  x*x

sonuc4=kare(3)
print(sonuc4)

#Global ve yerel değişkenler

x=10
def fonksiyon():
    x=5
    print(x)
fonksiyon() #çıktı :5
print(x) #çıktı:10

#iç içe fonksiyon tanımlama

def dis_fonksiyon():
    print("Dış fonksiyon")
    def ic_fonksiyon():
        print("iç fonksiyon")
        def son_fonksiyon():
            print("son fonksiyon")
        son_fonksiyon()
    ic_fonksiyon()
dis_fonksiyon()

#kapsam
def dis_fonksiyon_kapsam():
    x=10
    #print(x)
    def ic_fonksiyon_kapsam():
        print(x)
    ic_fonksiyon_kapsam()
dis_fonksiyon_kapsam()

#Docstring

def carp(a,b):
    """Bu fonksiyon 2 sayıyı çarpar"""
    return  a*b
print(carp.__doc__)

#lambda fonksiyonları

kare= lambda x:x*x
print(kare(5))

toplama= lambda a,b:a+b
print(toplama(3,5))

#Lambda Fonksiyonlarını Sıralama Anahtarı Olarak Kullanma - sort

liste =[(2,3),(1,2),(4,1)]
liste.sort(key=lambda  x: x[1])
print(liste)

#lambda ve regex re.sub fonksiyonunda lambda ifadeleri kullanarak dinamik ikameler yapabilirsiniz.

import re
text= "Merhaba 123 Dünya"

result= re.sub(r'\d+',lambda  x: str(int(x.group(0))*2),text)
print(result)
#rekürsif fonksiyonlar
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1) #5*4*3*2*1

print(factorial(5))

def fibonacci(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=10
fib_series=[fibonacci(i) for i in range(n)]
print(fib_series)