import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/v1/chat/completions"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def get_response(user_input):
    if not API_KEY:
        return "API key not found!"

    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 500
    }

    try:
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=data)

        if response.ok:
            response_data = response.json()

            print("\nAPI Response Debug:")
            print(response_data)

            if "choices" in response_data and len(response_data["choices"]) > 0:
                generated_text = response_data["choices"][0].get("message", {}).get("content", "")

                cleaned_text = " ".join(generated_text.splitlines())

                return cleaned_text

            return "No response was received in the API call."

        return f"Error in API call: {response.status_code} - {response.text}"

    except requests.RequestException as e:
        return f"Error in API call: {e}"

