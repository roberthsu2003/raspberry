
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("raspberrytest-51322-firebase-adminsdk-qdsvd-6ec84a9325.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrytest-51322-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/mfrc')
ref.update({
    'id': 'Hello! Raspberry!'
})



