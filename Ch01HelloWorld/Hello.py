print("Hello world")
#print(3/4)
#print(12//3)
#print(12/3)
#help()
#help('for')
#import  math
#print(dir(math))

def add(a, b):
    """
    İki sayıyı toplar ve sonucu döner.

    Parametreler:
    a (int or float): Toplama işlemindeki ilk sayı.
    b (int or float): Toplama işlemindeki ikinci sayı.

    Döndürür:
    int or float: Toplama işleminin sonucu.
    """
    return a + b

print(add(5,6))
print(add.__doc__)

class MyClass:
    """
    Bu sınıf, basit bir örnek sınıfıdır.

    Nitelikler:
    value (int): Sınıfın bir niteliği.
    """
    def __init__(self,value):
        """
        MyClass sınıfının kurucusudur.

        Parametreler:

        value (int): Sınıfıb başlangıç değeri.
        """
        self.value=value

    def increment(self):
        """
        value niteliğini 1 arttırır
        """
        self.value += 1
print(MyClass.__doc__)

def addGoogle(a,b):
    """
    İki sayıyı toplar ve sonucu döner.

    Args:
         a (int or float): Toplama işlemindeki ilk sayı.
         b (int or float): Toplama işlemindeki ikinci sayı.

    Returns:
        int or float: Toplama işleminin sonucu
    """
    return a+b

print(addGoogle.__doc__)

import math
def kare_al(x):
    return  x*x
print(kare_al(5))
def carpma(a,b):
    return  a*b

print(carpma(3,2))
print(len("Merhaba Dünya"))
list1=[1,2,3,4,5,6,7,8,9]
print(sum(list1))

sonuc=carpma(a=4,b=3)

print(sonuc)
a=6
b=5
print(a)
print(b)

print(carpma(a,b))

def toplama(a,b=3):
    return a+b

#toplama(5)
print(toplama(5))
print(toplama(5,6))

def bilgiler(ad,soyad,yas):
    print(f"Ad: {ad}, Soyad: {soyad}, Yaş: {yas}")
bilgiler(yas=25,soyad="Doe",ad="John")
bilgiler("Jane","Doe",22)

def esnek_fonksiyon(*args):
    for arg in args:
        print(arg)
esnek_fonksiyon(1,2,3,4,5)

def esnek_fonksiyon(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

esnek_fonksiyon(ad="Sue",soyad="Doe")

isim= input("İsim giriniz")
print(f"Merhaba, {isim}!")

list2= [7,11,9,3,5]
print(sorted(list2))