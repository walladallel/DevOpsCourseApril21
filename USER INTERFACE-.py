from create_user import create_user
from noams_youtube import search_download
import pyfiglet
search_results =1

#App Welcome Sign
welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

#Asking for Username and Creating a User
username = input("Enter Username: ")
# Creating a username for Youtube Crawler
create_user(username)

#Welcome Message for newly subscribed user
print("Hello {} and Welcome to Youtube Crawler".format(username))
print("--------------------------------------------")

#Asking User for Serach_String
print("Test -->   ","youtube-dl test video")
search_str = input("Please Enter A Topic To Download: ")

#Sending Youtube-Crawler User Name and serach_String
search_download(search_str,search_results,username)












