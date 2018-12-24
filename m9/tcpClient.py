import socket
def main():
    host  = '10.10.9.34'
    port = 5012
    s = socket.socket()
    s.connect((host,port))
    count = 0
    initial = s.recv(1024)
    print('received from server : '+ initial.decode())
    message = input("Enter your guess : ")
    while message != 'q':
        count += 1
        s.send(message.encode())
        data = s.recv(1024)
        print('received from server : ' + data.decode())
        if(data.decode() == 'correct!'):
            print("Number of guesses :"+str(count))
            break
        message = input("Enter your guess : ")
    s.close()

if __name__ == "__main__":
    main()