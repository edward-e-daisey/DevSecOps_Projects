set -ex

VERSION=$TAG
cd ${WORKSPACE}/DevOps_Project_3

export AWS_PROFILE="ed_devops_project"

echo $AWS_PROFILE

whoami
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin "... ..."

sudo docker build -t nginx-application .

sudo docker tag nginx-application:latest ... ...:$VERSION

sudo docker push ... ...:$VERSION

DOCKER_IMAGE="... ...:$VERSION"

sed -i "s@devops_image@$DOCKER_IMAGE@g" nginx_deployment.yaml

cat nginx_deployment.yaml

aws eks update-kubeconfig --name mycluster --region us-east-1 --profile ed_devops_project

kubectl apply -f nginx_deployment.yaml

kubectl expose deployment nginx-deployment --type=LoadBalancer --name=nginx-service
