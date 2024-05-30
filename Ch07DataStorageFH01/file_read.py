# Dosyanın tüm içeriğini okuma
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# Dosyayı satır satır okuma
with open('example.txt', 'r') as file:
    line=file.readline()
    while line:
        print(line,end='')
        line=file.readline()
# Dosyanın tüm satırlarını liste olarak okuma
with open('example.txt','r') as file:
    lines= file.readlines()
    for line in lines:
        print(line,end='')
#'for' döngüsü kullanarak dosyayı okuma
with open('example.txt','r') as file:
    for line in file:
        print(line,end='')