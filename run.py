import platform
import subprocess

def ping_website(website):
    # Determine the current operating system
    system = platform.system().lower()

    # Set the appropriate ping command based on the operating system
    if system == 'windows':
        command = ["ping", website, "-n", "4"]
    else:
        command = ["ping", website, "-c", "4"]

    try:
        # Use the 'ping' command to ping the website
        output = subprocess.run(command, capture_output=True, text=True)
        
        # Check if the ping was successful
        if output.returncode == 0:
            print(f"Ping to {website} was successful!")
            print(output.stdout)
        else:
            print(f"Ping to {website} failed.")
            print(output.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Ping bing.com
ping_website("bing.com")
