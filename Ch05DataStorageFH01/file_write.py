import os
from pathlib import Path
#os kullanarak dosya you oluşturma
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'example.txt')
#Dosyayı yazma modunda açma ve yazma
with open(file_path,'w') as file:
    file.write("Merhaba Dünya!\n")
    file.write("Bu, os modülü ile belirtilen dosya yoludur.\n")

#pathlib kullanarak dosya yolu oluşturma

current_dir=Path(__file__).parent
file_path=current_dir/'example.txt'
with open(file_path,'w') as file:
    file.write("Merhaba Dünya!\n")
    file.write("Bu, pathlib modülü ile belirtilen dosya yoludur.\n")