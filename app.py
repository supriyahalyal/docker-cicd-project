import requests
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Endpoints that return 200, 404, and 400 status codes
urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/400",
    "https://httpbin.org/status/201",
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        
        # Diagnostic tracker to reveal the real status code
        print(f"DEBUG: {url} actually returned code -> {response.status_code}")
        
        # Strict checking logic
        if response.status_code == 200:
            print(f"{Fore.GREEN}[SUCCESS] {url} is online.\n")
            
        elif response.status_code == 404:
            print(f"{Fore.RED}[ERROR] {url} page not found.\n")
            
        else:
            print(f"{Fore.YELLOW}[WARNING] {url} failed with code {response.status_code}.\n")
            
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[CRITICAL] Failed to connect to server: {e}\n")
