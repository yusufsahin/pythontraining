import sys

print("Bu normal bir mesajdır",file=sys.stdout)
print("Bu bir hata mesajıdır",file=sys.stderr)

import  warnings
warnings.warn("Bu bir uyarıdır",UserWarning)

#try, except, else ve finally blokları

try:
    x=1/1
    #x=1/0
except ZeroDivisionError:
    print("Bir sıfıra bölme hatası meydana geldi.")
else:
    #Hata oluşmadığında çalışacak kod
    print("Hata oluşmadı.")
finally:
    print("Her durumda çalışır")

#Birden fazla istisna

try:
    x=int("abc")
except ValueError:
    print("Bir değer hatası meydana geldi.")
except TypeError:
    print("Bir tür hatası meydana geldi.")

try:
    y=int("abc")
except (ValueError, TypeError) as e:
    print("Bir hata meydana geldi.",e)

#argümanlar
try:
    z=int("abc")
except ValueError as e:
    print("Bir değer hatası meydana geldi.",e)

a=input("Bir sayı giriniz")

try:
    x=1/int(a)
    print(x)
except ZeroDivisionError:
    print("Sıfıra bölme hatası meydana geldi.")
except (ValueError, TypeError) as e:
    print("Bir hata meydana geldi.",e)
finally:
    print("Her zaman çalışacak")

#İstisna hiyerarşisi
#Bütün istisnalar BaseException türetilmiştir.
try:
    raise ValueError("Bu bir değer hatası")
except BaseException as e:
    print("Bir temel istisna meydana geldi:", e)

#Yaygin bir hata
try:
    h=1/0
except:
    print("Bir hata meydana geldi.")

#Kendi istinanızı oluşturma

def pozitif_sayi(sayi):
    if sayi <= 0:
        raise ValueError("Sayı pozitif olmalıdır.")
    return sayi

try:
    print(pozitif_sayi(-1))
except ValueError as e:
    print("Hata:", e)
