class PawPatrol:
    # Constructor and class attributes
    def __init__(self, name, breed, profession):
        self.name = name
        self.breed = breed
        self.profession = profession

    # Common class methods
    def bark(self):
        print(self.name + " is barking.")

    def yelp(self):
        print(self.name + " simply yelps for help.")

    def description(self):
        print(f'{self.name} is a {self.breed} pup that serves as {self.profession} in the Paw Patrols.')
        print('='*70)


def main():
    pups_lst = [['Marshall', 'Dalmatian','FireFighter'],['Rubble', 'Bulldog','Constructor'],['Chase', 'German Shepherd','Police'],['Rocky', 'Mongrel','Handyman'],['Zuma', 'Labrador Retriever','Aquatic Rescuer'],['Skye', 'Cockapoo','Aviator']]
    # Set details for one of the Paw Patrols
    for pup in pups_lst:
        pup = PawPatrol(pup[0],pup[1],pup[2])
        pup.bark()
        pup.yelp()
        pup.description()
        if(pup.name != "Skye"):
            print(f'Hit enter to get the information of the next Puppie:')
            input()
        else:
            print('Thanks for your support to the channel. Keep watching our videos!')

if __name__ == "__main__":
    main()
