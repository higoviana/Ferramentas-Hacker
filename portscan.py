import socket

ports = [21,22,80,443,445,3306,25]

for port in ports:

         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
         client.settimeout(0.1)
         code = client.connect_ex(("127.0.0.1", port))
         if code ==0:
                  print(port, "porta aberta")
         else:
                  print(port, "porta fechada")
