
#assert

def karekok(sayi):
    assert sayi>=0,"Sayı negatif olamaz."
    return sayi**0.5
print(karekok(4))
print(karekok(-1))