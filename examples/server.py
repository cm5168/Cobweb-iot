from cobwebiot import server
'''
import Queue
add_q = Queue.Queue()
msg_q = Queue.Queue()

def update_queue(address,data):
	add_q.put(address)
	msg_q.put(data)
'''

temp_server = server.http_server("localhost",9999)
# temp_server = server.http_server("localhost",9999,update_queue)
temp_server.serve_forever()