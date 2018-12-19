import socket
def conversion(data):
	tokens = data.split()
	if(tokens[1]=="INR"):
		if(tokens[4]=="Dollar"):
			return int(tokens[2])/67
		if(tokens[4]=="Pounds"):
			return (int(tokens[2])*0.75)/67
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
	host = '10.10.9.34'
	port = 65431
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	print("Server Started: ")
	while True:
		data, addr = s.recvfrom(1024)
		print("messgae from: " + str(data))
		print("from connect user:" + str(data))
		data = conversion(data.decode('ASCII'))
		print("sending: " + str(data))
		s.sendto(str(data).encode('ASCII'),addr)
	s.close()
if __name__ == '__main__':
	main()