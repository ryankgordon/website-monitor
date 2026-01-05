import requests
import time
from datetime import datetime
CHECK_INTERVAL = 30  # seconds
def check_website(url):
   """Check if a website is up and measure response time."""
   try:
       start = time.time()
       response = requests.get(url, timeout=5)
       elapsed = (time.time() - start) * 1000
       print(f"{datetime.now()} | {url} | UP | Status: {response.status_code} | Time: {int(elapsed)}ms")
   except requests.exceptions.RequestException:
       print(f"{datetime.now()} | {url} | DOWN")
def monitor(url):
   """Run the monitoring loop for a single website."""
   try:
       while True:
           check_website(url)
           time.sleep(CHECK_INTERVAL)
   except KeyboardInterrupt:
       print("\nMonitoring stopped by user")
if __name__ == "__main__":
   website_url = "https://github.com"  # Change this to any site you want
   monitor(website_url)
