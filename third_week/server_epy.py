# this module will be imported in the into your flowgraph
import socket
import string
import sys



def gr_server(tt):
## pi=pigpio.pi()
## for gpioin in (21,20,26,16,19,13,5,6):
##     pi.set_mode(g, gpio.OUTPUT)
##     pi.write(g, 0)
    while True:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('192.168.2.2', 4242))
        print('Waitning for connection')
        sock.listen(1)
        conn, addr = sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1)
                if data:
                    data=data.decode()
                    print(data)
                    if '*' in data:
                        tt.f=tt.f+10000 # Frequency increment when receiving '*'
                        tt.set_f(tt.f)
                        print("f:"+str(tt.f))
                    if '+' in data:
                        tt.f=tt.f-10000 ## FREQUENCY increment when receiving '+'
                        tt.set_f(tt.f)
                        print("f:"+str(tt.f))
                    if 'q' in data:
                        print('bye')
                        sock.shutdown(socket.SHUT_RDWR)
                        sock.close()
                        break

