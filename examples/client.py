from cobwebiot import client

while 1:
	a = input('Enter Message:')
	client.send('localhost',9999,a)