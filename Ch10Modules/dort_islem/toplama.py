"""
Bu modül toplama işlemi sağlar
"""

def topla(a,b):
    """
    İki sayıyı toplar.

    Args:
        a (float): Birinci sayı.
        b (float): İkinci sayı.

    Returns:
        float: a ve b'nin toplamı.
    """
    return a+b

if __name__ == "__main__":
    # Test kodu
    print(topla(5, 3))  # Çıktı: 8