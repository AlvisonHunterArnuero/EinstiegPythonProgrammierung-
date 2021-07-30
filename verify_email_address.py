# --------------------------------------------------------------------------------
# Routine to verify a given email address and returns its boolean status.
# Made with ❤️ in Python 3 by Alvison Hunter - March 27th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
import re
def validate_email(arg_email):
    is_valid = True
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    is_valid = False if not EMAIL_REGEX.match(arg_email) else True
    print("Email is valid" if is_valid else "Invalid email address.")


validate_email("alvisonhunter@outlook.com") # This email address is valid
validate_email("alvisondr.com") # missing an @
validate_email("alvison@@peachtreelightscapes.com") # Double @ in the email
validate_email("alvison.hunter@concentrixcom") # missing the dot


