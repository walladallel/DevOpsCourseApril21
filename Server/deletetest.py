bucket1 ='youtube-crawler-bucket'
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket1)
bucket.objects.filter(Prefix="as/").delete()