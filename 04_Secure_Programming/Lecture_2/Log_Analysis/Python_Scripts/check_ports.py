import socket

def check_open_ports(host, ports):
    """
    Checks if specified ports are open on a host.
    Args:
    host (str): Hostname or IP address.
    ports (list): List of ports to check.
    """
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=1):
                print(f"Port {port} is open on {host}")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Port {port} is closed on {host}")
        except Exception as e:
            print(f"An error occurred while checking port {port}: {e}")

if __name__ == '__main__':
    check_open_ports('127.0.0.1', [80, 443, 22])
