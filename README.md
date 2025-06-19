

# 🔁 Auto Chat Replier: Emily Bot (OpenAI + PyAutoGUI)

A fun and intelligent chatbot that reads chat conversations from your screen, detects if a specific user has sent a new message, and responds automatically using OpenAI's GPT-3.5 Turbo with a unique personality — **Emily**, an Indian coder who chats fluently in **Hinglish** (Hindi + English) and adds playful flavor to conversations.

---

### 👩‍💻 About Emily

> Emily is smart, sarcastic, and a coding wizard. She responds like your witty best friend who never misses a beat. She mixes Hindi and English seamlessly, analyzes the chat context, and gives replies that sound human — with a fun twist.

---

## 🚀 Features

* 🔍 **Screen-based Chat Monitoring** using `pyautogui`
* 📋 **Automatic Text Extraction** from chat window
* 🧠 **Context-Aware Responses** using OpenAI’s GPT-3.5-Turbo
* 🗣️ **Personalized Replies** in a bilingual style (Hinglish)
* 💬 **Auto Message Sending** (copy–paste–enter mechanism)

---

## 🛠️ Tech Stack

| Tool        | Purpose                              |
| ----------- | ------------------------------------ |
| Python      | Programming Language                 |
| `pyautogui` | GUI automation (clicks, drags, keys) |
| `pyperclip` | Clipboard copy/paste handling        |
| `openai`    | API for GPT-3.5 Turbo                |
| `time`      | Timing operations                    |

---

## 📸 How It Works

1. **Opens** Chrome via screen click at a known location.
2. **Selects and copies** a chat region on the screen.
3. **Checks** if the last message was from a specific sender (e.g., "Rohan Das").
4. **Feeds** the chat history to OpenAI API.
5. **Generates a natural-sounding reply** from "Emily."
6. **Pastes and sends** the message in the chat input box.

---

## 🧩 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/emily-auto-chat.git
cd emily-auto-chat
```

### 2. Install Required Libraries

Make sure Python 3.8+ is installed, then run:

```bash
pip install pyautogui pyperclip openai
```

### 3. Add Your OpenAI API Key

Replace the placeholder in the script:

```python
client = OpenAI(api_key="<Your API Key Here>")
```

### 4. Adjust Screen Coordinates

The script uses hardcoded coordinates for clicks and selections. Use:

```python
pyautogui.position()
```

...to find the correct points on your screen and update:

```python
pyautogui.click(1639, 1412)  # Chrome icon
pyautogui.moveTo(972, 202)   # Chat start
pyautogui.dragTo(2213, 1278) # Chat end
pyautogui.click(1808, 1328)  # Chat input box
```

---

## 📂 File Structure

```plaintext
📁 emily-auto-chat
├── main.py           # Main Python script
├── README.md         # Project documentation
└── requirements.txt  # List of required packages
```

---

## ⚠️ Warnings

* This script uses absolute screen coordinates — it won't work as-is on every machine.
* Be cautious when using automation on messaging apps — test in safe environments first.
* Never expose your **OpenAI API Key** publicly.

---

## ✅ To-Do (Optional Improvements)

* ⏹️ Add Stop/Start hotkeys
* 🧠 Add memory of past messages
* 🌐 Add multi-platform chat support (WhatsApp Web, Telegram Web, etc.)
* 👁️ Use OCR (like `pytesseract`) instead of manual selection

---

## 🙋‍♂️ Author

**Emily Bot** powered by OpenAI
Custom script by *Ekaagra gupta*
Inspired by real conversations and fun vibes 🎧💬

