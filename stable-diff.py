

import requests
import os

API_ENDPOINT = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
API_KEY = "sk-API_KEY"  

def generate_logo(prompt, output_format='webp', output_filename='logo'):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/*" 
    }

    data = {
        "prompt": prompt,
        "output_format": output_format,
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, files={"none": ''}, data=data)
        if response.status_code == 200:
            output_filename_with_ext = f"{output_filename}.{output_format}"
            with open(output_filename_with_ext, 'wb') as file:
                file.write(response.content)
            print(f"Logo generated and saved as: {output_filename_with_ext}")
        else:
            print(f"Error: {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

def main():
    prompt = input("Enter a prompt for the logo generation: ")
    output_format = input("Enter output format (e.g., webp, png, jpg): ").strip().lower()
    output_filename = input("Enter output filename (without extension): ").strip()

    if output_format not in ['webp', 'png', 'jpg']:
        print("Unsupported output format. Please use webp, png, or jpg.")
        return

    generate_logo(prompt, output_format=output_format, output_filename=output_filename)

if __name__ == "__main__":
    main()

