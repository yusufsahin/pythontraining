import ctypes

libc = ctypes.CDLL('libc.so.6')
libc.printf(b"Merhaba, Dünya!\n")

#Linux veya unix