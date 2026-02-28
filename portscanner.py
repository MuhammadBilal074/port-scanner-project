import socket
target = input ("Enter target IP: ")

print("Scanning target :" , target)
print("please wait" )

for port in range (1, 1025):

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 socket.setdefaulttimeout(1)

 result = s.connect_ex((target, port))

 if result == 0:
  print("Port", port, "is OPEN")
 s.close()
print("Scan Completed")
