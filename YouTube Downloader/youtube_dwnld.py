# This Script will download YouTube videos using the pafy & youtube_dl packages
# To install, please use pip install pafy and pip install youtube_dl
# NOTE: You will have to configure your own SSL in your machine in order to work
# https://www.youtube.com/watch?v=I2wURDqiXdM
# https://www.youtube.com/watch?v=ErcV8vlKexE
# Made with ❤️ in Python 3 by Alvison Hunter - January 23rd, 2021
import pafy
import sys
def get_video():
    try:
        url = input("Please Enter your video URL:")
        print("Obtaining video information, please wait...")
        clip = pafy.new(url)
        print(f"Title: {clip.title}  | Length: {clip.length}  | Rating: {clip.rating}")
        dl =  clip.getbest(preftype="mp4")
        print(f"We are downloading at this quality: {dl.resolution} in {dl.extension} format.")
        myfilename = f"{sys.path[0]}/{clip.title}.{dl.extension}"
        print(f"Saving this file as: {clip.title} in {sys.path[0]}/")
        dl.download(progress=False, filepath=myfilename)
    except Exception as err:
        print(f"Uh Oh! An error has occurred: {err}")
    else:
        print(f"{clip.title} was successfully downloaded.")

get_video()
