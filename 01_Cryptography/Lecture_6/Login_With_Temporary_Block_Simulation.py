import time

# Simulated database of users
USERS = {"admin": "admin123", "user1": "password123"}

# Dictionary to track failed attempts and block time
block_list = {}

# Duration to block in seconds
BLOCK_DURATION = 5

# Simulated IP (in a real scenario, you'd fetch this from a request)
ip_address = "192.168.0.1"


def login(username, password):
    current_time = time.time()

    # Check if IP is blocked
    if ip_address in block_list:
        block_time = block_list[ip_address]
        if current_time < block_time:
            print(f"⛔ Access denied. IP {ip_address} is blocked. Try again later.")
            return False
        else:
            del block_list[ip_address]  # unblock after time expires

    # Verify credentials
    if username in USERS and USERS[username] == password:
        print(f"✅ Login successful! Welcome, {username}")
        return True
    else:
        print("❌ Login failed!")
        block_list[ip_address] = current_time + BLOCK_DURATION
        print(f"🔒 IP {ip_address} temporarily blocked for {BLOCK_DURATION} seconds.")
        return False


# Simulate login attempts
# Wrong attempt
login("user1", "wrongpassword")

# Try again immediately
login("user1", "password123")

# Wait for 6 seconds and try again
time.sleep(6)
login("user1", "password123")
