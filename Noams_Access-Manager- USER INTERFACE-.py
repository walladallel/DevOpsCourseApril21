from create_user import create_user
from noams_youtube import search_download
import pyfiglet

welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)


# Creating a username for Youtube Crawler
create_user()
#Welcome Message for newly subscribed user

#Asking User for Serach_String
#Sending Youtube-Crawler User Name and serach_String
search_download()








