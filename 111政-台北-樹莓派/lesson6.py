
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("raspberrytest-51322-firebase-adminsdk-qdsvd-6ec84a9325.json")
firebase_admin.initialize_app(cred)
