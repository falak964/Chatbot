import requests
import json

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HEADERS = {"Authorization": "Bearer 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"}

def chatbot(prompt):
    if not prompt.strip():
        return "Please enter a valid question!"

    payload = {"inputs": prompt}  # Correct input format
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    try:
        data = response.json()  # Convert response to JSON
        print("API Response:", json.dumps(data, indent=2))  # Debugging

        if "error" in data:
            return f"Error: {data['error']}"

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        
        return "Sorry, I couldn't generate a response."

    except requests.exceptions.JSONDecodeError:
        return "Invalid response from API. Try again later."

# Running the chatbot
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break
    print("Bot:", chatbot(user_input))
