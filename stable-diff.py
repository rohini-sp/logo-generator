# ***import requests
# import json

# # Replace with your Stability API endpoint and API key
# API_ENDPOINT = 'https://api.stability.io/logo/generate'
# API_KEY = 'sk-SNIqKMx7GiyNuj92y82aBUwZhRFL39fwUslEcLV2kDROT9Pe'

# def generate_logo(business_name, colors):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {API_KEY}'
#     }

#     # Example payload structure (adjust as per Stability API documentation)
#     payload = {
#         'business_name': business_name,
#         'colors': colors
#     }

#     try:
#         response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))
#         if response.status_code == 200:
#             return response.json()  # Assuming API returns JSON with logo data
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f"Request Error: {e}")
#         return None

# def main():
#     business_name = input("Enter your business name: ")
#     colors = input("Enter preferred colors (comma-separated): ").split(',')

#     # Generate logo
#     logo_data = generate_logo(business_name, colors)
    
#     if logo_data:
#         print("Generated logos:")
#         for idx, logo in enumerate(logo_data['logos']):
#             print(f"{idx + 1}. {logo['name']} - {logo['url']}")  # Adjust based on API response structure

#         # Example: Allow user to select a logo or download functionality
#         selected_logo = int(input("Select a logo number to download: "))
#         if 1 <= selected_logo <= len(logo_data['logos']):
#             # Example: Download functionality
#             download_url = logo_data['logos'][selected_logo - 1]['url']
#             print(f"Downloading logo from: {download_url}")
#             # Implement your download logic here

# if __name__ == "__main__":
#     main()***


# import requests

# response = requests.post(
#     f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
#     headers={
#         "authorization": f"Bearer sk-SNIqKMx7GiyNuj92y82aBUwZhRFL39fwUslEcLV2kDROT9Pe",
#         "accept": "image/*"
#     },
#     files={"none": ''},
#     data={
#         "prompt": "Lighthouse on a cliff overlooking the ocean",
#         "output_format": "webp",
#     },
# )

# if response.status_code == 200:
#     with open("./lighthouse.webp", 'wb') as file:
#         file.write(response.content)
# else:
#     raise Exception(str(response.json()))


import requests
import os

API_ENDPOINT = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
API_KEY = "sk-1QazoEQp6X7MFf2Iug4sU9Y4Kwdcsnj49fUPKs9oLFqIfxgL"  

def generate_logo(prompt, output_format='webp', output_filename='logo'):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/*"  # Update to accept any image format
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

