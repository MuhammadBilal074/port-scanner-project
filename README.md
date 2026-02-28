target = input("Enter target IP: ")

print("Scanning target:", target)
print("Please wait...")

for port in range(1, 1025):
    
    # Create a connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    # Try to connect
    result = s.connect_ex((target, port))
    
    # If result is 0, port is open
    if result == 0:
        print("Port", port, "is OPEN")
    
    # Close connection
    s.close()

print("Scan Complete!")
