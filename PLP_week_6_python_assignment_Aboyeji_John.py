import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    print(" Ubuntu Image Fetcher: 'I am because we are'")
    
    # Prompt user for image URL
    url = input("Please enter the URL of the image you want to fetch: ").strip()
    
    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        # Fetch image from the web
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if HTTP request failed
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename found, generate one
        if not filename:
            filename = f"ubuntu_image_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        
        # Full path to save file
        filepath = os.path.join(save_dir, filename)
        
        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)
        
        print(f" Image successfully saved as: {filepath}")
    
    except requests.exceptions.RequestException as e:
        print(" Respectfully, we couldn’t fetch the image:")
        print(f"   Reason: {e}")

if __name__ == "__main__":
    fetch_image()
