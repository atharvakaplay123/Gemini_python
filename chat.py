#pip install google-genai

from google import genai
from google.genai import types
from secret import API_KEY

client = genai.Client(api_key = API_KEY)
history=[]
while True:
    you = input("\nYou: ")
    history.append(
        types.Content(
            role='user',
            parts=[types.Part.from_text(text=you)]
        )
    )
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=history
    )
    print("Ai: " , response.text)
    history.append(
        types.Content(
            role='model',
            parts=[types.Part.from_text(text=response.text)]
        )
    )