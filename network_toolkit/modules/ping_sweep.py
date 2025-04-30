import ipaddress
import platform
import subprocess

def ping_host(ip):
    command = ['ping', '-n' if platform.system().lower()=='windows' else '-c', '1', str(ip)]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def sweep(network):
    print(f"\n🔍 Ping sweeping {network}")
    net = ipaddress.ip_network(network, strict=False)
    for ip in net.hosts():
        if ping_host(ip):
            print(f"[+] Host Up: {ip}")
