. config.sh

docker load < $IMAGE_FILE
docker run --name $CONTAINER -p 8888:8888 -p 6006:6006 -v $(pwd)/workspace:/root/workspace -tid $IMAGE bash
docker stop $CONTAINER
