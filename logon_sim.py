# Routine to recreate a simple logon attempt, NOT AUTHENTICATED.
# Made with ❤️ in Python 3 by Alvison Hunter - April 3rd, 2021
# Find more JavaScript & Python Tips at: https://bit.ly/3p9hpqj

# Divider function, nothing special, just a line in the screen
def display_divider(arg_char="-", line_length=100):
    print(arg_char*line_length)


def logon_simulator():
    usr_name = "Batman"
    usr_pwd = "Goth@mCity2021"
    attempts = 0
    success_login = False
    SUCCESSFUL_LOGIN_MSG = "🆗 You've successfully logged in into your account."
    MAX_ATTEMPTS_MSG = "ℹ️ You've reached the max amount of attempts to logon."
    FAILED_LOGIN_MSG = "❌ Unfortunately the user or password provided was incorrect."

    while True:
        try:
            if attempts >= 3:
                print(MAX_ATTEMPTS_MSG)
                break
            else:
                display_divider("-", 70)
                user_inp = input("👤 Please Enter your Username: \n")
                pwd_inp = input("🔑 Please Enter your Password: \n")
                attempts += 1
                success_login = True if (
                    user_inp == usr_name and pwd_inp == usr_pwd) else False

                if success_login == True:
                    display_divider("-", 70)
                    print(SUCCESSFUL_LOGIN_MSG)
                    display_divider("-", 70)
                    break
                else:
                    print(
                        f"⏬ You've used {attempts} out of 3 attempts to login.")
                    display_divider("-", 70)
                    print(FAILED_LOGIN_MSG)
                    continue
        except:
            print("Uh oh! Something went really wrong!. Please try again.")
            quit


logon_simulator()
