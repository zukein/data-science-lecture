. config.sh

# exportでは作業ディレクトリなどの情報が失われるのでsaveを使う
docker save $IMAGE > $IMAGE_FILE
