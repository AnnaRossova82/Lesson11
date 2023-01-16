import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
sock.send(bytes('Hello to server from client firs connected now', encoding='utf-8'))
data = sock.recv(1024)
print(data)
sock.close()

sock.connect(('localhost', 55000))
sock.send(bytes('Request', encoding='utf-8'))
data = sock.recv(1024)
print(data)
sock.close()
