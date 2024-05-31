import requests
import re
import os
from bs4 import BeautifulSoup

try:
    response = requests.get('https://www.xenserver.com/downloads')
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else Happened",err)
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'Software Development Kit \(SDK\) (\d+\.\d+\.\d+)')

for text in soup.stripped_strings:
    match = pattern.search(text)
    if match:
        version = match.group(1)
        sdk_url = f'https://downloads.xenserver.com/sdk/{version}/XenServer-SDK-{version}.zip'
        print(f"::set-output name=XENSERVER_SDK_URL::{sdk_url}")
        break