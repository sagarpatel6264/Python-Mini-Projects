import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((ip, port)) == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    s.close()

# scan_port("127.0.0.1", 3306) # MySQL Port
