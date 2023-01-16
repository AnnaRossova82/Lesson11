import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.connect(('localhost', 55000))
sock.listen(11)
print("Working now )))....")
client_socket, address = sock.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)
data = ("Hello to client from server connected now)))".encode('utf-8'))
client_socket.send(data)
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    if data == ():
        client_socket.send('Reply')
    if data == ('Test message'):
        client_socket.send('OK, norm')
    else:
        pass
        sock.close()
