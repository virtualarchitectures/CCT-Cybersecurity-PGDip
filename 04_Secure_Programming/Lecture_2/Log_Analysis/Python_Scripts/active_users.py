import subprocess

def display_logged_in_users():
    """
    Displays logged-in users using the 'who' command.
    """
    try:
        output = subprocess.check_output(['who']).decode('utf-8')
        print(output)
    except FileNotFoundError:
        print("The 'who' command is not available on this system.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    display_logged_in_users()
