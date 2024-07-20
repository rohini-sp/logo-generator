import requests
import os
import streamlit as st

# Using Stable image ultra api
API_ENDPOINT = "https://api.stability.ai/v2beta/stable-image/generate/ultra"
API_KEY = "sk-1QazoEQp6X7MFf2Iug4sU9Y4Kwdcsnj49fUPKs9oLFqIfxgL"   # Replace with your Stable Diffusion API key
OUTPUT_FOLDER = "./generated_logos"  # Folder to save generated logos

def generate_logos(prompt, num_variations):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/*"  # Specify that we accept JSON responses
    }

    # Convert the data dictionary into a multipart/form-data request
    files = {
        "prompt": (None, prompt),
        "num_variations": (None, str(num_variations))
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, files=files)
        if response.status_code == 200:
            return response.json()  # Return the response JSON for further processing
        else:
            st.error(f"Error: {response.status_code} - {response.json()}")
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"Request Error: {e}")
        return None

def save_logos(logos_data):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    saved_logos = []
    for idx, logo in enumerate(logos_data['logos']):
        filename = f"logo_{idx + 1}.png"  # Adjust extension based on API response format
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        with open(filepath, 'wb') as file:
            file.write(requests.get(logo['url']).content)
        saved_logos.append(filepath)
    return saved_logos

def main():
    st.title("Logo Generator using Stable Diffusion API")

    project_name = st.text_input("Enter project name:")
    logo_description = st.text_input("Enter logo description:")
    logo_style = st.text_input("Enter logo style:")
    num_variations = st.number_input("Enter number of logo variations:", min_value=1, max_value=10, step=1)

    if st.button("Generate Logos"):
        prompt = f"{project_name}, {logo_description}, {logo_style}"
        with st.spinner("Generating logos..."):
            logos_data = generate_logos(prompt, num_variations)
            if logos_data:
                saved_logos = save_logos(logos_data)
                st.success("Logos generated successfully!")
                for logo_path in saved_logos:
                    st.image(logo_path, caption=os.path.basename(logo_path))

if __name__ == "__main__":
    main()
