#pip install google-genai

from google import genai
from google.genai import types
import secret
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Path to your downloaded service account key JSON file
cred = credentials.Certificate(secret.DB_JSON)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': secret.DB_URL
})
ref = db.reference('sensorData')

# Example: Writing to the database
# ref.set({
#     'temperature': 25,
#     'humidity': 60
# })

# Example: Reading from the database
data = ref.get()
print("Fetched data:", data)

Instruction = "Your name is Sonu, you are developed by Atharva Kaplay. Here is the data provided by the sensor node from the feild " + str(data)
client = genai.Client(api_key = secret.API_KEY)
history=[
    types.Content(
            role='user',
            parts=[types.Part.from_text(text=Instruction)]
        )
]
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
    print("Sonu: " , response.text)
    history.append(
        types.Content(
            role='model',
            parts=[types.Part.from_text(text=response.text)]
        )
    )