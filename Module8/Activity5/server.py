import socket

def main():
    host = '10.2.133.150'
    port = 5027

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data = str(data).upper()
        print("sending data: " + str(data))
        c.send(str(data).encode())
    c.close()
if __name__ == '__main__':
    main()
