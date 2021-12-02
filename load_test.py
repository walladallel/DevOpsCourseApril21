import requests

while True:
    response = requests.get('http://flask-app-lb-1168614534.us-east-1.elb.amazonaws.com/')
    print(response.text)



