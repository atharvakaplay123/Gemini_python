import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import secret

# Path to your downloaded service account key JSON file
cred = credentials.Certificate(secret.DB_JSON)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': secret.DB_URL
})

# Example: Writing to the database
sensor = db.reference('sensorData')
temperature = db.reference('sensorData/temperature')
humidity = db.reference('sensorData/humidity')
sensor.set({
    'temperature': 25,
    'humidity': 60
})

# Example: Reading from the database
data = sensor.get()
print("data: ",data)
print("temp data:", temperature.get())
print("humidity data:", humidity.get())
print("str", str(data))
