import re
def extract_ips(log_file, output_file):
    """
    Extracts IP addresses from a log file using regular expressions.
    Args:
    log_file (str): Path to the log file.
    output_file (str): Path to the output file.
    """
    try:
        with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
            ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b' # Regex for IPv4
            for line in infile:
                ips = re.findall(ip_regex, line)
                for ip in ips:
                    outfile.write(ip + '\n')
        print(f"IP addresses extracted to {output_file}")
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    extract_ips('logfile.txt', 'extracted_ips.txt')
