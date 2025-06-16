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


####################  EVENTS  #############################
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
        print()
        print("Which event would you like to update?")
        docs = eventsDB.get()
        for doc in docs:
            print(doc.id)
        eventUpdate = input("Event Name: ")
        print()
        print("Which Item would you like to update?")
        print("1. Name")
        print("2. Date")
        print("3. Time")
        print("4. Location")
        userUpdate = int(input("Your Choice: "))
        if userUpdate == 1:
            print("Events")
            nameUpdate = input("Event Name: ")
            eventsDB.document(eventUpdate).update({"Event": nameUpdate, "ID": nameUpdate})

# DELETE a document
    elif eventUser == 4:
        print("DELETE")
        print()
        print("which event would you like to delete?: ")
        eventDelete = input("")
        eventsDB.document(eventDelete).delete()

################## GUEST LIST #########################

elif userChoice == 2:
    guestDB = db.collection("Guest List")

    docs = guestDB.get()

    print("1. Create a new Guest")
    print("2. Read the Guest List")
    print("3. Update Guest")
    print("4. Delete Guest")
    guestUser = int(input("Your Choice: "))

    if guestUser == 1:
    # CREATE a new Document

        # New Guest
        print()
        guestName = input("Guest Name: ")
        print()
        guestPhone = input("Phone #: ")
        print()
        guestEmail = input("Email Address: ")
        print()
        guestEvent = input("Event: ")
        print()
        guestRSVP = input("RSVP for Event (Yes/No): ")

        #Add to Database
        newGuest={"ID": guestName, "Name": guestName, "Phone": guestPhone, "Email": guestEmail, "EventID": guestEvent, "RSVP": guestRSVP}
        guestDB.document(guestName).set(newGuest)

        print()
        print("GUEST ADDED")

    elif guestUser == 2:
    # READ each Document
        for doc in docs:
            print(doc.id)
    
    elif guestUser == 3:
        print("UPDATE")
        print()
        print("What guest do you want to update?: ")
        guestUpdate = input("")

        print()
        print("Which Item would you like to update?")
        print("1. Name")
        print("2. Event")
        print("3. Phone")
        print("4. Email")
        print("5. RSVP")
        userUpdate = int(input("Your Choice: "))
        if userUpdate == 1:
            guestName = input("Name: ")
            guestDB.document(guestUpdate).update({"Name": guestName, "ID": guestUpdate})
        elif userUpdate == 2:
            guestEvent = input("Event: ")
            guestDB.document(guestUpdate).update({"EventID": guestEvent, "ID": guestUpdate})
        elif userUpdate == 3:
            guestPhone = input("Phone #: ")
            guestDB.document(guestUpdate).update({"Phone": guestPhone, "ID": guestUpdate})
        elif userUpdate == 4:
            guestEmail = input("Email: ")
            guestDB.document(guestUpdate).update({"Email": guestEmail, "ID": guestUpdate})
        elif userUpdate == 5:
            guestRSVP = input("RSVP: ")
            guestDB.document(guestUpdate).update({"RSVP": guestRSVP, "ID": guestUpdate})

    elif guestUser == 4:
        print("DELETE")