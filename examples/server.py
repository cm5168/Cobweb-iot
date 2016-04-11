from cobwebiot import server

temp_server = server.http_server("localhost",9999)
temp_server.serve_forever()