import socket

def scan_ports(ip, ports=[21,22,23,25,53,80,110,443]):
    open_ports = []
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, port))
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No Banner"
            print(f"[+] {ip}:{port} OPEN - {banner}")
            open_ports.append((port, banner))
            s.close()
        except:
            continue
    return open_ports
