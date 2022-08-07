# abort on errors
set -e

if [[ $(docker images | grep aiogram-template) ]]; then
    echo "[ + ] Docker image exists"
else
    echo "[ ~ ] Building docker image..."
    docker build -t aiogram-template .
fi
echo '[ ~ ] Running bot...'
docker run -it --rm -v $PWD:/home/telegram aiogram-template
