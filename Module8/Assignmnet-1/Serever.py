import socket
def conversion(data):
	tokens = data.split()
	if(tokens[1]=="INR"):
		if(tokens[4]=="Dollar"):
			return int(tokens[2])/67
		if(tokens[4]=="Pounds"):
			return (int(tokens[2]))/50.25
		if(tokens[4]=="Yen"):
			return (int(tokens[2])*113.41)/67
	
	if(tokens[1]=="Dollar"):
		if(tokens[4]=="INR"):
			return int(tokens[2])*67
		if(tokens[4]=="Pounds"):
			return (int(tokens[2])*0.75)
		if(tokens[4]=="Yen"):
			return (int(tokens[2])*113.41)

	if(tokens[1]=="Pounds"):
		if(tokens[4]=="Dollar"):
			return int(tokens[2])/0.75
		if(tokens[4]=="INR"):
			return (int(tokens[2])*67)/0.75
		if(tokens[4]=="Yen"):
			return (int(tokens[2])*113.41)/0.75

	if(tokens[1]=="Yen"):
		if(tokens[4]=="Dollar"):
			return int(tokens[2])/113.41
		if(tokens[4]=="Pounds"):
			return (int(tokens[2])*0.75)/113.41
		if(tokens[4]=="INR"):
			return (int(tokens[2])*67)/113.41



def main():
	host = '10.2.133.150'
	port = 65234

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))

	s.listen(5)
	message, addr = s.accept()
	print("Connection from:  " +str(addr))

	while True:
			data = message.recv(1024).decode('ASCII')
			if not data:
				break
			print("from connected user: " + str(data))
			data = conversion(data)
			print("sending: " + str(data))
			message.send(str(data).encode('ASCII')) 
	message.close()

if __name__ == '__main__':
	main()