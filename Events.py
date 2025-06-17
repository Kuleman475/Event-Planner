import firebase_admin
import os
import time
from google.cloud.firestore_v1 import FieldFilter
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/home/taylor/Downloads/eventplanner-db-firebase-adminsdk-fbsvc-76e97c9531.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
userChoice = 0

while(userChoice != 3):
    os.system('clear')
    print("Which Table to use?")
    print("1. Events")
    print("2. Guest")
    print("3. Quit")
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
            os.system('clear')
            print("READ")
            docs = eventsDB.get()

            for doc in docs:
                print()
                print("Name: ", doc.to_dict()["Event"])
                print("Date: ", doc.to_dict()["Date"])
                print("Time: ", doc.to_dict()["Time"])
                print("Location: " ,doc.to_dict()["Location"])

            print()
            input("Press enter key when done.... ")
                

    # UPDATE a document
        elif eventUser == 3:
            os.system('clear')
            print("UPDATE")
            print()
            print("Which event would you like to update?")
            print()
            docs = eventsDB.get()
            for doc in docs:
                print(doc.to_dict()["Event"])
                print()
            print()
            eventUpdate = input("Event Name: ")
            os.system('clear')
            print()
            print("Which Item would you like to update?")
            print("1. Name")
            print("2. Date")
            print("3. Time")
            print("4. Location")
            userUpdate = int(input("Your Choice: "))
            matchingDocs = eventsDB.where(filter=FieldFilter("Event", "==", eventUpdate)).get()
            doc = matchingDocs[0]
            docID = doc.id
            if userUpdate == 1:
                nameUpdate = input("Event Name: ")
                eventsDB.document(docID).update({"Event": nameUpdate, "ID": docID})
            elif userUpdate == 2:
                dateUpdate = input("New Date (MM/DD/YY): ")
                eventsDB.document(docID).update({"Date": dateUpdate, "ID": docID})
            elif userUpdate == 3:
                timeUpdate = input("Time of event: ")
                eventsDB.document(docID).update({"Time": timeUpdate, "ID": docID})
            elif userUpdate == 4:
                locationUpdate = input("Location: ")
                eventsDB.document(docID).update({"Location": locationUpdate, "ID": docID})

            print("EVENT UPDATED")

    # DELETE a document
        elif eventUser == 4:
            os.system('clear')
            print("DELETE")
            print()
            docs = eventsDB.get()
            for doc in docs:
                print(doc.id)
                print()
            print("")
            eventDelete = input("which event would you like to delete?: ")
            eventsDB.document(eventDelete).delete()

            os.system('clear')
            print("EVENT DELETED")


################## GUEST LIST #########################

    elif userChoice == 2:
        os.system('clear')
        guestDB = db.collection("Guest List")

        docs = guestDB.get()

        print("1. Create a new Guest")
        print("2. Read the Guest List")
        print("3. Update Guest")
        print("4. Delete Guest")
        guestUser = int(input("Your Choice: "))

        if guestUser == 1:
            os.system('clear')
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
            os.system('clear')
        # READ each Document
            for doc in docs:
                print(doc.id)
                print(doc.to_dict())
            time.sleep(5)
        
        elif guestUser == 3:
            os.system('clear')
            print("UPDATE")
            print()
            print("What guest do you want to update?: ")
            guestUpdate = input("")
            matchingDocs = guestDB.where(filter=FieldFilter("Name", "==", guestUpdate)).get()
            doc = matchingDocs[0]
            docID = doc.id
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
                guestDB.document(docID).update({"Name": guestName, "ID": docID})
            elif userUpdate == 2:
                guestEvent = input("Event: ")
                guestDB.document(docID).update({"EventID": guestEvent, "ID": docID})
            elif userUpdate == 3:
                guestPhone = input("Phone #: ")
                guestDB.document(docID).update({"Phone": guestPhone, "ID": docID})
            elif userUpdate == 4:
                guestEmail = input("Email: ")
                guestDB.document(docID).update({"Email": guestEmail, "ID": docID})
            elif userUpdate == 5:
                guestRSVP = input("RSVP: ")
                guestDB.document(docID).update({"RSVP": guestRSVP, "ID": docID})
            
            print("GUEST UPDATED")

        elif guestUser == 4:
            os.system('clear')
            print("DELETE")
            print()
            print("What Guest would you like to delete?: ")
            guestDelete = input("")
            guestDB.document(guestDelete).delete()

    elif userChoice == 3:
        os.system('clear')
        print("Goodbye :)")

    else:
        os.system('clear')
        print("Invalid input Try again")
    time.sleep(5)