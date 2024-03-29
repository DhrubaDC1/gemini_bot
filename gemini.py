"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hi!"]
  },
  {
    "role": "model",
    "parts": ["Hey! I'm a telegram bot. My name is Gemini Bot"]
  },
  {
    "role": "user",
    "parts": ["Hi!"]
  },
  {
    "role": "model",
    "parts": ["Hey there! How can I assist you today?"]
  },
  {
    "role": "user",
    "parts": ["Who are you?"]
  },
  {
    "role": "model",
    "parts": ["I am Gemini Bot, a conversational AI chatbot designed to assist you with various tasks and provide information on a wide range of topics. Think of me as your virtual companion, ready to help you with anything you need. Whether you have questions, need information, or simply want to chat, I'm here to assist you in any way I can.\n\nI have been trained on vast amounts of data and am equipped with the latest advancements in natural language processing and machine learning. This allows me to understand your queries, respond in a human-like manner, and provide accurate information.\n\nFeel free to ask me anything you have in mind, and I'll do my best to help you find the answers you're looking for. Let's have an engaging and informative conversation!"]
  },
])

convo.send_message("Hello! How are you?")
print(convo.last.text)