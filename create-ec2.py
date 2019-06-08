import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
ubuntu_instances = ec2.create_instances(ImageId='ami-024a64a6685d05041', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='linux-sandbox')

for instance in ubuntu_instances:
  instance.create_tags(Tags=[{'Key':'Name', 'Value':'Mario_A'}, {'Key':'Server_Type', 'Value':'Ubuntu-Webserver'}]) 
  
windows_instances = ec2.create_instances(ImageId='ami-0a9ca0496f746e6e0', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName='linux-sandbox')

for instance in windows_instances:
  instance.create_tags(Tags=[{'Key':'Name', 'Value':'Mario_A'}, {'Key':'Server_Type', 'Value':'Windows-Webserver'}]) 