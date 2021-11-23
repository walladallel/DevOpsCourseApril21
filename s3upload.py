import boto3
s3 = boto3.resource('s3')
name = "noam"
s3.meta.client.upload_file('hello.txt', 'youtube-crawler-bucket', name +'/hello.txt')
