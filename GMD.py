import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Example URL (You can replace this with the website by choice)
url = "https://unsplash.com/s/photos/nature"

# Sending a request to the website
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Finding all image tags
images = soup.findAll('img')

# Directory to save images
os.makedirs('downloaded_images', exist_ok=True)

# Looping through all found images
for image in images:
    try:
        # Ensure 'alt' and 'src' are in the image tag attributes
        if 'alt' in image.attrs and 'src' in image.attrs:
            name = image['alt'].replace(" ", "_")  # Replacing spaces with underscores for filename
            link = image['src']

            # Convert relative URL to absolute if necessary
            link = urljoin(url, link)

            # Extract the file extension from the URL
            ext = link.split('.')[-1]

            # Ensure the extension is valid (e.g., jpg, png, etc.)
            if ext.lower() not in ['jpg', 'jpeg', 'png', 'gif']:
                ext = 'jpg'  # Default to jpg if no valid extension found

            # Downloading and saving the image
            with open(os.path.join('downloaded_images', name + f'.{ext}'), 'wb') as f:
                im = requests.get(link)
                f.write(im.content)

            print(f"Downloaded {name}.{ext}")

    except Exception as e:
        print(f"Failed to download {name}: {e}")

print("Download complete.")
