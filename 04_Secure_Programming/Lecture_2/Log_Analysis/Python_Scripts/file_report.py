import os
import datetime

def generate_file_report(directory):
    """
    Generates a report of file sizes and creation dates for a directory.
    Args:
    directory (str): Path to the directory.
    """
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_size = os.path.getsize(filepath)
                creation_time = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
                print(f"File: {filename}, Size: {file_size} bytes, Creation: {creation_time}")
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    generate_file_report('.') # Current directory