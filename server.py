import socket

PORT = 1337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen(5)
print "Listening on Port", PORT 

while True:
    server.listen(5)
    connection, address = server.accept()
    data = "Hello, World"
    connection.sendall(data)
    print "Got a request!"
    connection.close()

