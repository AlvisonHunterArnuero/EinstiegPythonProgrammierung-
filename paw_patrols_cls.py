import random
class PawPatrol:
    # Constructor and class attributes
    def __init__(self, name, breed, profession):
        self.name = name
        self.breed = breed
        self.profession = profession
        self.pup_catch_phrases_dict  = {"Marshall":"Ready for a ruff ruff rescue!",
                               "Rubble":"Rubble on the double!",
                               "Chase":"Chase is on the case",
                               "Rocky":"Green means go!",
                               "Zuma":"Let's dive in!",
                               "Skye":"This pup's gotta fly!"}

    # Common class methods
    def bark(self):
        print("-"*80)
        print(f"Profile Details for: {self.name}")
        print(f"Woof Woof, {self.pup_catch_phrases_dict.get(self.name)}")

    def yelp(self):
        print("-"*80)
        print("Whenever you're in trouble, just yelp for help!")

    def description(self):
        print(f"{self.name} is a {self.breed} pup that serves as {self.profession} in the Paw Patrols.")
        print("-"*80)

def main():
    catchphrase_list = ["No job is too big, no pup is too small!","PAW Patrol, to the Lookout!","PAW Patrol is on a roll!","PAW Patrol, to the PAW Patroller!"]
    # Declare a list of lists containing the information for the main characters of the series, shall we?
    pups_lst = [['Marshall', 'Dalmatian','FireFighter'],['Rubble', 'Bulldog','Constructor'],['Chase', 'German Shepherd','Police'],['Rocky', 'Mongrel','Handyman'],['Zuma', 'Labrador Retriever','Aquatic Rescuer'],['Skye', 'Cockapoo','Aviator']]
    # Let's greet the PawPatrol way, shall we?
    print(f"\nRyder says: {random.choice(catchphrase_list)}")
    # Set details for each of the Paw Patrols on the lists
    for pup in pups_lst:
        # let's create the  instance of the Parent Class to fill it up with the list details
        pup = PawPatrol(pup[0],pup[1],pup[2])
        # Call the methods on the parent class
        pup.bark()
        pup.yelp()
        pup.description()
        # If we have reached the last pup on the list, lets wrap the routine, otherwise
        # let's keep asking the use to hit enter to continue reading the next pup details
        if(pup.name != "Skye"):
            input("Press Enter to Continue...")
        else:
            print('Thanks for your support to the channel. Keep watching our videos!')

if __name__ == "__main__":
    main()
