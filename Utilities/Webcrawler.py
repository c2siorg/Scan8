import os
import json
import re
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


# WebCrawler
class WebCrawler:
    def download_file(self, url, folder, proxy):
        try:
            # Check if URL is valid
            response = requests.head(url, timeout=2, proxies=proxy)
            response.raise_for_status()  # Raises an exception if the status is not 2xx

            # Create the folder if it doesn't exist
            if not os.path.exists(folder):
                os.makedirs(folder)

            # Extract the filename and extension from the URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            # Generate a unique filename with correct extension
            timestamp = str(int(time.time() * 1000))  # Use timestamp for uniqueness
            save_path = os.path.join(folder, timestamp)

            # Download the file
            with requests.get(url, stream=True, proxies=None) as response:
                response.raise_for_status()
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

            print(f"File downloaded successfully! Saved as {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    def extract_urls_from_js(self, url, proxy):
        try:
            response = requests.get(url, proxies=proxy)
            if response.status_code == 200:
                js_content = response.text
                urls = self.get_urls_from_js(js_content)
                return urls
            else:
                print(f'Error: Failed to fetch the URL ({url})')
                return []
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def get_urls_from_js(self, js_code):
        urls = re.findall(r'(?:https?:\/\/|www\.)[\w\.-]+\.[\w\.-]+[^\s\)\}\]\;\'\"]*', js_code)
        processed_urls = {url if url.startswith('http') else 'http://' + url for url in urls}
        return processed_urls

    def extract_urls(self, soup, tag, attribute, url, proxy):
        urls = set()
        for link in soup.find_all(tag):
            href = link.get(attribute)
            if href:
                urls.add(urljoin(url, href))
                if href.endswith('.js'):
                    urls.update(self.extract_urls_from_js(urljoin(url, href),proxy))
        return urls

    # Function to retrieve URLs from a web page
    def get_urls(self, url, proxy):
        headers = {'User-Agent': 'Mozilla/5.0'}  # Add user agent header

        with requests.Session() as session:
            try:
                response = session.get(url, headers=headers, proxies=proxy)
                response.raise_for_status()
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                urls = set()

                # Extract URLs from <> tags
                for attribute in ['href', 'src']:
                    for tag in ['a', 'link', 'img', 'area', 'base', 'script', 'iframe', 'form', 'button', 'input']:
                        urls.update(self.extract_urls(soup, tag, attribute, url, proxy))

                return urls

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                return []



    
