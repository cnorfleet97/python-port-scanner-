import socket
import datetime

text_file = open("Ced's Port Scanner.txt", "w")
text_file.write("Welcome join the scan \n\n")

server = input("enter target to scan: ")
ip = socket.gethostbyname(server)

print(server)
print(ip)

t1 = datetime.datetime.now()
text_file.write("Current datetime :" + str(t1) + "\n\n")


def scan(targetip):
    x = 1
    for x in range(1, 1026):

        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.settimeout(.25)
        a = s.connect_ex((targetip, x))
        print(a)
        if a == 0:
            print("Port " + str(x) + " is open!!!!!!!")
            text_file.write("Port {} is open \n\n".format(x))

        else:
            print("Port " + str(x) + " isn't available")
    x += 1


scan(ip)

t2 = datetime.datetime.now()

text_file.write("Ending datetime :" + str(t2) + "\n\n")
print("Ending datetime :" + str(t2) + "\n\n")
total = t2 - t1

print("Scan completed in: ", total)
text_file.write("Scan completed in: " + str(total))
text_file.close()

