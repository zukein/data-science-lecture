. config.sh

docker build -t $IMAGE .
docker run --name $CONTAINER -p $JUPYTER_PORT:8888 -p $TENSOR_BOARD_PORT:6006 -v $(pwd)/workspace:/root/workspace -tid $IMAGE bash
docker exec $CONTAINER pip freeze > requirements.txt
docker stop $CONTAINER
