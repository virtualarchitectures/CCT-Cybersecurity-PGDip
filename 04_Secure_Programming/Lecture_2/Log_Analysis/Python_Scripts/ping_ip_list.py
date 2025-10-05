import subprocess

def ping_ips(ip_list):
    """
    Pings a list of IP addresses.
    Args:
    ip_list (list): List of IP addresses.
    """
    for ip in ip_list:
        try:
            subprocess.check_output(['ping', '-c', '1', ip]) # '-c 1' sends one ping
            print(f"{ip} is reachable.")
        except subprocess.CalledProcessError:
            print(f"{ip} is unreachable.")
        except Exception as e:
            print(f"An error occurred while pinging {ip}: {e}")

if __name__ == '__main__':
    ping_ips(['8.8.8.8', '192.168.1.1'])