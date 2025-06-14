import firebase_admin
import os
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

    eventsDB = db.collection("Events")

    print("1. Create a new event")
    print("2. Read the event data")
    print("3. Update event")
    print("4. Delete event")
    eventUser = int(input("Your Choice: "))

# CREATE new Document
    if eventUser == 1:
        os.system('clear')

     # Data for new event document
        print("CREATE\n")
        eventName = input("Name of Event: ")
        print()
        eventDate = input("Date of event (MM/DD/YY): ")
        print()
        eventTime = input("What Time is the event at: ")
        print()
        eventLocation = input("Location of event: ")

     # Add data to Events database
        newEvent = {"ID": eventName, "Event": eventName, "Date": eventDate, "Time": eventTime, "Location": eventLocation}
        
        eventsDB.document(eventName).set(newEvent)

        print("Event Added")


# ID
# Event
# Date
# Time
# Location
        

# READ each Document
    elif eventUser == 2:
        print("READ")
        docs = eventsDB.get()

        for doc in docs:
            print()
            print(doc.id)
            print(doc.to_dict()["Date"])
            print(doc.to_dict()["Time"])

# UPDATE a document
    elif eventUser == 3:
        print("UPDATE")

# DELETE a document
    elif eventUser == 4:
        print("DELETE")



####### GUEST LIST #########

elif userChoice == 2:
    guestDB = db.collection("Guest List")

    docs = guestDB.get()

    # READ each Document
    for doc in docs:
        print(doc.id)