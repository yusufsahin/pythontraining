tek_tirnak_str='Merhaba'
cift_tirnak_str="Dünya"
cok_satir_str="""Bu
bir
çok
satırlı
stringtir.
"""

print(tek_tirnak_str)
print(cift_tirnak_str)
print(cok_satir_str)

print("Merhaba dünya!")
print('Merhaba dünya!')
print("""
Test
çoklu
satır
""")

#isim=input("İsim giriniz")
#print("Merhaba, {isim}!".format(isim=isim))

print("Merhaba","dünya","!")

#Ayırıcı / Separatör ile
print("Merhaba","dünya","!",sep="-")
print("Merhaba","dünya","!",sep=";")

#Sonlandırıcı

print("Merhaba Dünya!",end=" BİTTİ\n")

yeni_satır_str="\nMerhaba\nDünya"
print(yeni_satır_str)
#Cooking String
tab_str="Merhaba\tDünya"
print(tab_str)
print('O, "Merhaba" dedi')
print("O, \"Merhaba\" dedi")
ters_slas_str="Bu bir ters slash \\"
print(ters_slas_str)

#Concateation / String Birleştirme işlemleri

merhaba="Merhaba"
dünya="dünya"
merhaba_dünya=merhaba+" "+dünya
print(merhaba_dünya)

#Tekrarlama

tekrar_str="Merhaba"*3
print(tekrar_str)

uc_tırnak_str="""Bu bir çok satırlı ve 
'tek tırnak' ile "çift tırnak" 
içeren string"""
print(uc_tırnak_str)

#sring yöntemleri / methodları

s="merhaba"
print(s.upper())
k="DÜNYA"
print(k.lower())
print(s.capitalize())

t="merhaba dünya, merhaba uzay"
print(t.title())

v="    Merhaba Dünya      "
print(len(v))
print(v.strip())
u=v.strip()
print(len(u))

z="merhaba dünya"
print(z.replace("dünya","Python"))

print(z.find("dünya"))

l="merhaba dünya, merhaba uzay, merhaba Python"
print(l.count("merhaba"))

#String Testleri

print("merhaba Python".startswith("merhaba"))

m="merhaba dünya"
print(m.endswith("dünya"))

g="merhaba"
print(g.isalpha())

print("12345".isdigit())

print("    ".isspace())

#String Formatlama

#% operatörü
name="Alice"
age=30
formatted_str="İsim: %s, Yaş: %d" % (name,age)
print(formatted_str)

format_func_str="İsim: {}, Yaş: {}".format(name,age)
print(format_func_str)

#f String

f_str=f"İsim: {name}, Yaş: {age}"
print(f_str)

#Diğer yardımcılar
person={"name":"Alice","age":30}
formatted_dicti_str="İsim: {name}, Yaş: {age}".format(**person)
print(formatted_dicti_str)

from string import Template
template=Template("İsim: $name, Yaş: $age")
formatted_temp_str=template.substitute(name="Alice",age=30)
print(formatted_temp_str)

#Slicing  s[start:stop:step]

h="merhaba dünya"

print(h[0:7])
print(h[8:])
print(h[:7])
print(h[::2])
print(h[::-1])

#split

n="merhaba dünya"
kelimeler=n.split()
print(kelimeler)
csv="elma;armut;çilek"
meyveler=csv.split(";")
print(meyveler)

#join
sozcukler=['merhaba','dünya','merhaba','python']
print(' '.join(sozcukler))
fruits=['apple','banana','ananas']

csv2='|'.join(fruits)
print(csv2)