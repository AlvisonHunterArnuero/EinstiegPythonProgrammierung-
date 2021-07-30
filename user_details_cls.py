# --------------------------------------------------------------------------------
# Introduction to classes using a basic grading score for an student
# Made with ❤️ in Python 3 by Alvison Hunter - March 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
class UserDetails:
    user_details = {
        'name':None,
        'age': None,
        'phone':None,
        'post':None
    }
    # Constructor and Class Attributes
    def __init__(self):
        self.name = None
        self.age = None
        self.phone = None
        self.post = None

    # Regular Methods
    def display_divider(self, arg_char = "-", line_length=100):
        print(arg_char*line_length)

    def fill_user_details(self):
        self.user_details['name'] = self.name
        self.user_details['age'] = self.age
        self.user_details['phone'] = self.phone
        self.user_details['post'] = self.post

    # GETTER METHODS
    # a getter function, linked to parent level properties
    @property
    def name(self):
        print("getting the name")
        return self.__name

    # a getter to obtain all of the properties in a whole method
    def get_user_details(self):
        self.fill_user_details()
        self.display_divider()
        print(self.user_details)

    # SETTER METHODS
    # a setter function, linked to parent level properties
    @name.setter
    def name(self, name):
        self.__name = name

    # a setter to  change all the properties in a whole method
    def set_user_details(self,name, age, phone, post):
        if(name==None or age==None or phone==None or post==None):
            print("There are missing  or empty parameters on this  method.")
        else:
            self.name = name
            self.age = age
            self.phone = phone
            self.post = post
            self.display_divider()
            print(f"We've successfully register the user details for {self.name}.")

# Let us create the instances now
new_user_01 = UserDetails()
new_user_01.set_user_details('Alvison Hunter',40,'8863-8751','The Life of a Web Developer')
new_user_01.get_user_details()

# Using the setter to update one property from parent, in this case the name
new_user_01.name = "Lucas Arnuero"
new_user_01.get_user_details()

# Another instance only working with the entire set of properties
new_user_02 = UserDetails()
new_user_02.set_user_details('Onice Acevedo',29,'8800-0088','Working From Home Stories')
new_user_02.get_user_details()
