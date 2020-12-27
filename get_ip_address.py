# GET IP ADDRESS FROM ANY WEBSITE WITH PYTHON
# Made with ❤️ in Python 3 by Alvison Hunter - December 26th, 2020
# Website: https://alvisonhunter.com/

import socket as s
host_list = ['tutorialspoint.com','python.org','py4e.com','diveintopython3.net']
def get_ip_address(hosts):
    for h in hosts:
        print(f"IP Address of {h} is {s.gethostbyname(h)}")

# Let us test this baby now....
get_ip_address(host_list)
