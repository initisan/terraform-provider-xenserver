import requests
import re
import os
from bs4 import BeautifulSoup

response = requests.get('https://www.xenserver.com/downloads')
soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'Software Development Kit \(SDK\) (\d+\.\d+\.\d+)')

for text in soup.stripped_strings:
    match = pattern.search(text)
    if match:
        version = match.group(1)
        sdk_url = f'https://downloads.xenserver.com/sdk/{version}/XenServer-SDK-{version}.zip'
        os.env.GITHUB_OUTPUT = f'XENSERVER_SDK_URL={sdk_url}'