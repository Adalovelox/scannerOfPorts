import socket
import threading
import concurrent.futures


host = input("Enter websitename or IP address\n")
port_start = int(input("Enter the start point range of the port numbers you would like to test for:\n"))
port_end = int(input("Enter the end of the range of the port numbers you would like to test for:\n"))
port_end+=1

# prevents everything from printing concurrently
print_lock = threading.Lock()

def scanny(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        s.close()
        with print_lock:
            print (f"{port}")
    except:
        pass

print("The following ports were open: \n\n")

#With this, use more computational resources to execute the task more quickly
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(port_start, port_end):
        executor.submit(scanny, host, port)