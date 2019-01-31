. config.sh

docker exec $CONTAINER jupyter notebook stop
rm out.log err.log
docker stop $CONTAINER
