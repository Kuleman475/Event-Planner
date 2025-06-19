# Overview

I wrote an event planner that has it where you can create an event that people can rsvp to and say yes or no to and the second table has one where you can add guests and they put in information and say whether they want to come to the event or not and it will add them to the amount of people that have RSVPd to the event

I wrote this software because I have never used anything cloud based or using firestore so I thought it would be a fun way to learn how to use the firestore. 

[Event Planner Demo](https://youtu.be/-E63Xfd6Mo4)

# Cloud Database

I am using Googles firestore to store my database in.

I have 2 tables one for events and one for guests. the guests can say what event they are RSVP to and can add to the count of the guest list for that specific event.

# Development Environment

I used Google Firestore as well as VS code for the CLI.

I used python as the programming language to do my database and stored the data using firestore.

# Useful Websites

- [Firebase](https://firebase.google.com/docs/firestore/quickstart#python)
- [Firebase](https://firebase.google.com/docs/ai-logic?authuser=0#get-started)
- [Firestore](https://cloud.google.com/python/docs/reference/firestore/latest)
- [Firebase](https://firebase.google.com/docs/firestore/query-data/get-data#python_2)
- [Firebase](https://firebase.google.com/docs/firestore/manage-data/add-data#python)
- [Firebase](https://firebase.google.com/docs/firestore/query-data/queries#python)


# Future Work

- Make it where you can put multiple events under one person
- Make it be in a GUI
- break it up into 3 different files (main.py, events.py, guest-list.py)
