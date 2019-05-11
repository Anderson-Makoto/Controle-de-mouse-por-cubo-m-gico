import socket
import os
import datetime

port= 8000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig= ('', port)
tcp.bind(orig)
tcp.listen(1)

print('criado')

while True:
    con, cliente= tcp.accept()
    print('Conectado por: ', cliente)

    while True:
        msg= con.recv(1024)
        msg= msg.decode()
        print(msg)

        inicio= 0
        fim= 0

        for i in range(0, len(msg)):
            if 'GET /'== msg[i:i+ 5]:
                inicio= i+ 5
            if ' HTTP'== msg[i:i+ 5]:
                fim= i

        msg= msg[inicio: fim]
        
        existe= os.path.isfile(str(msg))
        data= datetime.datetime.now()

        if existe:
            indice1= 0
            indice2= 0
            
            arquivo= open(msg, 'r')
            arquivo= arquivo.read()

            for i in range(0, len(arquivo)):    
                if '<h1>'==arquivo[i:i+4]:
                    indice1= i+4
                if '</h1>'== arquivo[i:i+5]:
                    indice2= i
            
            file= open(msg, 'r')
            texto= arquivo[indice1:indice2]
            
            http= 'HTTP /1.1 200 OK\n'
            connect= 'Connection: close\n'
            tempo= 'Date: '+str(data)+'\n'
            server= 'Server: localhost\n'
            tipo= 'Content-type: text/html\n\n'
            resposta= http+connect+tempo+server+tipo+texto        
            
            con.send(resposta.encode())

        else:
            http= 'HTTP /1.1 404 NOT FOUND\n'
            connect= 'Connection: close\n'
            tempo= 'Date: '+str(data)+'\n'
            server= 'Server: localhost\n'
            tipo= 'Content-type: text/html\n\n'
            resposta= http+connect+tempo+server+tipo
            resposta2= 'HTTP/1.1 200 OK Connection: close Date: Zaqueo98 Content-type: text/html'
            
            con.send(resposta.encode())
            
        break
    break
con.close()
