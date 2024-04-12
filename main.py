import boto3

import boto3
from botocore.config import Config
# Let's use S3
s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id='jwapWbprD3ZsAVLo',
    aws_secret_access_key='2pgH4cCkEY7EELZGA0zcRRvydMCTdf0ZzgBq9X3r',
    endpoint_url='https://s3.tebi.io',
    )





#
# for bucket in s3.buckets.all():
#     for obj in bucket.objects.all():
#         print(obj)


#
# data = open('main.py', 'rb')
# print(data.read())
# s3.Bucket('progenz').put_object(Key='main.py', Body=data)

# # # #
# with open('c:/Users/Администратор/Downloads/iMe Desktop/Zohirshoh_Jorayev_-_Tamom_boldim_man_(www.zamonaviy.uz).mp3','rb') as f:
#     print(s3.Bucket('progenz').put_object(Key='musicwww.mp3', Body=f))




print(s3.Bucket('progenz').download_file('musicwww.mp3', 'smth.mp3'))

