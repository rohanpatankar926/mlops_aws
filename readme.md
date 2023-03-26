
#### For installing awscli use this command 
pip install awscli

#### For configuring aws in vs code terminal 
aws configure
Get these details after creating IAM role
-->aws access key 
-->aws access key id
-->region --> ap-south-1
-->output-->json

aws configure list

cat ~/.aws/config

https://blog.knoldus.com/how-to-create-ec2-instance-using-python3-with-boto3/


### day2

cloud watch alarm 
1-->add and create a cloudwatch monitoring to stop instance 
2-->goto aws console and run
`sudo apt-get install stress`
`stress --cpu 8` --> run stress for 8 worker nodes
after 5 mins we can able to generate an alarm wrt cloud-watch
