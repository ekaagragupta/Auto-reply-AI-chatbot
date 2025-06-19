from openai import OpenAI

# pip install openai
# Initialize the OpenAI client with your API key
client = OpenAI(
    api_key="<Your Key Here>",
)
# This code simulates a chat interaction where Emily responds to Rohan's messages with a casual
chat_history = '''
[20:30, 12/6/2024] Emily: kuch aisa bhejo jisse coding ke sath vibe aa jaye?
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Rohan Das: ye lo
[20:30, 12/6/2024] Rohan Das: same link again lol
[20:31, 12/6/2024] Emily: Arre this is Hindi 😅
[20:31, 12/6/2024] Emily: thoda English bhi bhej na
[20:31, 12/6/2024] Emily: lekin ruk
[20:31, 12/6/2024] Emily: yeh wala to fire nikla 🔥
[20:31, 12/6/2024] Emily: still... drop some English vibes too
[20:31, 12/6/2024] Rohan Das: chill kar, bhej raha hoon
[20:31, 12/6/2024] Emily: mujhe lagta hai mujhe pata hai kya bhejne wala hai tu 😆
[20:32, 12/6/2024] Emily: 😂😂
[20:32, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi-english mix hai but mood set ho jaayega
[20:33, 12/6/2024] Emily: okok vibe check
[20:33, 12/6/2024] Rohan Das: Haan
'''

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You are Emily — a fun, witty Indian coder who blends Hindi and English in casual chats. "
                "You're quick with comebacks, playful, and have a good taste in music. "
                "Read the chat and reply with Emily’s next message. "
                "Keep it casual, text-only, and avoid copying any existing style."
            )
        },
        {"role": "user", "content": chat_history}
    ]
)

# Output the AI-generated response
print(completion.choices[0].message.content)
# Note: Replace <Your Key Here> with your actual OpenAI API key.
# Make sure to handle your API key securely and not expose it in public code repositories.
