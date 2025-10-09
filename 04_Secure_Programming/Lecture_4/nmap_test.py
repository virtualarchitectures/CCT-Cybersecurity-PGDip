import nmap

def scan_host(target='127.0.0.1', ports='22-443'):
    nm = nmap.PortScanner()
    try:
        nm.scan(target, ports)
    except nmap.PortScannerError as e:
        print("nmap error:", e)
        return
    except Exception as e:
        print("unexpected error:", e)
        return

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"Host state: {nm[host].state()}")
        # all_protocols() returns a list like ['tcp']
        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            ports_list = sorted(nm[host][proto].keys())
            if not ports_list:
                print("  (no ports found for this protocol)")
                continue
            for port in ports_list:
                state = nm[host][proto][port]['state']   # <-- note the quotes
                print(f"  port {port}\tstate: {state}")
        print("-" * 40)

if __name__ == "__main__":
    scan_host('127.0.0.1', '22-443')
