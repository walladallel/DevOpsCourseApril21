from create_user import create_user
import pyfiglet

welcome = pyfiglet.figlet_format("Youtube Crawler")
print(welcome)

# TODO insert a while loop here
# Asking User to For a username to create a sub in app
username=(input("Please Enter Your User Name: "))
# Inserting input into create_user Function
create_user(username)
# TODO finish Youtube-crawaler and insert it here






