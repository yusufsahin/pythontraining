#Class tanımlama
class Arac:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Araba(Arac):
    sayac=0
    def __init__(self, marka,model,kapi_sayisi):
        #attributes/alan/field
        #self.marka=marka
        #self.model=model
        super().__init__(marka,model)
        self.kapi_sayisi = kapi_sayisi
        Araba.sayac+=1

    #classmthod kullanımı
    @classmethod
    def araba_sayisi(cls):
        return cls.sayac
    #method
    def bilgi(self):
        return f"{self.marka} {self.model} {self.kapi_sayisi}"
    def __str__(self):
        return f"{self.marka} {self.model} {self.kapi_sayisi}"

#Nesne / Object Oluşturma
araba1=Araba("Toyota","Corolla",4)
araba2=Araba("BMW","320",4)
print(Araba.araba_sayisi())

print(araba1.bilgi())
print(araba2.bilgi())

print(araba1)
print(araba2)

#Operatör Aşırı Yükleme (Operator Overloading)
#Operatör aşırı yükleme, Python'da operatörlerin özel anlamlar kazanmasını sağlar.
# Örneğin, + operatörünün __add__ yöntemi ile aşırı yüklenmesi.

class Vektor:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vektor(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"{self.x},{self.y}"

vektor1=Vektor(2,3)
vektor2=Vektor(4,5)
vektor3=vektor1+vektor2
print(vektor3)

#Özellikler  ve Dekorator

class Dikdortgen:
    def __init__(self,en,boy):
        self.en=en
        self.boy=boy
    @property
    def alan(self):
        return self.en * self.boy
dikdortgen=Dikdortgen(2,3)
print(dikdortgen.alan)