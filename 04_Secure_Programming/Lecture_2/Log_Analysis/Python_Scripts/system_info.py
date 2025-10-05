import platform
import psutil

def display_system_info():
    """
    Displays operating system, CPU usage, and memory usage.
    """
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")

if __name__ == '__main__':
    display_system_info()