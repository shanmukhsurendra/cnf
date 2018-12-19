import socket
def main():
    host = '10.10.9.34'
    port = 65532    

    server = ('10.10.9.34', 65534)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("--->")
    while message != 'q':
        s.sendto(message.encode('ASCII'), server)
        data, addr = s.recvfrom(1024)
        print("Received from server: " + data.decode('ASCII'))
        message = input("--->")
    s.close()
if __name__ == '__main__':
    main()
