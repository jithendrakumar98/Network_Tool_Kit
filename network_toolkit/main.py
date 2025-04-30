from modules import ping_sweep, port_scanner, dns_lookup, traceroute, whois_lookup

def menu():
    print("\n🔧 Network Toolkit")
    print("1. Ping Sweep")
    print("2. Port Scan + Banner Grab")
    print("3. DNS Lookup")
    print("4. Traceroute")
    print("5. Whois Lookup")
    print("0. Exit")

while True:
    menu()
    choice = input("Select: ")
    if choice == '1':
        net = input("Enter CIDR (e.g. 192.168.1.0/24): ")
        ping_sweep.sweep(net)
    elif choice == '2':
        ip = input("Enter IP: ")
        port_scanner.scan_ports(ip)
    elif choice == '3':
        domain = input("Enter domain: ")
        dns_lookup.lookup(domain)
    elif choice == '4':
        host = input("Enter host: ")
        traceroute.trace(host)
    elif choice == '5':
        domain = input("Enter domain: ")
        whois_lookup.whois_lookup(domain)
    elif choice == '0':
        break
    else:
        print("❌ Invalid option.")
