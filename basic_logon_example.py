# ------------------------------------------------------------------------------------
# Small routine to simulate a basic login access to an app, nothing fancy, very simple.
# ------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - February 28th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ------------------------------------------------------------------------------------

# First, let us simulate that we obtained an external object using a query to a remote DB,
# We should NOT hardcode any confidential information such as password, pin numbers, etc
dict_users = {
    "batman": 4523,
    "superman": 3456,
    "aquaman": 1223,
    "flash": 4567,
    "wonderwoman": 1523,
    "greenarrow": 8978,
}

# Declare the common messages constants in a dictionary to make our life easier
dict_error_msg = {
    "SUCCESS_LOGON": "You Have Successfully Logged in to CodeCrafters Labs.",
    "INVALID_USR_PIN": "Username or Pin Number is incorrect. Please try again.",
    "INVALID_INTEGER_TYPE": "Error! Pin Number can only contain integer numbers.",
    "VERIFY_TRY_AGAIN": "Please verify the number and try again.",
    "LOGIN_ERROR": "An unexpected error has occurred. Please try again in a few minutes.",
    "LOGIN_ATTEMPTS_MSG": "You've reached the maximum logon attempts.",
}

def display_divider(self, arg_char = "-", line_length=100):
    print(arg_char*line_length)

# This will be our function, where all the magic happens
def login():
    # We will gather 3 attempts to login and fail. If this goes more than 3, we will exit this routine
    num_attempts = 0
    # Loop this app until we break it with any of the below conditions
    while True:
        # Always remember to handle your exceptions, errors must be handled, that's a must
        try:
            user_name = input("User Name: ").lower()
            pin_num = int(input("Pin Number: "))
            if (user_name in dict_users) and (pin_num in dict_users.values()):
                print(" " * 80)
                print(
                    f"Welcome back, {user_name.title()}: {dict_error_msg['SUCCESS_LOGON']}"
                )
                print(" " * 80)
                break
            else:
                num_attempts = 1
                if num_attempts >= 3:
                    print(f"Uh Oh! {dict_error_msg['LOGIN_ATTEMPTS_MSG']}")
                    break
                else:
                    print(dict_error_msg["INVALID_USR_PIN"])
                    continue
        except ValueError:
            print(dict_error_msg["INVALID_INTEGER_TYPE"])
            print(dict_error_msg["VERIFY_TRY_AGAIN"])
            continue


# Let us call the function now
login()
