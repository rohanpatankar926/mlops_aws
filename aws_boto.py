import boto3
ec2=boto3.resource('ec2')

# def create_instance(id="ami-0f8ca728008ff5af4", type="t2.micro"):
instances = ec2.create_instances(
        ImageId=id,
        MinCount=1,
        MaxCount=1,
        InstanceType=type,
        KeyName="KeyPair1"
    )



import boto3
 
ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
	    InstanceIds=[
        'i-06707f89166c35fba',
    ],
)
# os.system("aws ec2 create-key-pair --key-name KeyPair1 --query 'KeyMaterial' --output text > KeyPair1.pem")
