docker load < python.tar
docker run --name dslec -p 8888:8888 -p 6006:6006 -v $(pwd)/workspace:/root/workspace -tid scenesk/dslec:0.1 bash
docker stop dslec
