import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.example.com',80))
s.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
response = s.recv(4096)
print(response.decode())
