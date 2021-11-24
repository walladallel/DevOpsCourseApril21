import boto3
client = boto3.client('iam')
print("Getting users from IAM...")
response_userlist = client.list_users()
print(response_userlist)
userlist=response_userlist['Users'][x]['UserName']
for x in userlist:
    print (x)