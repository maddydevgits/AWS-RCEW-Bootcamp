import boto3
import random

#client=boto3.client('sns',aws_access_key_id='',aws_secret_access_key='',region_name='')
#us-east-1

client=boto3.client('sns',aws_access_key_id='AKIAXHI5XG5NLGEEC7IO',aws_secret_access_key='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',region_name='us-east-1')
count=0

while True:
    k=random.randint(10,50)
    print(k)
    if(k>25):
        response=client.publish(TopicArn='arn:aws:sns:us-east-1:496667932506:rcew',Message='Hi Hello')
        print(response)
        count+=1
    if(count==2):
        break