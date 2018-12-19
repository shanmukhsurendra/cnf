import socket
def main():
    host = '10.10.9.34'
    port = 65534

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("Message from: " + str(addr))
        print("from connected user: " + str(data))
        data = str(data).upper()
        print("sending data: " + str(data))
        s.sendto(str(data).encode(), addr)
    s.close()
if __name__ == '__main__':
    main()