# -----------------------------------------------------------------------------------------------------
# Routine to send Whatssap Messages to a given number using pywhatkit library
# Made with ❤️ in Python 3 by Alvison Hunter - March 3rd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------------------------------------
import pyautogui as pg
import pywhatkit
import datetime as dt

def send_chat_msg():
    try:
        # Get current information about the time we run this
        now = dt.datetime.now()
        hour = now.hour
        minute = int(now.minute)+1

        # message to be sent
        msg = input("Please enter message to send: ")
        phone_num = input("Please enter Phone Number | Example +50588638751 : ")

        # Let us do the magic on this part of the code
        pywhatkit.sendwhatmsg(phone_num,msg,hour,minute)

        # additional events can be handled with the PyautoGUI library for example these ones
        pg.typewrite(" Deberias echarle un vistazo al lenguaje Python, vale la pena.")
        pg.press("enter")
        print("Your message has been successfully sent! ")
    except Exception as e:
        print(f"An Unexpected Error!{e}")

send_chat_msg()

# I'd like to give a big shout-out to my dear brother Engel Torres whose phone number is receiving
# my messages at this moment. Thank you for being a great programmer & an excellent musician.
