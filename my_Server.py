import socket
import string

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 4242))
    print('Waitning for connection')
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1)
            if data:
                data=data.decode()
                print(data)
                if data == 'q':
                    s.shutdown(socket.SHUT_RDWR)
                    s.close()
                    break
