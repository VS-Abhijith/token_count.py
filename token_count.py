import httpx

# Define the API endpoint and dummy API key
url = "https://api.openai.com/v1/chat/completions"
api_key = "dummy_api_key"

# Define the messages to be sent in the request
messages = [
    {"role": "user", "content": "List only the valid English words from these: y5W1djP1, eQ0GWWg, rhVr, ffXzPDs, zTkSH8Sb, JaKjT5"}
]

# Define the JSON payload for the POST request
payload = {
    "model": "gpt-4o-mini",
    "messages": messages
}

# Send the POST request to OpenAI's API
response = httpx.post(url, json=payload, headers={"Authorization": f"Bearer {api_key}"})
response.raise_for_status()  # Ensure the request was successful

# Parse and print the number of tokens used
result = response.json()
num_tokens = result['usage']['total_tokens']
print(f"Number of tokens: {num_tokens}")
