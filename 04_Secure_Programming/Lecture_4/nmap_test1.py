import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '0-1000')

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        ports = sorted(nm[host][proto].keys())
        for port in ports:
            print(f"Host: {host}, Port: {port}, State: {nm[host][proto][port]['state']}")
