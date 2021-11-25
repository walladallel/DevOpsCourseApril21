from create_user import create_user
import pyfiglet
from termcolor import colored

# App Welcome Sign
welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

# Asking for Username and Creating a User
username = input("Enter Username: ")

# Creating a username for Youtube Crawler
create_user(username)


# Welcome Message for newly subscribed user
print((colored("Hey '{}' And Welcome to Youtube Crawler By Noam -Ver. 1.0.0-beta ".format(username), 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")

# Asking User for a Search String
# If you only want to download a test video enter ---> youtube-dl test video
search_str = input("Please Enter A Topic To Download: ")
print("------------------------------------------------------------")
number = input("Please Enter A Number Of Videos To Download: ")
print("------------------------------------------------------------")
from youtube import upload
# Calling Youtube-Crawler With search_str,search_results,username
upload(username,search_str,number)

print("------------------------------------------------------------")
print((colored('Thank You {} for Using Youtube Crawler By Noam \U0001f60d'.format(username), 'blue', attrs=['bold'],)))
print("------------------------------------------------------------")
exit(0)












