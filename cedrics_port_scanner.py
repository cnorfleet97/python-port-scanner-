import socket
from datetime import datetime

text_file = open("Ceds Port Scanner.txt", "w")
text_file.write("Welcome join the scan \n\n")

server = input("enter target to scan: ")
ip = socket.gethostbyname(server)

print(server)
print(ip)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.settimeout(5)
t1 = datetime.now()
#a = s.connect_ex((ip,443))

text_file.write("Current datetime :" + str(t1) + "\n\n")
def scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
#if a == 0:
for x in range(1026):
    if scan(x):
      print("Port",x ,"is open!!!!!!!")

    else:
     print("Port" , x,"isnt available")
text_file.write("Port {} is open \n\n".format(x))

t2 = datetime.now()

text_file.write("Ending datetime :" + str(t2) + "\n\n")
print("Ending datetime :" +str(t2) + "\n\n")
total = t2 - t1

print("Scan completed in: ", total)

text_file.write('This is the end of the scan')
text_file.close()
#a_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#location = ("192.0.2.1", 443)
#result_of_check = a_socket.connect_ex(location)


#if result_of_check == 0:
 #   print("Port is open")
#else:
 #   print("Port is closed")

#a_socket.close()

