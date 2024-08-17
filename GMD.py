import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = "https://unsplash.com/s/photos/nature"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.findAll('img')

os.makedirs('downloaded_images', exist_ok=True)

for image in images:
        # Ensure 'alt' and 'src' are in the image tag attributes
        if 'alt' in image.attrs and 'src' in image.attrs:
            name = image['alt'].replace(" ", "_")  # Replacing spaces with underscores for filename
            link = image['src']

            # Convert relative URL to absolute if necessary
            link = urljoin(url, link)