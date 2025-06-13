import firebase_admin

from firebase_admin import credentials, firestore


cred = credentials.Certificate("/home/taylor/Downloads/eventplanner-db-firebase-adminsdk-fbsvc-76e97c9531.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

print("Which Table to use?")
print("1. Events")
print("2. Guest")
userChoice = int(input("Your Choice: "))


####### EVENTS  ############
if userChoice == 1:
    events_ref = db.collection("Events")

    docs = events_ref.get()

    # READ each Document
    for doc in docs:
        print()
        print(doc.id)
        print(doc.to_dict()["Date"])
        print(doc.to_dict()["Time"])




####### GUEST LIST #########

elif userChoice == 2:
    events_ref = db.collection("Guest List")

    docs = events_ref.get()

    # READ each Document
    for doc in docs:
        print(doc.id)