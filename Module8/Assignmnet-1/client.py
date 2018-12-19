import socket


def main():
	host ='10.2.133.150'
	port =65234

	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))

	message = input("Enter message :   ")
	while message !='q':
		s.send(str(message).encode('ASCII'))
		data = s.recv(1024)
		print("Recieved from server:" + data.decode('ASCII'))
		message=input("Enter another message:  ")
	s.close()

if __name__=='__main__':
	main()