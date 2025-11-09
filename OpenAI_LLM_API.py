**3.1. Accessing OpenAI LLMs via API in Python**
!pip install -q -U openai
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-2025-04-14",
    input="Tell me a three sentence bedtime story about a unicorn"
)

# print(response)
print(response.output[0].content[0].text)
response
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-3.5-turbo",
  input="Why sky is blue?"
)

# print(response)
print(response.output[0].content[0].text)
**Chat Completion**
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful chat assistant."},
        {"role": "user", "content": "What is Machine Learning?"}
    ]
)

print(completion.choices[0].message.content)
from openai import OpenAI
client = OpenAI()

# maintain chat history in a list
chat_history = [
    {"role": "system", "content": "You are a helpful chat assistant."},
    {"role": "user", "content": "What is Machine Learning?"},
    {"role": "assistant", "content": "Machine Learning is a field of AI where systems learn patterns from data and improve without explicit programming."},
    {"role": "user", "content": "Can you give me some examples?"}
]

# send the full history to the API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=chat_history
)

response = completion.choices[0].message.content
print(response)

# add the assistant's reply back into history for next round
chat_history.append({"role": "assistant", "content": response})
chat_history
