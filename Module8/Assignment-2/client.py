import socket
def main():
	host = '10.10.9.34'
	port = 65432
	server = ('10.10.9.34', 65431)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	message = input("Enter Message: ")
	while message != 'q':
		s.sendto(str(message).encode('ASCII'), server)
		data, addr = s.recvfrom(1024)
		print("Recieved from server: "+ data.decode('ASCII'))
		message = input("Enter another message: ")
	s.close()
if __name__ == '__main__':
	main()