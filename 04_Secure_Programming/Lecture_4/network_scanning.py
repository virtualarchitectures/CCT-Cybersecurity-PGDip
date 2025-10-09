import socket

def port_scan(target_ip, port):
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    try:
        print(f"Port {port} is open")
        sock.close()
    except:
        pass

target_ip =input("Enter IP address : \n") # local IP address 127.0.0.1
for port in range(1, 65535):
    port_scan(target_ip, port)

    if port == 10:
        break;