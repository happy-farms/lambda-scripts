import boto3
import os

def start_ec2(tag_key, tag_value):
    # os.environ['AWS_PROFILE'] = 'tel-dev'
    print ("This lambda fuction will stop non-prod EC2 at specific time")
    print ("Please define tag_key and tag_value of resource in variables for it, Lamdba will find EC2 instance which has those tag to stop")

    ec2=boto3.resource('ec2')

    nonprod_instance_iterator=ec2.instances.filter(
        Filters=[
            {
                'Name': 'tag:'+ tag_key,
                'Values': [
                    tag_value,
                ]
            }
        ]
        )

    print("list of EC2 instaces has tag_key:" + tag_key + "and tag_value:" + tag_value)
    for instance in nonprod_instance_iterator:
        print(instance.instance_id)

    print("stopping those EC2 instances")
    for instance in nonprod_instance_iterator:
        instance.start()

    print ("script done, please check")

def handler(event, context):
    start_ec2('Environment', 'dev')
