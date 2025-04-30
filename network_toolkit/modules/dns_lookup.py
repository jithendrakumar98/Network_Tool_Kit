import socket

def lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"🌐 {domain} resolves to {ip}")
        print(f"🔄 Reverse lookup: {socket.gethostbyaddr(ip)[0]}")
    except Exception as e:
        print("❌ DNS Error:", e)
