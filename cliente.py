import socket

tcp= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest= ('10.20.150.101', 8000)
tcp.connect(dest)

print('conectado')

msg= 'opa, beleza'


tcp.send(msg.encode())

#msg= tcp.recv(1024)
#msg= msg.decode()
print(msg)
tcp.close()
