from create_user import create_user
from noams_youtube import search_download
import pyfiglet

welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

username = input("Enter Username: ")
# Creating a username for Youtube Crawler
create_user(username)

#Welcome Message for newly subscribed user
print("Hello {} and Welcome to Youtube Crawler".format(username))

#Asking User for Serach_String
search_str = input("Please Enter A Topic: ")
#Sending Youtube-Crawler User Name and serach_String
search_download(search_str,1,username)











