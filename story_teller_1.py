import time
import random

for x in range(5):
    namelist = ["Elvina", "Sherry", "Evonne", "Ariane", "Dorie", "Pinkie", "Somer", "Soledad", "Digna", "Susana",
                "Lael",
                "Elias", "Cody", "Cyrus", "Anjanette", "Aubrey", "Earline", "Chan", "Kandice", "Bernadine", "Judi",
                "Leatrice", "Miguelina", "Libbie", "Ginger", "Karine", "Lorri", "Charlette", "Eartha", "Beverlee",
                "Lizabeth", "Judie", "Lennie", "Johnnie", "Laverna", "Orville", "Jamee", "Claretha", "Jami",
                "Philomena",
                "Cole", "Reid", "Cara", "Wanetta", "Lila"]
    eventlist_whitout_secret_mission = ["party", "swimming practice", "programming course", "family reunion"]
    random_event_whitout_secret_mission = random.choice(eventlist_whitout_secret_mission)
    locationlist = ["the shop", "the airport", "work", "Cybercom", "a Esports tournament", "the moon", "Atlantis"]
    foodlist = ["moldy cheeseburger", "poisoned cupcake", "regular pbj-sandwich"]
    eventlist = ["party", "swimming practice", "programming course", "family reunion",
                 "secret mission, I mean ehh " + random_event_whitout_secret_mission + "..."]
    random_name = random.choice(namelist)
    random_location = random.choice(locationlist)
    random_food = random.choice(foodlist)
    random_event = random.choice(eventlist)
    print("This is a story about an human being named " + random_name + "!")
    print("One day when " + random_name + " was at " + random_location + ", " + random_name +
          " had a weird feeling. It was probably the " + random_food + " from yesterdays " +
          random_event + ". Too bad " + "that " + random_name + " had eaten that.      ***THE END***")

    time.sleep(1)
