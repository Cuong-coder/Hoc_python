import requests

# Replace "YOUR_API_KEY" with your actual API Key from OpenAI
api_key = "Api"
model = "text-davinci-002"
prompt = "What is your name?"

# Define the API endpoint
url = f"https://api.openai.com/v1/engines/{model}/jobs"

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the request data
data = {
    "prompt": prompt,
    "max_tokens": 128,
    "temperature": 0.5,
}

# Send the request to the API
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Get the response data
    response_data = response.json()
    # Get the generated text
    generated_text = response_data["choices"][0]["text"]
    # Print the generated text
    print(generated_text)
else:
    # Print the error message
    print(f"Request failed with status code: {response.status_code}")
