from create_user import create_user
from noams_youtube import search_download
import pyfiglet
from termcolor import colored
search_results =1

# App Welcome Sign
welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

# Asking for Username and Creating a User
username = input("Enter Username: ")

# Creating a username for Youtube Crawler
create_user(username)

# Welcome Message for newly subscribed user
print((colored("Hey '{}' And Welcome to Youtube Crawler Ver. 1.0.0-beta".format(username), 'magenta', attrs=['bold'],)))
print("------------------------------------------------------------")

# Asking User for a Serach String
# If you only want to download a test video enter ---> youtube-dl test video

search_str = input("Please Enter A Topic To Download: ")

# Calling Youtube-Crawler With search_str,search_results,username
search_download(search_str,search_results,username)












