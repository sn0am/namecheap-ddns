import os
import time
import requests
import urllib.request

host = os.environ.get('host')
domain = os.environ.get('domain')
ddns_password = os.environ.get('ddns_password')
url_to_check_public_ip = os.environ.get('url_to_check_public_ip')
ddns_update_interval = int(os.environ.get('ddns_update_interval'))  # in seconds


def update_current_ip(x):
    global current_ip
    current_ip = x


current_ip = None
while True:
    try:
        print("Checking current public ip...")
        public_ip = urllib.request.urlopen(f'{url_to_check_public_ip}').read().decode('utf-8')
        time.sleep(1)
        if public_ip != current_ip:
            update_current_ip(public_ip)
            print("Attempting to update on namecheap...")
            requests.get(f"https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={ddns_password}&ip={public_ip}")
            time.sleep(1)
            print(f"Public IP has been updated to: {public_ip}")
            time.sleep(1)
        else:
            print("No need to update DDNS on namecheap, public ip has not changed.")
            time.sleep(1)
    except:
        print("An error has occurred during processing.")
    print(f'Waiting {ddns_update_interval} seconds before attempting to update again...')
    time.sleep(ddns_update_interval)
