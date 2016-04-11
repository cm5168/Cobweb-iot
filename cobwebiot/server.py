import sys

if sys.version_info.major == 2:
	import SocketServer as ss
else:
	import socketserver as ss



def http_server(HOST,PORT,FUNC=0):

	class SERVER(ss.BaseRequestHandler):
		def handle(self):
			# self.request is the TCP socket connected to the client
			self.data = self.request.recv(1024).strip()
			print("{} sent:".format(self.client_address[0]))
			print(self.data)
			if FUNC:
				FUNC("{}".format(self.client_address[0]),self.data)
			# just send back the same data, but upper-cased
			self.request.sendall(self.data.upper())

	server = ss.TCPServer((HOST,PORT),SERVER)
	return server

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = ss.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
