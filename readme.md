
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


curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


## docker commands
docker login<br>
docker ps --> list all the running images in background<br>
docker ps -a --> list all the container made by the developer<br>
docker rm container_id --> remove the running or static container<br>
docker rm container_id -f --> forceful remove<br>
docker run -t docker_image_name --> run the container for non server application<br>
docker run -t -p 8000:8000 docker_image_name --->for server application<br>
docker run -t -p 8000:8000 -d docker_image_name --> running image in the background<br>
docker rm container_id -f --> remove the container from the docker running in backround<br>
docker exec -it container_id bash --> for getting into the docker vm or docker terminal<br>