docker start dslec
docker exec dslec nohup bash /root/workspace/python/notebook.sh > out.log 2> err.log &
echo 'Access 127.0.0.1:8888 for Jupyter (pass:jupyter)'
