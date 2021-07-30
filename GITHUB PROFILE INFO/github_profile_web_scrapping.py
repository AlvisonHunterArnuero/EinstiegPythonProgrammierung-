# ------------------------------------------------------------------------------------------
# From a Github Profile, grab a couple of details that'll give us information about its user
# ------------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - April 5th, 2021
# For JavaScript, Python & Web Development tips, visit our channel: https://bit.ly/3p9hpqj
# ------------------------------------------------------------------------------------------
import requests
import textwrap
from bs4 import BeautifulSoup as bs

# Base list of user profiles.
gh_profiles_lst = ['getify', 'maxschwarzmueller', 'AlvisonHunterArnuero']

# Constants to draw box with title & screen line divider
TOP_BOX_LINES = "╔" + "═"*88 + "╗"
BOTTOM_BOX_LINES = "╚" + "═" * 88 + "╝"
BOX_TITLE = "USER PROFILE #"  # The title inside the box
HORIZ_LINE = "-"*90  # simple data divider on screen

# Get current user github profile, add it to gh_profiles_lst
get_profile_name = input("Enter Github User Name: \n")
print("Retrieving information. Please wait...")

# If no user name is provided, let's add Guido Van Rossum
gh_profiles_lst.append('gvanrossum') if (
    not get_profile_name) else gh_profiles_lst.append(get_profile_name)

# Time to try all of this, let us do it, folks!
try:
    for ind, user in enumerate(gh_profiles_lst):
        gh_user = user
        url = "https://github.com/" + gh_user
        r = requests.get(url)
        
        soup = bs(r.content, 'html.parser')
        name = soup.select_one('span.p-name').get_text(strip=True)
        nickname = soup.select_one('span.p-nickname').get_text(strip=True)
        followers = soup.select_one('div.mb-3 > a > span').get_text(strip=True)
        bio = soup.select_one('div.p-note').get_text()
        company = soup.select_one('span.p-org').get_text()
        location = soup.select_one('span.p-label').get_text()
        repos = soup.select_one(
            'a.UnderlineNav-item > span').get_text(strip=True)
        contributions = soup.select_one(
            'div.position-relative > h2').get_text()

        # Let's grab the Repositories that are currently pinned on the Profile
        pinned_repos = []
        for elem in soup.find_all(class_="repo"):
            pinned_repos.append(elem.text.strip())

        # Let's wrapup the Profile Bio Content Text
        wrapper = textwrap.TextWrapper(width=88)
        word_list = wrapper.wrap(text=bio)

        # Let's add a boxed Header for each of the profiles
        print(f"{TOP_BOX_LINES}")
        print(f"║ {(BOX_TITLE+str(ind+1)).ljust(86)} ║")
        print(f"{BOTTOM_BOX_LINES}")

        # Additional profile information comes on these lines now
        print(f"NAME: {name} | NICKNAME: {nickname} | FOLLOWERS: {followers}")
        print(HORIZ_LINE)  # This is a simple dashed line on the screen
        print("PROFILE BIO:")

        # Print each line from the BIO object.
        for element in word_list:
            print(element)
        print(HORIZ_LINE)  # This is a simple dashed line on the screen
        print(f"COMPANY: {company} | LOCATION: {location}")
        print(HORIZ_LINE)  # This is a simple dashed line on the screen
        print(
            f"REPOSITORIES: {repos} | LAST YEARS CONTRIBUTIONS: {contributions.lstrip().split(' ')[0]}")
        print(HORIZ_LINE)  # This is a simple dashed line on the screen
        print("CURRENT PINNED REPOSITORIES:")
        print(HORIZ_LINE)  # This is a simple dashed line on the screen

        # If the pinned repos are less than 6, let's add the difference
        if len(pinned_repos) < 6:
            for el in range(6-len(pinned_repos)):
                pinned_repos.append("--")

        # Time to display all of this on the screen, shall we?
        for i, elem in enumerate(pinned_repos, 1):
            print(str(elem.title()).ljust(30), end='\n' if i % 3 == 0 else ' ')
        print(HORIZ_LINE)

# If we are unable to find the provided user, let us handle it like this
except AttributeError:
    print(HORIZ_LINE)  # This is a simple dashed line on the screen
    print(
        f"Uh oh! We are unable to find user << {gh_user} >> on Github Records.")
    print(HORIZ_LINE)  # This is a simple dashed line on the screen
    quit
