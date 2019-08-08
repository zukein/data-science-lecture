. "config.ps1"

docker build -t $IMAGE .
docker run --name $CONTAINER -p 8888:8888 -p 6006:6006 -v $pwd/workspace:/root/workspace -tid $IMAGE bash
docker exec $CONTAINER pip freeze > requirements.txt
docker stop $CONTAINER
