import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(ImageId='ami-0a313d6098716f372', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='linux-sandbox')

for instance in instances:
  instance.create_tags(Tags=[{'Key':'Name', 'Value':'Mario_Alcantar'}, {'Key':'Server_Type', 'Value':'Webserver'}]) 