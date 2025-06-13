# EVENTS CRUD
import firebase_admin

from firebase_admin import credentials, firestore


cred = credentials.Certificate("/home/taylor/Downloads/eventplanner-db-firebase-adminsdk-fbsvc-76e97c9531.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

# 3. Reference a collection (e.g., 'events')
events_ref = db.collection("Events")

# 4. Read all documents in that collection
docs = events_ref.get()

# 5. Print each document
for doc in docs:
    print()
    print(doc.id)
    print(f"{doc.to_dict()}")

print("PPPPPPPPPPP")