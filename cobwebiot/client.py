import socket
import sys

def send(HOST,PORT,MESSAGE):
	data = MESSAGE

	# Create a socket (SOCK_STREAM means a TCP socket)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		# Connect to server and send data
		sock.connect((HOST, PORT))
		if sys.version_info.major == 2:
			sock.sendall(data + "\n")

			# Receive data from the server and shut down
			received = sock.recv(1024)
		else:
			# Connect to server and send data
			sock.sendall(bytes(data + "\n", "utf-8"))

			# Receive data from the server and shut down
			received = str(sock.recv(1024), "utf-8")
	finally:
		sock.close()

	print("Sent:     {}".format(data))
	print("Received: {}".format(received))