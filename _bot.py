import pyautogui
import time
import pyperclip
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key="<Your API Key Here>")

# Function to check if the last message is from the target sender
def is_last_message_from(chat_log: str, sender: str = "Rohan Das") -> bool:
    latest_chunk = chat_log.strip().split("/2024] ")[-1]
    return sender in latest_chunk

# Open Chrome (assumes Chrome icon is at specific location on screen)
pyautogui.click(1639, 1412)
time.sleep(1)

while True:
    time.sleep(5)

    # Select and copy the chat area
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')  # Simulates drag to highlight
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1994, 281)  # Click away to ensure copy completes

    # Get chat text from clipboard
    chat_content = pyperclip.paste()
    print(chat_content)

    if is_last_message_from(chat_content):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are emily, a bilingual coder from India who roasts people in a funny way. Your replies should be entertaining, not formatted like chat logs."},
                {"role": "user", "content": chat_content}
            ]
        ).choices[0].message.content

        # Copy AI's reply to clipboard
        pyperclip.copy(response)

        # Paste the reply in the chat box
        pyautogui.click(1808, 1328)  # Click on the message input area
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')  # Send the message
