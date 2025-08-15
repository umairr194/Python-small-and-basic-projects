import random

subjects = [  
    "imran khan",
    "nawaz shareef chor",
    "maryam nawaz chor",
    "virat kholi",
    "prime minster imran khan",
    "auto driver in lahore",
    "cat eat "
]

actions = [ 
    "order",
    "celebration",
    "love imran khan",
    "cancel",
    "launches",
    "eat",
    "dance with"
]

places_or_things = [ 
    "in lahore",
    "in local area of pakistan",
    "a plate of samosa",
    "fight in lahore",
    "at parliment",
    "at local bus stand",
    "during PSL match"
]

while True:
    selected_subject = random.choice(subjects)
    selected_action = random.choice(actions)  
    selected_place = random.choice(places_or_things)  

    headline = f"breking news: {selected_subject} {selected_action} {selected_place}"

    print("\n" + headline)

    user_input = input("do you want more headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("thanks for using a fake news generator: have a good day")