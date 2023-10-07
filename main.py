'''
This is the main file for the Google Chrome extension.
'''
import json
import requests
import keyboard
from tkinter import messagebox
from tkinter import Tk
# Function to send a request to the OpenAI Chat GPT API
def send_request(prompt):
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    api_key = 'YOUR_API_KEY'
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['text']
# Function to handle the key binding event
def handle_key_binding(event):
    if event.name == 'n' and keyboard.is_pressed('alt'):
        # Get the active text field on the website
        root = Tk()
        root.withdraw()
        active_element = root.clipboard_get()
        root.destroy()
        # Generate a prompt for the Chat GPT
        prompt = f'User: {active_element}\nAI: '
        # Send the prompt to the Chat GPT API
        response = send_request(prompt)
        # Display the AI response
        messagebox.showinfo('AI Response', response)
# Register the key binding event
keyboard.on_press(handle_key_binding)
# Start the main event loop
keyboard.wait()