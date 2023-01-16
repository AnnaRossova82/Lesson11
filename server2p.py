import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.connect(('localhost', 55000))
sock.listen(11)
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024).decode('utf-8')
        print('Message', result.decode('utf-8'))
        x = str(result)
        client.send(len(x))
        client.close()

