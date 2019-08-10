. config.sh

docker start $CONTAINER
chmod 777 workspace/notebook.sh
docker exec $CONTAINER nohup /root/workspace/notebook.sh > out.log 2> err.log &
echo 'Access 127.0.0.1:' $JUPYTER_PORT ' for Jupyter (pass:jupyter)'
